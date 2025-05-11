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
		if (!record_.isEof()) {
			iPacket.result_ = TRUE;
		}
		


		Terminal* terminal = _terminal.get(L"LoginServer");
		terminal->sendPacket(&iPacket);
	}
};