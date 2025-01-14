#pragma once
#include "pch.h"
#include "SessionManager.h"

typedef enum SERVER_STATUS {
	SERVER_STOP,
	SERVER_INITALZE,
	SERVER_READY,
};

class Server
{
protected:
	char ip_[16];
	int port_;
	int workerThreadCount_;

	SERVER_STATUS status_;
	ContentsProcess* contentsProcess_;
public:
	Server(contentsProcess_* contentsProcess);
	virtual ~Server();

	virtual void initialize(xml_t* config);

	virtual bool run() = 0;
	SERVER_STATUS& status();

	void putPackage(Package* pacakage);
};