#pragma once
#include "stdafx.h"

class QI_DB_USER_ID_PW : public Query
{
public:
	oid_t clientId_;

	WCHAR* procedure()
	{
		return L"p_AccountData_Select";
	}

	QI_DB_USER_ID_PW() {
		statement_->setQuery(this->procedure(), QUERY_CALL_BACK);
	}

	~QI_DB_USER_ID_PW() {
		PK_I_DB_ANS_USER_ID_PW iPacket;
		iPacket.clientId_ = (UInt64)clientId_;
		iPacket.result_ = FALSE;
		if (!record_.isEof()) {
			record_.moveFirst();
		}

		while (!record_.isEof()) {
			int oidAccount = 0;
			if (record_.get("oidAccount", oidAccount)) {
				iPacket.oidAccountId_ = oidAccount;
				iPacket.result_ = TRUE;
				break;
			}
			else {
				SLog(L"* this query [%s] have error", this->procedure());
				break;
			}
			record_.moveNext();
		}

		Terminal* terminal = _terminal.get(L"LoginServer");
		terminal->sendPacket(&iPacket);
	}
};