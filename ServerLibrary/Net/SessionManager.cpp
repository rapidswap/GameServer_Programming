#include "stdafx.h"
#include "SessionManager.h"
#include "./Iocp/IOCPServer.h"

SessionManager::SessionManager(int maxConnection)
	: lock_(L"SessionManager")
{
	sessionSeed_ = 1;
	sessionCount_ = 0;
	// Singleton 패턴에서는 기본 생성자가 호출되므로 항상 기본값 사용
	maxConnection_ = SESSION_CAPACITY;  // 5000
	SLog(L"* SessionManager initialized with capacity: %d", maxConnection_);
	this->commandFuncInitialize();
}

SessionManager::~SessionManager()
{
	vector<Session *> removeSessionVec;
	removeSessionVec.resize(sessionList_.size());
	std::copy(sessionList_.begin(), sessionList_.end(), removeSessionVec.begin());
	for (auto session : removeSessionVec) {
		session->onClose();
	}
	sessionList_.clear();
}

list<Session*>& SessionManager::sessionList()
{
	return sessionList_;
}

oid_t SessionManager::createSessionId()
{
	return sessionSeed_++;
}

bool SessionManager::addSession(Session *session)
{
	SAFE_LOCK(lock_);
	auto findSession = std::find(sessionList_.begin(), sessionList_.end(), session);
	if (findSession != sessionList_.end()) {
		return false;
	}
	
	// 현재 세션 수 정확히 계산
	int currentSessionCount = static_cast<int>(sessionList_.size());
	if (currentSessionCount >= maxConnection_) {
		SLog(L"* session limit reached. current[%d], max[%d]", currentSessionCount, maxConnection_);
		return false;
	}

	session->setId(this->createSessionId());
	sessionList_.push_back(session);
	sessionCount_ = currentSessionCount + 1;  // 정확한 카운트
	return true;
}


bool SessionManager::closeSession(Session *session)
{
	SAFE_LOCK(lock_);
	if (session == nullptr) {
		return false;
	}
	auto findSession = std::find(sessionList_.begin(), sessionList_.end(), session);
	if (findSession != sessionList_.end()) {
		Session *delSession = *findSession;
		SLog(L"* detected close by client [%s]", delSession->clientAddress().c_str());
		
		try {
			::closesocket(delSession->socket());
		} catch (...) {
			// 소켓 닫기 실패 시 무시
		}

		sessionList_.remove(delSession);
		sessionCount_ = static_cast<int>(sessionList_.size());  // 정확한 카운트
		SAFE_DELETE(delSession);
		return true;
	}
	return false;
}


void SessionManager::forceCloseSession(Session *session)
{
	SAFE_LOCK(lock_);
	if (!session) {
		return;
	}

	//����� ���� ����. 
	LINGER linger;
	linger.l_onoff = 1;   //���
	linger.l_linger = 0;  //���ð�, 0�Ͻ� �Ϸ� �ȵ� ��Ŷ ������ ��� ����.

	::setsockopt(session->socket(), SOL_SOCKET, SO_LINGER, (char *)&linger, sizeof(linger));
	this->closeSession(session);
}

Session* SessionManager::session(oid_t id)
{
	SAFE_LOCK(lock_);
	Session *findSession = nullptr;

	for (auto session : sessionList_) {
		if (session->id() == id) {
			findSession = session;
			break;
		}
	}
	
	return findSession;
}

void SessionManager::runCommand(wstr_t cmdLine)
{
	std::size_t found = cmdLine.find(L' ');
	wstr_t command;
	wstr_t arg;
	if (found != wstr_t::npos) {
		command = cmdLine.substr(0, found);
		arg = cmdLine.substr(found);
	}
	else {
		command = cmdLine;
	}

	auto itr = serverCommand_.find(command);
	if (itr == serverCommand_.end()) {
		return;
	}

	auto cmdFunc = serverCommand_.at(command);
	if (cmdFunc) {
		cmdFunc(&sessionList_, &arg);
	}
}

// ġƮŰ
void SessionManager::commandFuncInitialize()
{
#if 0

    auto notiyFunc = [](SessionList *sessionList, wstr_t *arg) {
        auto eachFunc = [arg](void *atom) {
            Session *session = (Session*)atom;
			if (session->type() == SESSION_TYPE_TERMINAL) {
				return;
			}
            array<CHAR, SIZE_256> tmpBuf;
            StrConvW2A((WCHAR*)arg->c_str(), tmpBuf.data(), tmpBuf.size());

			PK_S_ANS_CHATTING retPacket;
			retPacket.id_ = "Server";
			retPacket.text_ = "* Notity : ";
			retPacket.text_ += tmpBuf.data();

			session->sendPacket(&retPacket);
        };

		for (auto session : *sessionList) {
			eachFunc(session);
		}
    };

    auto kickoffFunc = [](SessionList *sessionList, wstr_t *arg){
        vector<Session *> removeSessionVec;
        auto eachFunc = [&removeSessionVec, arg](void *atom) {
            Session *session = (Session*)atom;
			if (session->type() == SESSION_TYPE_TERMINAL) {
				return;
			}

			PK_S_ANS_CHATTING retPacket;
			retPacket.id_ = "Server";
			retPacket.text_ = "! Kick off by Server";
			session->sendPacket(&retPacket);

            removeSessionVec.push_back(session);
        }; 
		for (auto session : *sessionList) {
			eachFunc(session);
		}

        for (auto session : removeSessionVec) {
			session->onClose();
        }
    };

    auto exitFunc = [](SessionList *sessionList, wstr_t *arg){
        _shutdown = true;
    };

    //���ɾ� ���
    serverCommand_.insert(make_pair(L"/notify", notiyFunc));
	serverCommand_.insert(make_pair(L"/kickoff", kickoffFunc));
	serverCommand_.insert(make_pair(L"/exit", exitFunc));
#endif
}