#include "stdafx.h"
#include "LoginProcess.h"

LoginProcess::LoginProcess()
{
	this->registSubPacketFunc();
}

void LoginProcess::registSubPacketFunc()
{
#define INSERT_PACKET_PROCESS(type)		runFuncTable_.insert(make_pair(E_##type, &LoginProcess::##type))

	INSERT_PACKET_PROCESS(C_REQ_ID_PW);
	INSERT_PACKET_PROCESS(C_REQ_CREATE_USER);
	INSERT_PACKET_PROCESS(I_DB_ANS_ID_PW);
	INSERT_PACKET_PROCESS(I_LOGIN_NOTIFY_ID_LOADED);
	INSERT_PACKET_PROCESS(C_REQ_CREATE_CHARACTER_ID_PW);
	INSERT_PACKET_PROCESS(I_DB_ANS_CREATE_CHARACTER);
	INSERT_PACKET_PROCESS(I_DB_ANS_CREATE_USER);
	INSERT_PACKET_PROCESS(I_DB_ANS_CREATE_CHARACTER_SUCCESS);
	INSERT_PACKET_PROCESS(C_REQ_PING);
}


void LoginProcess::C_REQ_ID_PW(Session *session, Packet *rowPacket)
{
	PK_C_REQ_ID_PW *packet = (PK_C_REQ_ID_PW *)rowPacket;

	PK_I_DB_REQ_ID_PW dbPacket;
	dbPacket.clientId_ = (UInt64)session->id();
	dbPacket.id_ = packet->id_;
	dbPacket.password_ = packet->password_;

	Terminal *terminal = _terminal.get(L"DBAgent");
	terminal->sendPacket(&dbPacket);
}

void LoginProcess::C_REQ_CREATE_USER(Session* session, Packet* rowPacket)
{
	PK_C_REQ_CREATE_USER* packet = (PK_C_REQ_CREATE_USER*)rowPacket;

	PK_I_DB_REQ_CREATE_USER dbPacket;
	dbPacket.clientId_ = (UInt64)session->id();
	dbPacket.id_ = packet->id_;
	dbPacket.password_ = packet->password_;
	Terminal* terminal = _terminal.get(L"DBAgent");
	terminal->sendPacket(&dbPacket);

	//dbPacket.oidAccountId_ = packet->oidAccountId_;
	//dbPacket.level_ = packet->level_;
	//dbPacket.exp_ = packet->exp_;
	//dbPacket.name_ = packet->name_;
}

void LoginProcess::I_DB_ANS_CREATE_USER(Session* session, Packet* rowPacket)
{
	PK_I_DB_ANS_CREATE_USER* packet = (PK_I_DB_ANS_CREATE_USER*)rowPacket;
	SLog(L"* id/ pw result = %d", packet->result_);

	Session* clientSession = _session_manager.session(packet->clientId_);
	if (clientSession == nullptr) {
		return;
	}

	const int authFail = 0;
	if (packet->result_ == authFail) {
		PK_S_ANS_CREATE_FAIL ansPacket;
		clientSession->sendPacket(&ansPacket);
		return;
	}
	clientSession->sendPacket(packet);
}

void LoginProcess::C_REQ_CREATE_CHARACTER_ID_PW(Session* session, Packet* rowPacket)
{
	PK_C_REQ_CREATE_CHARACTER_ID_PW* packet = (PK_C_REQ_CREATE_CHARACTER_ID_PW*)rowPacket;

	PK_I_DB_REQ_CREATE_CHARACTER_ID_PW dbPacket;
	dbPacket.clientId_ = (UInt64)session->id();
	dbPacket.id_ = packet->id_;
	dbPacket.password_ = packet->password_;
	dbPacket.name_ = packet->name_;
	Terminal* terminal = _terminal.get(L"DBAgent");
	terminal->sendPacket(&dbPacket);
}

void LoginProcess::I_DB_ANS_CREATE_CHARACTER(Session* session, Packet* rowPacket)
{
	PK_I_DB_ANS_CREATE_CHARACTER* packet = (PK_I_DB_ANS_CREATE_CHARACTER*)rowPacket;
	//PK_S_ANS_CREATE_CHARACTER_SUCCESS ansPacket;

	PK_I_DB_REQ_CREATE_CHARACTER dbPacket;
	//Session* clientSession = _session_manager.session(packet->clientId_);

	dbPacket.clientId_ = (UInt64)packet->clientId_;
	dbPacket.oidAccountId_ = packet->oidAccountId_;
	dbPacket.name_ = packet->name_;

	Terminal* terminal = _terminal.get(L"DBAgent");
	terminal->sendPacket(&dbPacket);
	//clientSession->sendPacket(&ansPacket);
}

void LoginProcess::I_DB_ANS_CREATE_CHARACTER_SUCCESS(Session* session, Packet* rowPacket)
{
	PK_I_DB_ANS_CREATE_CHARACTER_SUCCESS* packet = (PK_I_DB_ANS_CREATE_CHARACTER_SUCCESS*)rowPacket;
	PK_S_ANS_CREATE_CHARACTER_SUCCESS dbPacket;
	SLog(L"* id/ pw result = %d", packet->result_);

	Session* clientSession = _session_manager.session(packet->clientId_);
	if (clientSession == nullptr) {
		return;
	}
	const int authFail = 0;
	if (packet->result_ == authFail) {
		PK_S_ANS_CREATE_FAIL ansPacket;
		clientSession->sendPacket(&ansPacket);
		return;
	}
	clientSession->sendPacket(&dbPacket);
}

void LoginProcess::I_DB_ANS_ID_PW(Session *session, Packet *rowPacket)
{
	PK_I_DB_ANS_ID_PW *packet = (PK_I_DB_ANS_ID_PW  *)rowPacket;
	SLog(L"* id/ pw result = %d", packet->result_);

	Session *clientSession = _session_manager.session(packet->clientId_);
	if (clientSession == nullptr) {
		return;
	}

	const int authFail = 0;
	if (packet->result_ == authFail) {
		PK_S_ANS_ID_PW_FAIL ansPacket;
		clientSession->sendPacket(&ansPacket);
		return;
	}
	
	PK_I_CHTTING_NOTIFY_ID iPacket;
	iPacket.oidAccountId_ = packet->oidAccountId_;
	iPacket.clientId_ = packet->clientId_;
	Terminal *terminal = _terminal.get(L"ChattingServer");
	if (terminal == nullptr) {
		SLog(L"! Chatting Server terminal is not connected");
	}
	terminal->sendPacket(&iPacket);
}

void LoginProcess::I_LOGIN_NOTIFY_ID_LOADED(Session *session, Packet *rowPacket)
{
	PK_I_LOGIN_NOTIFY_ID_LOADED *packet = (PK_I_LOGIN_NOTIFY_ID_LOADED *)rowPacket;
	
	const int dataNull = 0;
	if (packet->result_ == dataNull) {
		return;
	}
	Session *clientSession = _session_manager.session(packet->clientId_);
	if (clientSession == nullptr) {
		return;
	}
	Terminal *terminal = _terminal.get(L"ChattingServer");
	if (terminal == nullptr) {
		SLog(L"! Chatting Server terminal is not connected");
	}
	PK_S_ANS_ID_PW_SUCCESS ansPacket;
	ansPacket.ip_ = terminal->ip();
	ansPacket.port_ = terminal->port();
	ansPacket.name_ = packet->name_;

	SLog(L"* loaded [%S] user name, from [%s]", ansPacket.name_.c_str(), session->clientAddress().c_str());
	clientSession->sendPacket(&ansPacket);
}

void LoginProcess::C_REQ_PING(Session *session, Packet *rowPacket)
{
	PK_C_REQ_PING *packet = (PK_C_REQ_PING *)rowPacket;
	
	// Get current server timestamp
	UInt64 serverTimestamp = GetTickCount64();
	
	// Calculate latency (server time - client time)
	UInt64 latency = serverTimestamp - packet->clientTimestamp_;
	
	// Log the ping information
	SLog(L"[LOGIN_PING] Session %llu - Seq: %u, Latency: %llu ms", 
		(UInt64)session->id(), packet->sequenceNumber_, latency);
	
	// Send pong response
	PK_S_ANS_PONG pongPacket;
	pongPacket.clientTimestamp_ = packet->clientTimestamp_;
	pongPacket.serverTimestamp_ = serverTimestamp;
	pongPacket.sequenceNumber_ = packet->sequenceNumber_;
	
	session->sendPacket(&pongPacket);
}