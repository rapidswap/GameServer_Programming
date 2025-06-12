#pragma once
#include "stdafx.h"
#include <algorithm>
class User;
class Session;

class UserManager :public Singleton<UserManager>
{
	unordered_map<oid_t, User*> userPool_;
	// 락 제거 - 단순한 데이터 보호만 하도록 변경

public:
	UserManager() {}

	void insert(User* user)
	{
		oid_t key = user->session()->id();
		userPool_.insert(make_pair(key, user));
	}

	template<typename T>
	void broadcast(T* packet, oid_t senderId)
	{
		for (const auto& userPair : userPool_)
		{
			if (userPair.first == senderId) {
				continue;
			}

			if (userPair.second && userPair.second->session()) {
				try {
					userPair.second->session()->sendPacket(packet);
				} catch (...) {
					// 전송 실패 시 무시하고 계속
				}
			}
		}
	}

	vector<pair<oid_t, User*>> getAllUsers()
	{
		vector<pair<oid_t, User*>> users;
		for (const auto& pair : userPool_) {
			users.push_back(pair);
		}
		return users;
	}

	void remove(oid_t id)
	{
		auto itr = userPool_.find(id);
		if (itr != userPool_.end()) {
			User* user = itr->second;
			userPool_.erase(itr);
			SAFE_DELETE(user);  // 메모리 누수 수정 유지
		}
	}

	User* at(oid_t id)
	{
		auto itr = userPool_.find(id);
		if (itr == userPool_.end()) {
			return nullptr;
		}
		return itr->second;
	}

	size_t size()
	{
		return userPool_.size();
	}
};