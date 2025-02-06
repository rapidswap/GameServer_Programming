#pragma once
#include "stdafx.h"
#include "dbghelp.h"

//dump �Լ� ������
typedef BOOL(WINAPI *WRITEDUMP)(
    _In_  HANDLE hProcess,
    _In_  DWORD ProcessId,
    _In_  HANDLE hFile,
    _In_  MINIDUMP_TYPE DumpType,
    _In_  PMINIDUMP_EXCEPTION_INFORMATION ExceptionParam,
    _In_  PMINIDUMP_USER_STREAM_INFORMATION UserStreamParam,
    _In_  PMINIDUMP_CALLBACK_INFORMATION CallbackParam
    );

class MiniDump : public Singleton<MiniDump>
{
public:
	MiniDump();

	static LONG WINAPI execptionFilter(struct _EXCEPTION_POINTERS *exceptionInfo);
};
