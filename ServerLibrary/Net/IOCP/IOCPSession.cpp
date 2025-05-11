#include "stdafx.h"
#include "../Session.h"
#include "IOCPSession.h"
#include "../SessionManager.h"
#include "../Packet/PacketAnalyzer.h"

IoData::IoData()
{
	ZeroMemory(&overlapped_, sizeof(overlapped_));
	ioType_ = IO_ERROR;
	
	this->clear();
}

void IoData::clear()
{
	buffer_.fill(0);
	totalBytes_ = 0;
	currentBytes_ = 0;
}

bool IoData::needMoreIO(size_t transferSize)
{
	currentBytes_ += transferSize;
	if (currentBytes_ < totalBytes_) {
		return true;
	}
	return false;
}

int32_t IoData::setupTotalBytes()
{
	packet_size_t offset = 0;
	packet_size_t packetLen[1] = { 0, };
	if (totalBytes_ == 0) {
		memcpy_s((void *)packetLen, sizeof(packetLen), (void *)buffer_.data(), sizeof(packetLen));
		PacketObfuscation::getInstance().decodingHeader((Byte*)&packetLen, sizeof(packetLen));

		totalBytes_ = (size_t)packetLen[0];
	}
	offset += sizeof(packetLen);

	return offset;
}
size_t IoData::totalByte()
{
	return totalBytes_;
}

IO_OPERATION &IoData::type()
{
	return ioType_;
}

void IoData::setType(IO_OPERATION type)
{
	ioType_ = type;
}

char* IoData::data()
{
	return buffer_.data();
}

bool IoData::setData(Stream &stream)
{
	this->clear();

	if (buffer_.max_size() <= stream.size()) {
		SLog(L"! packet size too big [%d]byte", stream.size());
		return false;
	}

	const size_t packetHeaderSize = sizeof(packet_size_t);
	packet_size_t offset = 0;

	char *buf = buffer_.data();
	packet_size_t packetLen[1] = { (packet_size_t)packetHeaderSize + (packet_size_t)stream.size(), };
	memcpy_s(buf + offset, buffer_.max_size(), (void *)packetLen, packetHeaderSize);
	offset += packetHeaderSize;

	PacketObfuscation::getInstance().encodingHeader((Byte*)buf, packetHeaderSize);
	PacketObfuscation::getInstance().encodingData((Byte*)stream.data(), stream.size());

	memcpy_s(buf + offset, buffer_.max_size(), stream.data(), (int32_t)stream.size());
	offset += (packet_size_t)stream.size();

	totalBytes_ = offset;
	return true;
}

LPWSAOVERLAPPED IoData::overlapped()
{
	return &overlapped_;
}

WSABUF IoData::wsabuf()
{
	WSABUF wsaBuf;
	wsaBuf.buf = buffer_.data() + currentBytes_;
	wsaBuf.len = (ULONG)(totalBytes_ - currentBytes_);
	return wsaBuf;
}

//-----------------------------------------------------------------//
IOCPSession::IOCPSession()
: Session(), isBufferingEnabled_(true)
{
    this->initialize();
}

void IOCPSession::initialize()
{
	ZeroMemory(&socketData_, sizeof(SOCKET_DATA));
	ioData_[IO_READ].setType(IO_READ);
	ioData_[IO_WRITE].setType(IO_WRITE);
}

void IOCPSession::checkErrorIO(DWORD ret)
{
	if (ret == SOCKET_ERROR
		&& (WSAGetLastError() != ERROR_IO_PENDING)) {
        SLog(L"! socket error: %d", WSAGetLastError());
	}
}

void IOCPSession::recv(WSABUF wsaBuf)
{
	DWORD flags = 0;
	DWORD recvBytes;
	DWORD errorCode = WSARecv(socketData_.socket_, &wsaBuf, 1, &recvBytes, &flags, ioData_[IO_READ].overlapped(), NULL);
	this->checkErrorIO(errorCode);
}

bool IOCPSession::isRecving(size_t transferSize)
{
	if (ioData_[IO_READ].needMoreIO(transferSize)) {
		this->recv(ioData_[IO_READ].wsabuf());
		return true;
	}
	return false;
}

void IOCPSession::recvStandBy()
{
	ioData_[IO_READ].clear();

	WSABUF wsaBuf;
	wsaBuf.buf = ioData_[IO_READ].data();
	wsaBuf.len = SOCKET_BUF_SIZE;

	this->recv(wsaBuf);
}

void IOCPSession::send(WSABUF wsaBuf)
{
	DWORD flags = 0;
	DWORD sendBytes;
	DWORD errorCode = WSASend(socketData_.socket_, &wsaBuf, 1, &sendBytes, flags, ioData_[IO_WRITE].overlapped(), NULL);
	this->checkErrorIO(errorCode);
}

void IOCPSession::onSend(size_t transferSize)
{
	if (ioData_[IO_WRITE].needMoreIO(transferSize)) {
		this->send(ioData_[IO_WRITE].wsabuf());
	}
	
	if (sendBuffer_.size() > 0) {
		int sent = sendBuffer_.flush(this->socket());
		if (sent <= 0 && WSAGetLastError() != WSAEWOULDBLOCK) {
			// 오류 처리
			SLog(L"! IOCPSession::onSend flush failed. error:%d", WSAGetLastError());
			this->onClose();
		}
	}
}

void IOCPSession::sendPacket(Packet* packet)
{
	if (!isBufferingEnabled_) {
		// 기존 즉시 전송 로직 유지
		Stream stream;
		packet->encode(stream);

		// postSend 또는 기존 전송 메서드 호출
		if (!this->postSend(stream.data(), stream.size())) {
			SLog(L"! IOCPSession::sendPacket failed. error:%d", WSAGetLastError());
			this->onClose();
		}
		return;
	}

	// 버퍼링 활성화 시 패킷을 버퍼에 추가
	bool shouldFlush = sendBuffer_.addPacket(packet);

	if (shouldFlush) {
		// 임계값 초과 시 즉시 전송
		if (!this->postSend(reinterpret_cast<UCHAR*>(const_cast<char*>(sendBuffer_.data())),
			static_cast<DWORD>(sendBuffer_.size()))) {
			SLog(L"! IOCPSession::sendPacket flush failed. error:%d", WSAGetLastError());
			this->onClose();
		}
	}
}

bool IOCPSession::postSend(UCHAR* data, DWORD length)
{
	// 기존 데이터 송신 중이면 현재 데이터는 버퍼에 추가
	if (ioData_[IO_WRITE].totalByte() > 0) {
		// 버퍼가 비어있지 않으면 현재 송신 중인 데이터가 있음
		// 이 경우 sendBuffer_에 추가하고 true 반환
		return true;
	}

	// Stream 객체 생성
	Stream stream(data, length);

	// IoData에 스트림 데이터 설정
	if (!ioData_[IO_WRITE].setData(stream)) {
		SLog(L"! Failed to set data for sending");
		return false;
	}

	// WSABUF 준비
	WSABUF wsaBuf = ioData_[IO_WRITE].wsabuf();

	// 비동기 송신 시작
	this->send(wsaBuf);

	return true;
}


Package *IOCPSession::onRecv(size_t transferSize)
{
	packet_size_t offset = 0;
	offset += ioData_[IO_READ].setupTotalBytes();

	if (this->isRecving(transferSize)) {
		return nullptr;
	}

	const size_t packetHeaderSize = sizeof(packet_size_t);
	packet_size_t packetDataSize = (packet_size_t)(ioData_[IO_READ].totalByte() - packetHeaderSize);
	Byte *packetData = (Byte*) ioData_[IO_READ].data() + offset;

	PacketObfuscation::getInstance().decodingData(packetData, packetDataSize);
	Packet *packet = PacketAnalyzer::getInstance().analyzer((const char *)packetData, packetDataSize);
	if (packet == nullptr) {
		SLog(L"! invaild packet");
		this->onClose(true);
		return nullptr;
	}

	this->recvStandBy();

	Package *package = new Package(this, packet);
	return package;
}
