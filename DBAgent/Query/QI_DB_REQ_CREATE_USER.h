#pragma once
#include "stdafx.h"

class QI_DB_REQ_CREATE_USER : public Query
{
public:
	oid_t clientId_;

	WCHAR* procedure()
	{
		return L"p_AccountData_Insert";
	}


	QI_DB_REQ_CREATE_USER() {
		statement_->setQuery(this->procedure(), QUERY_CALL_BACK);
	}

	~QI_DB_REQ_CREATE_USER() {
		PK_I_DB_ANS_CREATE_USER iPacket;
		iPacket.clientId_ = (UInt64)clientId_;
		iPacket.result_ = FALSE;

		int testVal = this->result().resultVal();

		if (this->result().resultVal() > 0) {
			iPacket.result_ = TRUE; 
		}
		else {
			iPacket.result_ = FALSE; 
			SLog(L"* Account creation failed for client %llu. DB result value: %d", clientId_, this->result().resultVal());

		}


		Terminal* terminal = _terminal.get(L"LoginServer");
		terminal->sendPacket(&iPacket);
	}
};