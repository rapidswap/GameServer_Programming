#include "stdafx.h"
#include "ChattingProcess.h"

ChattingProcess::ChattingProcess()
{
	this->registSubPacketFunc();
}

void ChattingProcess::registSubPacketFunc()
{
#define INSERT_PACKET_PROCESS(type)		runFuncTable_.insert(make_pair(E_##type, &ChattingProcess::##type))

	INSERT_PACKET_PROCESS(I_CHTTING_NOTIFY_ID);
	INSERT_PACKET_PROCESS(I_DB_ANS_PARSE_DATA);
	INSERT_PACKET_PROCESS(C_REQ_REGIST_CHATTING_NAME);
	INSERT_PACKET_PROCESS(C_REQ_CHATTING);
	INSERT_PACKET_PROCESS(C_REQ_CHAT_EXIT);
	INSERT_PACKET_PROCESS(C_REQ_PING);
	
}

void ChattingProcess::I_CHTTING_NOTIFY_ID(Session* session, Packet* rowPacket)
{
	PK_I_CHTTING_NOTIFY_ID* packet = (PK_I_CHTTING_NOTIFY_ID*)rowPacket;

	PK_I_DB_REQ_LOAD_DATA dbPacket;
	dbPacket.clientId_ = packet->clientId_;
	dbPacket.oidAccountId_ = packet->oidAccountId_;

	Terminal* terminal = _terminal.get(L"DBAgent");
	terminal->sendPacket(&dbPacket);
}

void ChattingProcess::I_DB_ANS_PARSE_DATA(Session* session, Packet* rowPacket)
{
	PK_I_DB_ANS_PARSE_DATA* packet = (PK_I_DB_ANS_PARSE_DATA*)rowPacket;

	PK_I_LOGIN_NOTIFY_ID_LOADED iPacket;
	iPacket.clientId_ = packet->clientId_;
	iPacket.name_ = packet->name_;
	iPacket.result_ = packet->result_;

	SLog(L"* [%S] name load from db", iPacket.name_.c_str());
	Terminal* terminal = _terminal.get(L"LoginServer");
	terminal->sendPacket(&iPacket);
}

void ChattingProcess::C_REQ_REGIST_CHATTING_NAME(Session* session, Packet* rowPacket)
{
	PK_C_REQ_REGIST_CHATTING_NAME* packet = (PK_C_REQ_REGIST_CHATTING_NAME*)rowPacket;
	User* user = UserManager::getInstance().at(session->id());
	if (user != nullptr) {
		SLog(L"! try duplicate regist : %s, name : %S", session->clientAddress().c_str(), packet->name_.c_str());
		session->onClose();
		return;
	}
	user = new User(session);

	array<WCHAR, SIZE_64> userName;
	StrConvA2W((CHAR*)packet->name_.c_str(), userName.data(), userName.size());
	user->setName(userName.data());
	UserManager::getInstance().insert(user);

	SLog(L"* user [%s] created from [%S]", userName.data(), session->clientAddress().c_str());

	PK_S_ANS_NEW_USER_NOTIFY notifyPacket;
	notifyPacket.name_ = packet->name_;
	UserManager::getInstance().broadcast(&notifyPacket, session->id());

	PK_S_ANS_USER_LIST listPacket;
	auto& userManager = UserManager::getInstance();
	std::vector<pair<oid_t, User*>> users = userManager.getAllUsers();

	SLog(L"* Current user count: %d", users.size());

	for (const auto& userPair : users) {
		if (userPair.first != session->id()) {  // �ڽ� ����
			User* existingUser = userPair.second;
			if (existingUser) {
				array<char, SIZE_64> existingName;
				StrConvW2A((WCHAR*)existingUser->name().c_str(), existingName.data(), existingName.size());
				listPacket.names_.push_back(string(existingName.data()));

				SLog(L"* Added user to list: %S", existingName.data());
			}
		}
	}

	SLog(L"* Sending user list with %d users", listPacket.names_.size());
	session->sendPacket(&listPacket);
}

void ChattingProcess::C_REQ_CHATTING(Session* session, Packet* rowPacket)
{
	// 메시지 수신 시간 기록
	UInt64 messageReceiveTime = GetTickCount64();
	
	PK_C_REQ_CHATTING* packet = (PK_C_REQ_CHATTING*)rowPacket;

	User* user = UserManager::getInstance().at(session->id());
	if (user == nullptr) {
		SLog(L"! not registed : %s", session->clientAddress().c_str());
		session->onClose();
		return;
	}

	// 클라이언트에서 서버까지의 네트워크 지연시간 계산
	// 타임스탬프 유효성 검사 추가
	UInt64 networkLatency = 0;
	if (packet->clientTimestamp_ > 0 && messageReceiveTime > packet->clientTimestamp_) {
		networkLatency = messageReceiveTime - packet->clientTimestamp_;
		// 비정상적으로 큰 값 체크 (10초 이상이면 오류로 간주)
		if (networkLatency > 10000) {
			SLog(L"! [CHAT_LATENCY] Invalid timestamp detected - ClientTime: %llu, ServerTime: %llu", 
				packet->clientTimestamp_, messageReceiveTime);
			networkLatency = 0; // 오류 시 0으로 설정
		}
	} else {
		SLog(L"! [CHAT_LATENCY] Invalid client timestamp: %llu (Server time: %llu)", 
			packet->clientTimestamp_, messageReceiveTime);
	}

	// 메시지 응답 전송 시간 기록
	UInt64 messageResponseTime = GetTickCount64();
	UInt64 processingTime = messageResponseTime - messageReceiveTime;

	PK_S_ANS_CHATTING retPacket;
	array<char, SIZE_64> name;
	StrConvW2A((WCHAR*)user->name().c_str(), name.data(), name.size());
	retPacket.name_ = name.data();
	retPacket.text_ = "-> : ";
	retPacket.text_ += packet->text_;
	retPacket.serverTimestamp_ = messageResponseTime; // 서버 응답 시간 추가

	// 지연시간 정보를 콘솔에 출력
	SLog(L"* [CHAT_LATENCY] User: [%S] | Network: %llums | Processing: %llums | Total: %llums", 
		retPacket.name_.c_str(), networkLatency, processingTime, networkLatency + processingTime);
	
	session->sendPacket(&retPacket);

	UserManager::getInstance().broadcast(&retPacket,session->id());
}

void ChattingProcess::C_REQ_CHAT_EXIT(Session* session, Packet* rowPacket)
{
	
	PK_C_REQ_CHAT_EXIT* packet = (PK_C_REQ_CHAT_EXIT*)rowPacket;
	SLog(L"chattingPro!!!test!!!");
	User* user = UserManager::getInstance().at(session->id());
	if (user == nullptr) {
		SLog(L"! not registed : %s", session->clientAddress().c_str());
		session->onClose();
		return;
	}

	PK_S_ANS_EXIT_USER exitPacket;
	array<char, SIZE_64> name;
	StrConvW2A((WCHAR*)user->name().c_str(), name.data(), name.size());
	exitPacket.name_ = name.data();
	SLog(L"exitUser!!!test!!! Name: %S", exitPacket.name_.c_str());
	UserManager::getInstance().broadcast(&exitPacket, session->id());
	UserManager::getInstance().remove(session->id());

	PK_S_ANS_EXIT ansPacket;
	SLog(L"* recv exit packet by [%s]", session->clientAddress().c_str());
	session->sendPacket(&ansPacket);
}

void ChattingProcess::C_REQ_PING(Session* session, Packet* rowPacket)
{
	PK_C_REQ_PING* packet = (PK_C_REQ_PING*)rowPacket;
	
	// Get current server timestamp
	UInt64 serverTimestamp = GetTickCount64();
	
	// Calculate latency (server time - client time)
	UInt64 latency = serverTimestamp - packet->clientTimestamp_;
	
	// Get current user count for additional info
	auto& userManager = UserManager::getInstance();
	std::vector<pair<oid_t, User*>> users = userManager.getAllUsers();
	int userCount = users.size();
	
	// Log the ping information with user count
	SLog(L"[CHAT_PING] Session %llu - Seq: %u, Latency: %llu ms, Users: %d", 
		(UInt64)session->id(), packet->sequenceNumber_, latency, userCount);
	
	// Send pong response
	PK_S_ANS_PONG pongPacket;
	pongPacket.clientTimestamp_ = packet->clientTimestamp_;
	pongPacket.serverTimestamp_ = serverTimestamp;
	pongPacket.sequenceNumber_ = packet->sequenceNumber_;
	
	session->sendPacket(&pongPacket);
}



