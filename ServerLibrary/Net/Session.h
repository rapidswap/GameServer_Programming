#pragma once
#include "pch.h"

struct SOCKET_DATA {
	SOCKET socket_;
	SOCKADDR_IN addrInfo_;
};

enum {
	SESSION_TYPE_TERMINAL,
	SESSION_TYPE_CLIENT,
};

class Session
{
protected:
	SOCKET_DATA socketData_;
	oid_t id_;
	int8_t type_;
	bool setSocketOpt();
	tick_t lastHeartBeat_;

public:
	Session();
	virtual ~Session();

	virtual bool onAccept(SOCKET socket, SOCKADDR_IN addrInfo);

	virtual void onSend(size_t transferSize) = 0;
	virtual void sendPacket(Packet* packet) = 0;

	virtual Package* pmRecv(size_t transferSize) = 0;
	virtual void recvStandBy() {};

	virtual void onClose(bool force = false);

	SOCKET& socket();
	str_t clientAddress();

	oid_t id();
	void setId(oid_t id);

	int8_t type();
	void setType(int8_t tpye);

	tick_t heartBeat();
	void updateHeartBeat();
};