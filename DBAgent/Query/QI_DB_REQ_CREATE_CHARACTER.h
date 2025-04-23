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

		if (this->result().resultVal() > 0) {
			iPacket.result_ = TRUE; 
		}
		else {
			iPacket.result_ = FALSE; 
			SLog(L"* Character creation failed for client %llu. DB result value: %d", clientId_, this->result().resultVal());

		}

		Terminal* terminal = _terminal.get(L"LoginServer");
		terminal->sendPacket(&iPacket);
	}
};