#pragma once
#include "stdafx.h"

#pragma comment(lib, "ws2_32.lib")
#pragma comment(lib, "mswsock.lib")
#pragma comment(lib, "Winmm.lib")

#include <Ws2tcpip.h>
#include <winsock2.h>
#include <mswsock.h>
#include <Mmsystem.h>
#include <Ws2spi.h>
#include <Mstcpip.h>

#include <windows.h>
#include <iostream>
#include <io.h>
#include <cstdlib>
#include <stdio.h>
#include <cstdint>

#include <assert.h> 
#include <fcntl.h>
#include <algorithm>  
#include <functional>

#include <thread>
#include <mutex>
#include <memory>

#include <string>
#include <tchar.h>

#include <ctime>
#include <random>
#include <typeinfo>    //typeinfo
// TODO: ���� ��ũ��

#if _DEBUG
#define CONTEXT_SWITCH		Sleep(1)
#else
#define CONTEXT_SWITCH		::SwitchToThread()
#endif

typedef void(*Function)(void *);

//��Ÿ ��ƿ
#include "./Util/csv_parser/csv_parser.hpp"
#include "./Util/tinyXml/tinyxml.h"

// TODO: �ʼ� ��� ����
//-------------------------------------------------------------------//
#include "./Net/WinSocket.h"
#include "./Util/Type.h"
#include "./Util/Util.h"

#include "./Util/GameObject.h"
#include "./Util/Singleton.h"

#include "./Util/Clock.h"
#include "./Util/Logger.h"
#include "./Util/Assert.h"

#include "./Util/Table.h"
#include "./Util/Thread.h"
#include "./Util/Lock.h"
#include "./Util/ThreadJobQueue.h"
#include "./Util/Task.h"

#include "./Util/MemoryLeak.h"
#include "./Util/Memory_LowFragmentationHeap.h"
#include "./Util/Minidump.h"

#include "./Util/Config.h"
#include "./Util/Monitoring.h"
#include "./util/ProgramValidation.h"

//��Ŷ��
#include "./Net/Packet/Stream.h"
#include "./Net/Packet/PacketHeader.h"
#include "./Net/Packet/PacketClass.h"
#include "./Net/Packet/PacketAnalyzer.h"
#include "./Net/Packet/PacketFactory.h"
#include "./Net/Packet/Package.h"
#include "./Net/Packet/PacketObfuscation.h"

//������ ����
#include "./Contents/ContentsProcess.h"

//����
#include "./Net/Session.h"
#include "./Net/SessionManager.h"
#include "./Net/Server.h"

#include "./Net/Iocp/IOCPServer.h"
#include "./Net/Iocp/IOCPSession.h"
#include "./Net/SessionMonitor.h"

//�͹̳�
#include "./Net/Terminal/TerminalSession.h"
#include "./Net/Terminal/Terminal.h"
#include "./Net/Terminal/TerminalManager.h"

//DB
#include "./Database/ADODatabase.h"
#include "./Database/Query.h"
#include "./Database/DBManager.h"

// ���� ����
#include "Shutdown.h"
