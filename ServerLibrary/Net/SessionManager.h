#pragma once
#include "stdafx.h"
#include "Session.h"



#define SESSION_CAPACITY		(5000)
#define _session_manager		SessionManager::getInstance()

class SessionManager : public Singleton<SessionManager>
{
    typedef list<Session*>		SessionList;

    SessionList		            sessionList_;
	int									sessionCount_ = 0;  // 초기화 추가
	int									maxConnection_;
    Lock								lock_;

	oid_t								sessionSeed_;			

	// ���� ���� ���ɾ�
    typedef std::function<void (SessionList *sessionList, wstr_t *arg)> cmdFunc;
	unordered_map<wstr_t, cmdFunc>   serverCommand_;

public:
	SessionManager(int maxConnection = SESSION_CAPACITY);
	~SessionManager();
	oid_t				createSessionId();

	bool				addSession(Session *session);

	list<Session*>		&sessionList();
	bool				closeSession(Session *session);
	void				forceCloseSession(Session *session);

	Session				*session(oid_t id);

    void                runCommand(wstr_t cmd);
    void                commandFuncInitialize();
};