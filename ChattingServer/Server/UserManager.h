#pragma once
#include "stdafx.h"
#include <algorithm>
class User;
class Session;

class UserManager :public Singleton<UserManager>
{
	unordered_map<oid_t, User*> userPool_;

public:
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
				userPair.second->session()->sendPacket(packet);
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
		userPool_.erase(id);
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