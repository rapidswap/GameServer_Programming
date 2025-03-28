#pragma once
#include "stdafx.h"
#include "DBAgentProcess.h"

DBAgentProcess::DBAgentProcess()
{
	this->registSubPacketFunc();
}

void DBAgentProcess::registSubPacketFunc()
{
#define INSERT_PACKET_PROCESS(type)		runFuncTable_.insert(make_pair(E_##type, &DBAgentProcess::##type))

	INSERT_PACKET_PROCESS(I_DB_REQ_ID_PW);
	INSERT_PACKET_PROCESS(I_DB_REQ_LOAD_DATA);
	INSERT_PACKET_PROCESS(I_DB_REQ_CHARACTER);
}

void DBAgentProcess::I_DB_REQ_ID_PW(Session *session, Packet *rowPacket)
{
	PK_I_DB_REQ_ID_PW *packet = (PK_I_DB_REQ_ID_PW *)rowPacket;

	QI_DB_REQ_ID_PW *query = new QI_DB_REQ_ID_PW();	        			
	query->clientId_ = packet->clientId_;

	QueryStatement *statement = query->statement();
	statement->addParam((char *)packet->id_.c_str());					
	statement->addParam((char *)packet->password_.c_str());
	
	DBManager::getInstance().pushQuery(query);
}
void DBAgentProcess::I_DB_REQ_CHARACTER(Session* session, Packet* rowPacket)
{
	PK_I_DB_REQ_CHARACTER* packet = (PK_I_DB_REQ_CHARACTER*)rowPacket;

	QI_DB_REQ_CREATE_CHARACTER* query = new QI_DB_REQ_CREATE_CHARACTER();
	query->clientId_ = packet->clientId_;

	QueryStatement* statement = query->statement();
	statement->addParam((char*)packet->id_.c_str());
	statement->addParam((char*)packet->password_.c_str());
	statement->addParam((char*)packet->name_.c_str());
}

void DBAgentProcess::I_DB_REQ_LOAD_DATA(Session *session, Packet *rowPacket)
{
	PK_I_DB_REQ_LOAD_DATA *packet = (PK_I_DB_REQ_LOAD_DATA *)rowPacket;

	QI_DB_REQ_LOAD_DATA *query = new QI_DB_REQ_LOAD_DATA();
	query->clientId_ = packet->clientId_;

	QueryStatement *statement = query->statement();
	statement->addParam(packet->oidAccountId_);

	DBManager::getInstance().pushQuery(query);
}