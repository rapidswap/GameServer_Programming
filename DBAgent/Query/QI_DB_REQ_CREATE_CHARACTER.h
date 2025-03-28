#pragma once
#include "stdafx.h"

class QI_DB_REQ_CREATE_CHARACTER : public Query
{
public:
	oid_t clientId_;

	WCHAR* procedure_1()
	{
		return L" p_AccountData_Insert";
	}

	WCHAR* procedure_2()
	{
		return L"p_Character_Insert";
	}

	QI_DB_REQ_CREATE_CHARACTER() {
		statement_->setQuery(this->procedure_1(), QUERY_CALL_BACK);
		statement_->setQuery(this->procedure_2(), QUERY_CALL_BACK);
	}

	~QI_DB_REQ_CREATE_CHARACTER() {
		PK_I_DB_ANS_CREATE_CHARACTER iPacket;
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
				SLog(L"* this query [%s] have error", this->procedure_1());
				SLog(L"* this query [%s] have error", this->procedure_2());
				break;
			}
			record_.moveNext();
		}

		Terminal* terminal = _terminal.get(L"LoginServer");
		terminal->sendPacket(&iPacket);
	}
};