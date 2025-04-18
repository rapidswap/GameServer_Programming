#pragma once
#include "stdafx.h"

class QI_DB_REQ_CREATE_CHARACTER : public Query
{
public:
	oid_t clientId_;

	WCHAR* procedure()
	{
		return L"p_Character_Insert";
	}

	QI_DB_REQ_CREATE_CHARACTER() {
		statement_->setQuery(this->procedure(), QUERY_CALL_BACK);
	}

	~QI_DB_REQ_CREATE_CHARACTER() {
		PK_I_DB_ANS_CREATE_CHARACTER_SUCCESS iPacket;
		iPacket.clientId_ = (UInt64)clientId_;
		iPacket.result_ = FALSE;

		//if (!record_.isEof()) {
		//	record_.moveFirst();
		//	int oidAccount = 0;
		//	if (record_.get("oidAccount", oidAccount)) {
		//		iPacket.oidAccountId_ = oidAccount;
		//		iPacket.result_ = TRUE;
		//	}
		//	else {
		//		SLog(L"* Insert result [%s] parsing ����", this->procedure());
		//	}
		//}
		//else {
		//	SLog(L"* Insert ���� �Ǵ� ��� ���� [%s]", this->procedure());
		//}

		Terminal* terminal = _terminal.get(L"LoginServer");
		terminal->sendPacket(&iPacket);
	}
};