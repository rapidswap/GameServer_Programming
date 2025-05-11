#pragma once
#include "stdafx.h"
#include "ContentsProcess.h"

ContentsProcess::ContentsProcess()
{
	xml_t config;
	if (!loadConfig(&config)) {
		return;
	}
	this->initialize(&config);

	runFuncArray_.fill(&ContentsProcess::handleInvalidPacket);
}

ContentsProcess::~ContentsProcess()
{
	SAFE_DELETE(packageQueue_);

	for (auto thread : threadPool_) {
		SAFE_DELETE(thread);
	}
	runFuncTable_.clear();
}

void ContentsProcess::initialize(xml_t *config)
{
	xmlNode_t *root = config->FirstChildElement("App")->FirstChildElement("Contents");
	if (!root) {
		SErrLog(L"* not exist process setting");
		return;
	}
	xmlNode_t *elem = root->FirstChildElement("ThreadCount");
	int processCount = 0;
	sscanf_s(elem->GetText(), "%d", &processCount);

	if (MAX_PACKET_THREAD_ < processCount) {
		SErrLog(L"! processThread limit[%d], but config setting [%d]", MAX_PACKET_THREAD_, processCount);
		return;
	}

	packageQueue_ = new ThreadJobQueue<Package *> (L"ContentsProcessQueue");
	for (int i = 0; i < processCount; ++i) {
		threadPool_[i] = MAKE_THREAD(ContentsProcess, process);
	}
	this->registDefaultPacketFunc();
}

void ContentsProcess::registDefaultPacketFunc()
{
	runFuncTable_.insert(make_pair(E_C_NOTIFY_HEARTBEAT, &ContentsProcess::Packet_HeartBeat));
	runFuncTable_.insert(make_pair(E_I_NOTIFY_TERMINAL, &ContentsProcess::Packet_Notify_Terminal));
	runFuncTable_.insert(make_pair(E_C_REQ_EXIT, &ContentsProcess::C_REQ_EXIT));

	runFuncArray_[E_C_NOTIFY_HEARTBEAT] = &ContentsProcess::Packet_HeartBeat;
	runFuncArray_[E_I_NOTIFY_TERMINAL] = &ContentsProcess::Packet_Notify_Terminal;
	runFuncArray_[E_C_REQ_EXIT] = &ContentsProcess::C_REQ_EXIT;
}

void ContentsProcess::putPackage(Package *package)
{
	packageQueue_->push(package);
}

void ContentsProcess::run(Package* package)
{
	PacketType type = package->packet_->type();

	// 배열 인덱싱으로 직접 접근 (안전 검사 포함)
	if (type >= 0 && type < MAX_PACKET_TYPE_NUM) {
		RunFunc runFunction = runFuncArray_[type];
#ifdef _DEBUG
		SLog(L"*** [%d] packet run ***", type);
#endif //_DEBUG
		runFunction(package->session_, package->packet_);
	}
	else {
		// 범위를 벗어난 경우 기존 방식으로 폴백
		auto itr = runFuncTable_.find(type);
		if (itr == runFuncTable_.end()) {
			SLog(L"! invalid packet runFunction. type[%d]", type);
			package->session_->onClose();
			return;
		}
		RunFunc runFunction = itr->second;
#ifdef _DEBUG
		SLog(L"*** [%d] packet run ***", type);
#endif //_DEBUG
		runFunction(package->session_, package->packet_);
	}
}

void ContentsProcess::execute()
{
	Package *package = nullptr;
	if (packageQueue_->pop(package) == false) {
		return;
	}

	this->run(package);
	
	SAFE_DELETE(package);
}

void ContentsProcess::process()
{
	const int BATCH_SIZE = 16; // 적절한 배치 크기
	std::vector<Package*> batch(BATCH_SIZE);

	while (_shutdown == false) {
		int processedCount = 0;

		// 배치 단위로 한 번에 여러 작업 가져오기
		for (int i = 0; i < BATCH_SIZE; i++) {
			Package* package = nullptr;
			if (packageQueue_->pop(package)) {
				batch[processedCount++] = package;
			}
			else {
				break;
			}
		}

		// 가져온 작업 처리
		for (int i = 0; i < processedCount; i++) {
			this->run(batch[i]);
			SAFE_DELETE(batch[i]);
		}

		// 처리할 작업이 없을 때만 컨텍스트 스위칭
		if (processedCount == 0) {
			CONTEXT_SWITCH;
		}
	}
}


void ContentsProcess::Packet_HeartBeat(Session *session, Packet *rowPacket)
{
	if (session->type() != SESSION_TYPE_CLIENT) {
		return;
	}
	session->updateHeartBeat();
}

void ContentsProcess::Packet_Notify_Terminal(Session *session, Packet *rowPacket)
{
	session->setType(SESSION_TYPE_TERMINAL);
	SLog(L"* [%s] Terminal accepted.", session->clientAddress().c_str());
}

void ContentsProcess::C_REQ_EXIT(Session *session, Packet *rowPacket)
{
	PK_C_REQ_EXIT *packet = (PK_C_REQ_EXIT *)rowPacket;
	PK_S_ANS_EXIT ansPacket;

	SLog(L"ContentsPro!!!test!!!");
	SLog(L"* recv exit packet by [%s]", session->clientAddress().c_str());
	session->sendPacket(&ansPacket);
}

void ContentsProcess::handleInvalidPacket(Session* session, Packet* rowPacket) {
	PacketType type = rowPacket->type();
	SLog(L"! invalid packet runFunction. type[%d]", type);
	session->onClose();
}