#  Project Contents
## ChattingServer\ChattingServer.vcxproj
```vcxproj
<?xml version="1.0" encoding="utf-8"?>
<Project DefaultTargets="Build" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <ItemGroup Label="ProjectConfigurations">
    <ProjectConfiguration Include="Debug|Win32">
      <Configuration>Debug</Configuration>
      <Platform>Win32</Platform>
    </ProjectConfiguration>
    <ProjectConfiguration Include="Release|Win32">
      <Configuration>Release</Configuration>
      <Platform>Win32</Platform>
    </ProjectConfiguration>
    <ProjectConfiguration Include="Debug|x64">
      <Configuration>Debug</Configuration>
      <Platform>x64</Platform>
    </ProjectConfiguration>
    <ProjectConfiguration Include="Release|x64">
      <Configuration>Release</Configuration>
      <Platform>x64</Platform>
    </ProjectConfiguration>
  </ItemGroup>
  <PropertyGroup Label="Globals">
    <VCProjectVersion>17.0</VCProjectVersion>
    <Keyword>Win32Proj</Keyword>
    <ProjectGuid>{d9687045-9147-4b36-816e-71c68e01c7eb}</ProjectGuid>
    <RootNamespace>ChattingServer</RootNamespace>
    <WindowsTargetPlatformVersion>10.0</WindowsTargetPlatformVersion>
  </PropertyGroup>
  <Import Project="$(VCTargetsPath)\Microsoft.Cpp.Default.props" />
  <PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Debug|Win32'" Label="Configuration">
    <ConfigurationType>Application</ConfigurationType>
    <UseDebugLibraries>true</UseDebugLibraries>
    <PlatformToolset>v143</PlatformToolset>
    <CharacterSet>Unicode</CharacterSet>
  </PropertyGroup>
  <PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Release|Win32'" Label="Configuration">
    <ConfigurationType>Application</ConfigurationType>
    <UseDebugLibraries>false</UseDebugLibraries>
    <PlatformToolset>v143</PlatformToolset>
    <WholeProgramOptimization>true</WholeProgramOptimization>
    <CharacterSet>Unicode</CharacterSet>
  </PropertyGroup>
  <PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Debug|x64'" Label="Configuration">
    <ConfigurationType>Application</ConfigurationType>
    <UseDebugLibraries>true</UseDebugLibraries>
    <PlatformToolset>v143</PlatformToolset>
    <CharacterSet>Unicode</CharacterSet>
  </PropertyGroup>
  <PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Release|x64'" Label="Configuration">
    <ConfigurationType>Application</ConfigurationType>
    <UseDebugLibraries>false</UseDebugLibraries>
    <PlatformToolset>v143</PlatformToolset>
    <WholeProgramOptimization>true</WholeProgramOptimization>
    <CharacterSet>Unicode</CharacterSet>
  </PropertyGroup>
  <Import Project="$(VCTargetsPath)\Microsoft.Cpp.props" />
  <ImportGroup Label="ExtensionSettings">
  </ImportGroup>
  <ImportGroup Label="Shared">
  </ImportGroup>
  <ImportGroup Label="PropertySheets" Condition="'$(Configuration)|$(Platform)'=='Debug|Win32'">
    <Import Project="$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props" Condition="exists('$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props')" Label="LocalAppDataPlatform" />
  </ImportGroup>
  <ImportGroup Label="PropertySheets" Condition="'$(Configuration)|$(Platform)'=='Release|Win32'">
    <Import Project="$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props" Condition="exists('$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props')" Label="LocalAppDataPlatform" />
  </ImportGroup>
  <ImportGroup Label="PropertySheets" Condition="'$(Configuration)|$(Platform)'=='Debug|x64'">
    <Import Project="$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props" Condition="exists('$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props')" Label="LocalAppDataPlatform" />
  </ImportGroup>
  <ImportGroup Label="PropertySheets" Condition="'$(Configuration)|$(Platform)'=='Release|x64'">
    <Import Project="$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props" Condition="exists('$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props')" Label="LocalAppDataPlatform" />
  </ImportGroup>
  <PropertyGroup Label="UserMacros" />
  <PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Debug|x64'">
    <IncludePath>$(SolutuinDir)\ServerLibrary;$(VC_IncludePath);$(WindowsSDK_IncludePath);$(ProjectDir);$(SolutionDir)\ServerLibrary;C:\github\GameServer_Programming\ServerLibrary;</IncludePath>
  </PropertyGroup>
  <ItemDefinitionGroup Condition="'$(Configuration)|$(Platform)'=='Debug|Win32'">
    <ClCompile>
      <WarningLevel>Level3</WarningLevel>
      <SDLCheck>true</SDLCheck>
      <PreprocessorDefinitions>WIN32;_DEBUG;_CONSOLE;%(PreprocessorDefinitions)</PreprocessorDefinitions>
      <ConformanceMode>true</ConformanceMode>
    </ClCompile>
    <Link>
      <SubSystem>Console</SubSystem>
      <GenerateDebugInformation>true</GenerateDebugInformation>
    </Link>
  </ItemDefinitionGroup>
  <ItemDefinitionGroup Condition="'$(Configuration)|$(Platform)'=='Release|Win32'">
    <ClCompile>
      <WarningLevel>Level3</WarningLevel>
      <FunctionLevelLinking>true</FunctionLevelLinking>
      <IntrinsicFunctions>true</IntrinsicFunctions>
      <SDLCheck>true</SDLCheck>
      <PreprocessorDefinitions>WIN32;NDEBUG;_CONSOLE;%(PreprocessorDefinitions)</PreprocessorDefinitions>
      <ConformanceMode>true</ConformanceMode>
    </ClCompile>
    <Link>
      <SubSystem>Console</SubSystem>
      <EnableCOMDATFolding>true</EnableCOMDATFolding>
      <OptimizeReferences>true</OptimizeReferences>
      <GenerateDebugInformation>true</GenerateDebugInformation>
    </Link>
  </ItemDefinitionGroup>
  <ItemDefinitionGroup Condition="'$(Configuration)|$(Platform)'=='Debug|x64'">
    <ClCompile>
      <WarningLevel>Level3</WarningLevel>
      <SDLCheck>true</SDLCheck>
      <PreprocessorDefinitions>_DEBUG;_CONSOLE;%(PreprocessorDefinitions)</PreprocessorDefinitions>
      <ConformanceMode>false</ConformanceMode>
      <PrecompiledHeader>Use</PrecompiledHeader>
      <RuntimeLibrary>MultiThreadedDebug</RuntimeLibrary>
    </ClCompile>
    <Link>
      <SubSystem>Console</SubSystem>
      <GenerateDebugInformation>true</GenerateDebugInformation>
    </Link>
  </ItemDefinitionGroup>
  <ItemDefinitionGroup Condition="'$(Configuration)|$(Platform)'=='Release|x64'">
    <ClCompile>
      <WarningLevel>Level3</WarningLevel>
      <FunctionLevelLinking>true</FunctionLevelLinking>
      <IntrinsicFunctions>true</IntrinsicFunctions>
      <SDLCheck>true</SDLCheck>
      <PreprocessorDefinitions>NDEBUG;_CONSOLE;%(PreprocessorDefinitions)</PreprocessorDefinitions>
      <ConformanceMode>true</ConformanceMode>
    </ClCompile>
    <Link>
      <SubSystem>Console</SubSystem>
      <EnableCOMDATFolding>true</EnableCOMDATFolding>
      <OptimizeReferences>true</OptimizeReferences>
      <GenerateDebugInformation>true</GenerateDebugInformation>
    </Link>
  </ItemDefinitionGroup>
  <ItemGroup>
    <ClCompile Include="ChattingServer.cpp" />
    <ClCompile Include="Server\ChattingProcess.cpp" />
    <ClCompile Include="stdafx.cpp">
      <PrecompiledHeader Condition="'$(Configuration)|$(Platform)'=='Debug|x64'">Create</PrecompiledHeader>
    </ClCompile>
    <ClInclude Include="targetver.h">
      <FileType>CppCode</FileType>
    </ClInclude>
  </ItemGroup>
  <ItemGroup>
    <ProjectReference Include="..\ServerLibrary\ServerLibrary.vcxproj">
      <Project>{6e110469-40cf-47f8-b4c3-df093d50164c}</Project>
    </ProjectReference>
  </ItemGroup>
  <ItemGroup>
    <ClInclude Include="Server\ChattingProcess.h" />
    <ClInclude Include="Server\User.h" />
    <ClInclude Include="Server\UserManager.h" />
    <ClInclude Include="stdafx.h" />
  </ItemGroup>
  <ItemGroup>
    <Xml Include="config.xml" />
  </ItemGroup>
  <Import Project="$(VCTargetsPath)\Microsoft.Cpp.targets" />
  <ImportGroup Label="ExtensionTargets">
  </ImportGroup>
</Project>
```

## ChattingServer\Server\ChattingProcess.cpp
```cpp
#include "stdafx.h"
#include "ChattingProcess.h"

ChattingProcess::ChattingProcess()
{
	this->registSubPacketFunc();
}

void ChattingProcess::registSubPacketFunc()
{
#define INSERT_PACKET_PROCESS(type)		runFuncTable_.insert(make_pair(E_##type, &ChattingProcess::##type))

	INSERT_PACKET_PROCESS(I_CHTTING_NOTIFY_ID);
	INSERT_PACKET_PROCESS(I_DB_ANS_PARSE_DATA);
	INSERT_PACKET_PROCESS(C_REQ_REGIST_CHATTING_NAME);
	INSERT_PACKET_PROCESS(C_REQ_CHATTING);
	INSERT_PACKET_PROCESS(C_REQ_CHAT_EXIT);
	
}

void ChattingProcess::I_CHTTING_NOTIFY_ID(Session* session, Packet* rowPacket)
{
	PK_I_CHTTING_NOTIFY_ID* packet = (PK_I_CHTTING_NOTIFY_ID*)rowPacket;

	PK_I_DB_REQ_LOAD_DATA dbPacket;
	dbPacket.clientId_ = packet->clientId_;
	dbPacket.oidAccountId_ = packet->oidAccountId_;

	Terminal* terminal = _terminal.get(L"DBAgent");
	terminal->sendPacket(&dbPacket);
}

void ChattingProcess::I_DB_ANS_PARSE_DATA(Session* session, Packet* rowPacket)
{
	PK_I_DB_ANS_PARSE_DATA* packet = (PK_I_DB_ANS_PARSE_DATA*)rowPacket;

	PK_I_LOGIN_NOTIFY_ID_LOADED iPacket;
	iPacket.clientId_ = packet->clientId_;
	iPacket.name_ = packet->name_;
	iPacket.result_ = packet->result_;

	SLog(L"* [%S] name load from db", iPacket.name_.c_str());
	Terminal* terminal = _terminal.get(L"LoginServer");
	terminal->sendPacket(&iPacket);
}

void ChattingProcess::C_REQ_REGIST_CHATTING_NAME(Session* session, Packet* rowPacket)
{
	PK_C_REQ_REGIST_CHATTING_NAME* packet = (PK_C_REQ_REGIST_CHATTING_NAME*)rowPacket;
	User* user = UserManager::getInstance().at(session->id());
	if (user != nullptr) {
		SLog(L"! try duplicate regist : %s, name : %S", session->clientAddress().c_str(), packet->name_.c_str());
		session->onClose();
		return;
	}
	user = new User(session);

	array<WCHAR, SIZE_64> userName;
	StrConvA2W((CHAR*)packet->name_.c_str(), userName.data(), userName.size());
	user->setName(userName.data());
	UserManager::getInstance().insert(user);

	SLog(L"* user [%s] created from [%S]", userName.data(), session->clientAddress().c_str());

	PK_S_ANS_NEW_USER_NOTIFY notifyPacket;
	notifyPacket.name_ = packet->name_;
	UserManager::getInstance().broadcast(&notifyPacket, session->id());

	PK_S_ANS_USER_LIST listPacket;
	auto& userManager = UserManager::getInstance();
	std::vector<pair<oid_t, User*>> users = userManager.getAllUsers();

	SLog(L"* Current user count: %d", users.size());

	for (const auto& userPair : users) {
		if (userPair.first != session->id()) {  // 자신 제외
			User* existingUser = userPair.second;
			if (existingUser) {
				array<char, SIZE_64> existingName;
				StrConvW2A((WCHAR*)existingUser->name().c_str(), existingName.data(), existingName.size());
				listPacket.names_.push_back(string(existingName.data()));

				SLog(L"* Added user to list: %S", existingName.data());
			}
		}
	}

	SLog(L"* Sending user list with %d users", listPacket.names_.size());
	session->sendPacket(&listPacket);
}

void ChattingProcess::C_REQ_CHATTING(Session* session, Packet* rowPacket)
{
	PK_C_REQ_CHATTING* packet = (PK_C_REQ_CHATTING*)rowPacket;

	User* user = UserManager::getInstance().at(session->id());
	if (user == nullptr) {
		SLog(L"! not registed : %s", session->clientAddress().c_str());
		session->onClose();
		return;
	}

	PK_S_ANS_CHATTING retPacket;
	array<char, SIZE_64> name;
	StrConvW2A((WCHAR*)user->name().c_str(), name.data(), name.size());
	retPacket.name_ = name.data();
	retPacket.text_ = "-> : ";
	retPacket.text_ += packet->text_;

	SLog(L"* send message %S, %S", retPacket.name_.c_str(), retPacket.text_.c_str());
	session->sendPacket(&retPacket);

	UserManager::getInstance().broadcast(&retPacket,session->id());
}

void ChattingProcess::C_REQ_CHAT_EXIT(Session* session, Packet* rowPacket)
{
	
	PK_C_REQ_CHAT_EXIT* packet = (PK_C_REQ_CHAT_EXIT*)rowPacket;
	SLog(L"chattingPro!!!test!!!");
	User* user = UserManager::getInstance().at(session->id());
	if (user == nullptr) {
		SLog(L"! not registed : %s", session->clientAddress().c_str());
		session->onClose();
		return;
	}

	PK_S_ANS_EXIT_USER exitPacket;
	array<char, SIZE_64> name;
	StrConvW2A((WCHAR*)user->name().c_str(), name.data(), name.size());
	exitPacket.name_ = name.data();
	SLog(L"exitUser!!!test!!! Name: %S", exitPacket.name_.c_str());
	UserManager::getInstance().broadcast(&exitPacket, session->id());
	UserManager::getInstance().remove(session->id());

	PK_S_ANS_EXIT ansPacket;
	SLog(L"* recv exit packet by [%s]", session->clientAddress().c_str());
	session->sendPacket(&ansPacket);
}
```

## ChattingServer\Server\ChattingProcess.h
```h
#pragma once
#include "stdafx.h"

class ChattingProcess : public ContentsProcess
{
public:
	ChattingProcess();
private:
	void registSubPacketFunc();

	static void I_CHTTING_NOTIFY_ID(Session* session, Packet* rowPacket);
	static void I_DB_ANS_PARSE_DATA(Session* session, Packet* rowPacket);
	static void C_REQ_REGIST_CHATTING_NAME(Session* session, Packet* rowPacket);
	static void C_REQ_CHATTING(Session* session, Packet* rowPacket);
	//static void C_REQ_EXIT(Session* session, Packet* rowPacket);
	static void C_REQ_CHAT_EXIT(Session* session, Packet* rowPacket);
};
```

## ChattingServer\Server\User.h
```h
#pragma once
#include "stdafx.h"

class User :public GameObject
{
	Session* session_;

public:
	User(Session* session)
	{
		session_ = session;
	}

	Session* session()
	{
		return session_;
	}

	void tick()
	{

	}
};
```

## ChattingServer\Server\UserManager.h
```h
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
```

## ChattingServer\stdafx.cpp
```cpp
// stdafx.cpp : source file that includes just the standard includes
// LoginServer.pch will be the pre-compiled header
// stdafx.obj will contain the pre-compiled type information

#include "stdafx.h"

// TODO: reference any additional headers you need in STDAFX.H
// and not in this file
```

## ChattingServer\stdafx.h
```h
// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently, but
// are changed infrequently
//

#pragma once

#include "targetver.h"

#include <stdio.h>
#include <tchar.h>

// TODO: reference additional headers your program requires here
#include "ServerLibrary.h"

#include "Server\User.h"
#include "Server\UserManager.h"
#include "Server\ChattingProcess.h"
```

## ChattingServer\targetver.h
```h
#pragma once

// Including SDKDDKVer.h defines the highest available Windows platform.

// If you wish to build your application for a previous Windows platform, include WinSDKVer.h and
// set the _WIN32_WINNT macro to the platform you wish to support before including SDKDDKVer.h.

#include <SDKDDKVer.h>
```

## ChattingServer\x64\Debug\ChattingServer.tlog\ChattingServer.lastbuildstate
```lastbuildstate
PlatformToolSet=v143:VCToolArchitecture=Native64Bit:VCToolsVersion=14.41.34120:TargetPlatformVersion=10.0.26100.0:
Debug|x64|C:\github\GameServer_Programming\ServerLibrary\|
```

## DBAgent\DBAgentProcess.cpp
```cpp
#pragma once
#include "stdafx.h"
#include "DBAgentProcess.h"

DBAgentProcess::DBAgentProcess()
{
	this->registSubPacketFunc();
}

void DBAgentProcess::registSubPacketFunc()
{
#define INSERT_PACKET_PROCESS(type)		runFuncTable_.insert(make_pair(E_##type, &DBAgentProcess::##type))

	INSERT_PACKET_PROCESS(I_DB_REQ_ID_PW);
	INSERT_PACKET_PROCESS(I_DB_REQ_LOAD_DATA);
}

void DBAgentProcess::I_DB_REQ_ID_PW(Session *session, Packet *rowPacket)
{
	PK_I_DB_REQ_ID_PW *packet = (PK_I_DB_REQ_ID_PW *)rowPacket;

	QI_DB_REQ_ID_PW *query = new QI_DB_REQ_ID_PW();	        			
	query->clientId_ = packet->clientId_;

	QueryStatement *statement = query->statement();
	statement->addParam((char *)packet->id_.c_str());					
	statement->addParam((char *)packet->password_.c_str());
	
	DBManager::getInstance().pushQuery(query);
}

void DBAgentProcess::I_DB_REQ_LOAD_DATA(Session *session, Packet *rowPacket)
{
	PK_I_DB_REQ_LOAD_DATA *packet = (PK_I_DB_REQ_LOAD_DATA *)rowPacket;

	QI_DB_REQ_LOAD_DATA *query = new QI_DB_REQ_LOAD_DATA();
	query->clientId_ = packet->clientId_;

	QueryStatement *statement = query->statement();
	statement->addParam(packet->oidAccountId_);

	DBManager::getInstance().pushQuery(query);
}
```

## DBAgent\DBAgentProcess.h
```h
#pragma once
#include "stdafx.h"

class DBAgentProcess : public ContentsProcess
{
public:
	DBAgentProcess();
private:
	void registSubPacketFunc();
	static void I_DB_REQ_ID_PW(Session *session, Packet *rowPacket);
	static void I_DB_REQ_LOAD_DATA(Session *session, Packet *rowPacket);
};
```

## DBAgent\main.cpp
```cpp
#include "stdafx.h"
#include "DBAgentProcess.h"

void serverProcess()
{
	shared_ptr<Server> server(new IOCPServer(new DBAgentProcess()));
	if (!server->run()) {
		SLog(L"! error: server start fail");
		return;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	DBManager::getInstance().run();

	shared_ptr<Thread> serverThread(new Thread(new thread_t(serverProcess), L"DBAgent"));
	return 0;
}
```

## DBAgent\Query\QI_DB_REQ_ID_PW.h
```h
#pragma once
#include "stdafx.h"

class QI_DB_REQ_ID_PW: public Query
{
public:
	oid_t clientId_;

	WCHAR *procedure()
	{
		return L"p_AccountData_Select";
	}

	QI_DB_REQ_ID_PW() {
		statement_->setQuery(this->procedure(), QUERY_CALL_BACK);		
	}

	~QI_DB_REQ_ID_PW() {
		PK_I_DB_ANS_ID_PW iPacket;
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

		Terminal *terminal = _terminal.get(L"LoginServer");
		terminal->sendPacket(&iPacket);
	}
};
```

## DBAgent\Query\QI_DB_REQ_LOAD_DATA.h
```h
#pragma once
#include "stdafx.h"

class QI_DB_REQ_LOAD_DATA: public Query
{
public:
	oid_t clientId_;

	WCHAR *procedure()
	{
		return L"p_Character_Select";
	}

	QI_DB_REQ_LOAD_DATA() {
		statement_->setQuery(this->procedure(), QUERY_CALL_BACK);		
	}

	~QI_DB_REQ_LOAD_DATA() {
		PK_I_DB_ANS_PARSE_DATA	iPacket;
		iPacket.clientId_ = (UInt64)clientId_;
		iPacket.result_ = FALSE;
		if (!record_.isEof()) {
			record_.moveFirst();
		}

		while (!record_.isEof()) {
			array<WCHAR, DB_PARAM_SIZE> buffer;

			if (record_.get("name", buffer.data())) {
				SLog(L"id : %s", buffer.data());
				array<CHAR, DB_PARAM_SIZE> nameBuf;
				StrConvW2A(buffer.data(), nameBuf.data(), nameBuf.size());
				iPacket.name_ = nameBuf.data();
				iPacket.result_ = TRUE;
			}
			record_.moveNext();
		}

		Terminal *terminal = _terminal.get(L"ChattingServer");
		terminal->sendPacket(&iPacket);
	}
};
```

## DBAgent\stdafx.cpp
```cpp
// stdafx.cpp : source file that includes just the standard includes
// DBAgent.pch will be the pre-compiled header
// stdafx.obj will contain the pre-compiled type information

#include "stdafx.h"

// TODO: reference any additional headers you need in STDAFX.H
// and not in this file
```

## DBAgent\stdafx.h
```h
// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently, but
// are changed infrequently
//

#pragma once

#include "targetver.h"

#include <stdio.h>
#include <tchar.h>

// TODO: reference additional headers your program requires here
#include "ServerLibrary.h"

#include "./Query/QI_DB_REQ_ID_PW.h"
#include "./Query/QI_DB_REQ_LOAD_DATA.h"
```

## DBAgent\targetver.h
```h
#pragma once

// Including SDKDDKVer.h defines the highest available Windows platform.

// If you wish to build your application for a previous Windows platform, include WinSDKVer.h and
// set the _WIN32_WINNT macro to the platform you wish to support before including SDKDDKVer.h.

#include <SDKDDKVer.h>
```

## DBAgent\x64\Debug\DBAgent.tlog\DBAgent.lastbuildstate
```lastbuildstate
PlatformToolSet=v143:VCToolArchitecture=Native64Bit:VCToolsVersion=14.41.34120:TargetPlatformVersion=10.0.26100.0:
Debug|x64|C:\github\GameServer_Programming\ServerLibrary\|
```

## DummyClient\.vs\DummyClient\v17\DocumentLayout.backup.json
```json
{
  "Version": 1,
  "WorkspaceRootPath": "C:\\github\\GameServer_Programming\\DummyClient\\",
  "Documents": [
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\chatting\\chattingcontents.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\chatting\\chattingcontents.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\chattingform.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}|Form",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:chattingform.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}|Form"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\chattingform.designer.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:chattingform.designer.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\chattingform.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:chattingform.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\contentsprocess.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\contentsprocess.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\programstate.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\programstate.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\formstate.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\formstate.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\packetgen\\packetheader.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\packetgen\\packetheader.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\packetgen\\packetfactory.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\packetgen\\packetfactory.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\chatting\\chattingpacketprocess.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\chatting\\chattingpacketprocess.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\packetgen\\packetclass.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\packetgen\\packetclass.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\network\\network.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\network\\network.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\network\\packet.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\network\\packet.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\network\\packetobfuscation.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\network\\packetobfuscation.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\loginform.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:loginform.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\login\\logincontents.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\login\\logincontents.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\chatting\\chatwnd.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\chatting\\chatwnd.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\network\\packetutil.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\network\\packetutil.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\packetprocess.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\packetprocess.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\dummyclient.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:dummyclient.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|C:\\github\\GameServer_Programming\\DummyClient\\dummyclient.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}|Form",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:dummyclient.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}|Form"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\dummyclient.designer.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:dummyclient.designer.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|C:\\github\\GameServer_Programming\\DummyClient\\loginform.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}|Form",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:loginform.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}|Form"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\dummyclient.csproj||{04B8AB82-A572-4FEF-95CE-5222444B6B64}|",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:dummyclient.csproj||{04B8AB82-A572-4FEF-95CE-5222444B6B64}|"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\loginform.designer.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:loginform.designer.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\program.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:program.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    }
  ],
  "DocumentGroupContainers": [
    {
      "Orientation": 0,
      "VerticalTabListWidth": 256,
      "DocumentGroups": [
        {
          "DockedWidth": 200,
          "SelectedChildIndex": 0,
          "Children": [
            {
              "$type": "Document",
              "DocumentIndex": 0,
              "Title": "ChattingContents.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Chatting\\ChattingContents.cs",
              "RelativeDocumentMoniker": "Source\\Chatting\\ChattingContents.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Chatting\\ChattingContents.cs",
              "RelativeToolTip": "Source\\Chatting\\ChattingContents.cs",
              "ViewState": "AgIAAAUAAAAAAAAAAAAkwBwAAAANAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:25:58.395Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 8,
              "Title": "PacketFactory.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\PacketGen\\PacketFactory.cs",
              "RelativeDocumentMoniker": "Source\\PacketGen\\PacketFactory.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\PacketGen\\PacketFactory.cs",
              "RelativeToolTip": "Source\\PacketGen\\PacketFactory.cs",
              "ViewState": "AgIAABYAAAAAAAAAAAAQwCQAAAAxAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:12:59.48Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 4,
              "Title": "ContentsProcess.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\ContentsProcess.cs",
              "RelativeDocumentMoniker": "Source\\ContentsProcess.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\ContentsProcess.cs",
              "RelativeToolTip": "Source\\ContentsProcess.cs",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAUAAAAFAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:16:34.125Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 2,
              "Title": "ChattingForm.Designer.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\ChattingForm.Designer.cs",
              "RelativeDocumentMoniker": "ChattingForm.Designer.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\ChattingForm.Designer.cs",
              "RelativeToolTip": "ChattingForm.Designer.cs",
              "ViewState": "AgIAAC4AAAAAAAAAAIAwwEQAAAAPAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T07:15:58.345Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 1,
              "Title": "ChattingForm.cs [Design]",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\ChattingForm.cs",
              "RelativeDocumentMoniker": "ChattingForm.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\ChattingForm.cs [Design]",
              "RelativeToolTip": "ChattingForm.cs [Design]",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-03-03T13:51:02.247Z",
              "EditorCaption": " [Design]"
            },
            {
              "$type": "Document",
              "DocumentIndex": 3,
              "Title": "ChattingForm.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\ChattingForm.cs",
              "RelativeDocumentMoniker": "ChattingForm.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\ChattingForm.cs",
              "RelativeToolTip": "ChattingForm.cs",
              "ViewState": "AgIAACIAAAAAAAAAAAApwDoAAAA9AAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-03-03T09:15:29.689Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 9,
              "Title": "ChattingPacketProcess.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Chatting\\ChattingPacketProcess.cs",
              "RelativeDocumentMoniker": "Source\\Chatting\\ChattingPacketProcess.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Chatting\\ChattingPacketProcess.cs",
              "RelativeToolTip": "Source\\Chatting\\ChattingPacketProcess.cs",
              "ViewState": "AgIAAAoAAAAAAAAAAAAowBgAAAAbAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:27:19.923Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 7,
              "Title": "PacketHeader.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\PacketGen\\PacketHeader.cs",
              "RelativeDocumentMoniker": "Source\\PacketGen\\PacketHeader.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\PacketGen\\PacketHeader.cs",
              "RelativeToolTip": "Source\\PacketGen\\PacketHeader.cs",
              "ViewState": "AgIAAAYAAAAAAAAAAAAAAAwAAAAkAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:13:11.575Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 11,
              "Title": "Network.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Network\\Network.cs",
              "RelativeDocumentMoniker": "Source\\Network\\Network.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Network\\Network.cs",
              "RelativeToolTip": "Source\\Network\\Network.cs",
              "ViewState": "AgIAAKcAAAAAAAAAAAAUwJIAAAAWAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T07:28:36.871Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 6,
              "Title": "FormState.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\FormState.cs",
              "RelativeDocumentMoniker": "Source\\FormState.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\FormState.cs",
              "RelativeToolTip": "Source\\FormState.cs",
              "ViewState": "AgIAACgAAAAAAAAAAAAkwEEAAAAkAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:33:06.342Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 5,
              "Title": "ProgramState.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\ProgramState.cs",
              "RelativeDocumentMoniker": "Source\\ProgramState.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\ProgramState.cs",
              "RelativeToolTip": "Source\\ProgramState.cs",
              "ViewState": "AgIAAAoAAAAAAAAAAAAQwBQAAAAbAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:32:54.334Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 10,
              "Title": "PacketClass.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\PacketGen\\PacketClass.cs",
              "RelativeDocumentMoniker": "Source\\PacketGen\\PacketClass.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\PacketGen\\PacketClass.cs",
              "RelativeToolTip": "Source\\PacketGen\\PacketClass.cs",
              "ViewState": "AgIAAMUAAAAAAAAAAAAuwNkAAABXAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T22:57:00.462Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 12,
              "Title": "Packet.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Network\\Packet.cs",
              "RelativeDocumentMoniker": "Source\\Network\\Packet.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Network\\Packet.cs",
              "RelativeToolTip": "Source\\Network\\Packet.cs",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAsAAAAhAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T22:53:41.913Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 13,
              "Title": "PacketObfuscation.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Network\\PacketObfuscation.cs",
              "RelativeDocumentMoniker": "Source\\Network\\PacketObfuscation.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Network\\PacketObfuscation.cs",
              "RelativeToolTip": "Source\\Network\\PacketObfuscation.cs",
              "ViewState": "AgIAABMAAAAAAAAAAAAQwAYAAAAVAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:34:37.614Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 14,
              "Title": "LoginForm.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\LoginForm.cs",
              "RelativeDocumentMoniker": "LoginForm.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\LoginForm.cs",
              "RelativeToolTip": "LoginForm.cs",
              "ViewState": "AgIAAAcAAAAAAAAAAAAowB8AAAAMAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T06:52:01.182Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 15,
              "Title": "LoginContents.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Login\\LoginContents.cs",
              "RelativeDocumentMoniker": "Source\\Login\\LoginContents.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Login\\LoginContents.cs",
              "RelativeToolTip": "Source\\Login\\LoginContents.cs",
              "ViewState": "AgIAAAkAAAAAAAAAAAAuwB8AAAAJAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:22:07.482Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 16,
              "Title": "ChatWnd.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Chatting\\ChatWnd.cs",
              "RelativeDocumentMoniker": "Source\\Chatting\\ChatWnd.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Chatting\\ChatWnd.cs",
              "RelativeToolTip": "Source\\Chatting\\ChatWnd.cs",
              "ViewState": "AgIAADoAAAAAAAAAAAAkwAwAAAAoAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T07:18:51.274Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 17,
              "Title": "PacketUtil.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Network\\PacketUtil.cs",
              "RelativeDocumentMoniker": "Source\\Network\\PacketUtil.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Network\\PacketUtil.cs",
              "RelativeToolTip": "Source\\Network\\PacketUtil.cs",
              "ViewState": "AgIAACwAAAAAAAAAAAAuwDMAAABKAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:14:02.729Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 18,
              "Title": "PacketProcess.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\PacketProcess.cs",
              "RelativeDocumentMoniker": "Source\\PacketProcess.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\PacketProcess.cs",
              "RelativeToolTip": "Source\\PacketProcess.cs",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:15:00.881Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 19,
              "Title": "DummyClient.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\DummyClient.cs",
              "RelativeDocumentMoniker": "DummyClient.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\DummyClient.cs",
              "RelativeToolTip": "DummyClient.cs",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABkAAABTAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T06:48:46.448Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 20,
              "Title": "DummyClient.cs [\uB514\uC790\uC778]",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\DummyClient.cs",
              "RelativeDocumentMoniker": "DummyClient.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\DummyClient.cs [\uB514\uC790\uC778]",
              "RelativeToolTip": "DummyClient.cs [\uB514\uC790\uC778]",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:37:13.682Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 23,
              "Title": "DummyClient",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\DummyClient.csproj",
              "RelativeDocumentMoniker": "DummyClient.csproj",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\DummyClient.csproj",
              "RelativeToolTip": "DummyClient.csproj",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000758|",
              "WhenOpened": "2025-02-17T11:43:33.536Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 24,
              "Title": "LoginForm.Designer.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\LoginForm.Designer.cs",
              "RelativeDocumentMoniker": "LoginForm.Designer.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\LoginForm.Designer.cs",
              "RelativeToolTip": "LoginForm.Designer.cs",
              "ViewState": "AgIAAFcAAAAAAAAAAAAYwGsAAAAlAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T07:17:22.327Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 21,
              "Title": "DummyClient.Designer.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\DummyClient.Designer.cs",
              "RelativeDocumentMoniker": "DummyClient.Designer.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\DummyClient.Designer.cs",
              "RelativeToolTip": "DummyClient.Designer.cs",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABMAAAAkAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T07:10:43.708Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 25,
              "Title": "Program.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Program.cs",
              "RelativeDocumentMoniker": "Program.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Program.cs",
              "RelativeToolTip": "Program.cs",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAA0AAAA2AAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T07:08:00.438Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 22,
              "Title": "LoginForm.cs [\uB514\uC790\uC778]",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\LoginForm.cs",
              "RelativeDocumentMoniker": "LoginForm.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\LoginForm.cs [\uB514\uC790\uC778]",
              "RelativeToolTip": "LoginForm.cs [\uB514\uC790\uC778]",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T06:49:25.79Z"
            }
          ]
        }
      ]
    }
  ]
}
```

## DummyClient\.vs\DummyClient\v17\DocumentLayout.json
```json
{
  "Version": 1,
  "WorkspaceRootPath": "C:\\github\\GameServer_Programming\\DummyClient\\",
  "Documents": [
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\loginform.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:loginform.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\formstate.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\formstate.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\network\\network.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\network\\network.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\program.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:program.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\network\\packet.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\network\\packet.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\programstate.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\programstate.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\createcharacter\\createcharacterprocess.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\createcharacter\\createcharacterprocess.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\packetgen\\packetclass.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\packetgen\\packetclass.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\packetprocess.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\packetprocess.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\packetgen\\packetfactory.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\packetgen\\packetfactory.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\packetgen\\packetheader.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\packetgen\\packetheader.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\network\\packetobfuscation.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\network\\packetobfuscation.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\network\\packetutil.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\network\\packetutil.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\chatting\\chattingpacketprocess.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\chatting\\chattingpacketprocess.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\chatting\\chattingcontents.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\chatting\\chattingcontents.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\createcharacter.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:createcharacter.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\dummyclient.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:dummyclient.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\chattingform.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:chattingform.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\contentsprocess.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\contentsprocess.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|C:\\github\\GameServer_Programming\\DummyClient\\chattingform.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}|Form",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:chattingform.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}|Form"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\chattingform.designer.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:chattingform.designer.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\source\\chatting\\chatwnd.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:source\\chatting\\chatwnd.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|C:\\github\\GameServer_Programming\\DummyClient\\dummyclient.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}|Form",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:dummyclient.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}|Form"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\dummyclient.designer.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:dummyclient.designer.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\dummyclient.csproj||{04B8AB82-A572-4FEF-95CE-5222444B6B64}|",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:dummyclient.csproj||{04B8AB82-A572-4FEF-95CE-5222444B6B64}|"
    },
    {
      "AbsoluteMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|c:\\github\\gameserver_programming\\dummyclient\\loginform.designer.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}",
      "RelativeMoniker": "D:0:0:{67BE53CC-032B-4090-A9A1-3CA1F27BC710}|DummyClient.csproj|solutionrelative:loginform.designer.cs||{A6C744A8-0E4A-4FC6-886A-064283054674}"
    }
  ],
  "DocumentGroupContainers": [
    {
      "Orientation": 0,
      "VerticalTabListWidth": 256,
      "DocumentGroups": [
        {
          "DockedWidth": 200,
          "SelectedChildIndex": 4,
          "Children": [
            {
              "$type": "Document",
              "DocumentIndex": 6,
              "Title": "CreateCharacterProcess.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\CreateCharacter\\CreateCharacterProcess.cs",
              "RelativeDocumentMoniker": "Source\\CreateCharacter\\CreateCharacterProcess.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\CreateCharacter\\CreateCharacterProcess.cs",
              "RelativeToolTip": "Source\\CreateCharacter\\CreateCharacterProcess.cs",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABIAAAAJAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-03-27T12:35:50.058Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 1,
              "Title": "FormState.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\FormState.cs",
              "RelativeDocumentMoniker": "Source\\FormState.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\FormState.cs",
              "RelativeToolTip": "Source\\FormState.cs",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAYAAAAFAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:33:06.342Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 8,
              "Title": "PacketProcess.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\PacketProcess.cs",
              "RelativeDocumentMoniker": "Source\\PacketProcess.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\PacketProcess.cs",
              "RelativeToolTip": "Source\\PacketProcess.cs",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAYAAAA2AAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:15:00.881Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 5,
              "Title": "ProgramState.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\ProgramState.cs",
              "RelativeDocumentMoniker": "Source\\ProgramState.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\ProgramState.cs",
              "RelativeToolTip": "Source\\ProgramState.cs",
              "ViewState": "AgIAACEAAAAAAAAAAAAYwDsAAAAgAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:32:54.334Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 0,
              "Title": "LoginForm.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\LoginForm.cs",
              "RelativeDocumentMoniker": "LoginForm.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\LoginForm.cs",
              "RelativeToolTip": "LoginForm.cs",
              "ViewState": "AgIAAAEAAAAAAAAAAAAawAsAAAABAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T06:52:01.182Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 3,
              "Title": "Program.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Program.cs",
              "RelativeDocumentMoniker": "Program.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Program.cs",
              "RelativeToolTip": "Program.cs",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAsAAAAjAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T07:08:00.438Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 2,
              "Title": "Network.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Network\\Network.cs",
              "RelativeDocumentMoniker": "Source\\Network\\Network.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Network\\Network.cs",
              "RelativeToolTip": "Source\\Network\\Network.cs",
              "ViewState": "AgIAAJsAAAAAAAAAAAAUwBAAAAATAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T07:28:36.871Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 4,
              "Title": "Packet.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Network\\Packet.cs",
              "RelativeDocumentMoniker": "Source\\Network\\Packet.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Network\\Packet.cs",
              "RelativeToolTip": "Source\\Network\\Packet.cs",
              "ViewState": "AgIAAAAAAAAAAAAAAAAuwAcAAAANAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T22:53:41.913Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 9,
              "Title": "PacketFactory.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\PacketGen\\PacketFactory.cs",
              "RelativeDocumentMoniker": "Source\\PacketGen\\PacketFactory.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\PacketGen\\PacketFactory.cs",
              "RelativeToolTip": "Source\\PacketGen\\PacketFactory.cs",
              "ViewState": "AgIAABMAAAAAAAAAAAAQwCgAAAAJAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:12:59.48Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 7,
              "Title": "PacketClass.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\PacketGen\\PacketClass.cs",
              "RelativeDocumentMoniker": "Source\\PacketGen\\PacketClass.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\PacketGen\\PacketClass.cs",
              "RelativeToolTip": "Source\\PacketGen\\PacketClass.cs",
              "ViewState": "AgIAAEUAAAAAAAAAAAAAwM4BAAAJAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T22:57:00.462Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 10,
              "Title": "PacketHeader.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\PacketGen\\PacketHeader.cs",
              "RelativeDocumentMoniker": "Source\\PacketGen\\PacketHeader.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\PacketGen\\PacketHeader.cs",
              "RelativeToolTip": "Source\\PacketGen\\PacketHeader.cs",
              "ViewState": "AgIAAA0AAAAAAAAAAAAQwCMAAAAmAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:13:11.575Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 11,
              "Title": "PacketObfuscation.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Network\\PacketObfuscation.cs",
              "RelativeDocumentMoniker": "Source\\Network\\PacketObfuscation.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Network\\PacketObfuscation.cs",
              "RelativeToolTip": "Source\\Network\\PacketObfuscation.cs",
              "ViewState": "AgIAABMAAAAAAAAAAAAQwAYAAAAVAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:34:37.614Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 12,
              "Title": "PacketUtil.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Network\\PacketUtil.cs",
              "RelativeDocumentMoniker": "Source\\Network\\PacketUtil.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Network\\PacketUtil.cs",
              "RelativeToolTip": "Source\\Network\\PacketUtil.cs",
              "ViewState": "AgIAACwAAAAAAAAAAAA+wDMAAABKAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:14:02.729Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 14,
              "Title": "ChattingContents.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Chatting\\ChattingContents.cs",
              "RelativeDocumentMoniker": "Source\\Chatting\\ChattingContents.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Chatting\\ChattingContents.cs",
              "RelativeToolTip": "Source\\Chatting\\ChattingContents.cs",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABwAAAANAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:25:58.395Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 15,
              "Title": "CreateCharacter.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\CreateCharacter.cs",
              "RelativeDocumentMoniker": "CreateCharacter.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\CreateCharacter.cs",
              "RelativeToolTip": "CreateCharacter.cs",
              "ViewState": "AgIAAAMAAAAAAAAAAAAqwAwAAAABAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-03-27T12:30:43.04Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 16,
              "Title": "DummyClient.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\DummyClient.cs",
              "RelativeDocumentMoniker": "DummyClient.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\DummyClient.cs",
              "RelativeToolTip": "DummyClient.cs",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABIAAAAJAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T06:48:46.448Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 17,
              "Title": "ChattingForm.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\ChattingForm.cs",
              "RelativeDocumentMoniker": "ChattingForm.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\ChattingForm.cs",
              "RelativeToolTip": "ChattingForm.cs",
              "ViewState": "AgIAAB8AAAAAAAAAAAA7wDEAAAAJAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-03-03T09:15:29.689Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 18,
              "Title": "ContentsProcess.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\ContentsProcess.cs",
              "RelativeDocumentMoniker": "Source\\ContentsProcess.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\ContentsProcess.cs",
              "RelativeToolTip": "Source\\ContentsProcess.cs",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAUAAAAFAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:16:34.125Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 13,
              "Title": "ChattingPacketProcess.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Chatting\\ChattingPacketProcess.cs",
              "RelativeDocumentMoniker": "Source\\Chatting\\ChattingPacketProcess.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Chatting\\ChattingPacketProcess.cs",
              "RelativeToolTip": "Source\\Chatting\\ChattingPacketProcess.cs",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAA4AAAAvAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:27:19.923Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 19,
              "Title": "ChattingForm.cs [\uB514\uC790\uC778]",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\ChattingForm.cs",
              "RelativeDocumentMoniker": "ChattingForm.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\ChattingForm.cs [\uB514\uC790\uC778]",
              "RelativeToolTip": "ChattingForm.cs [\uB514\uC790\uC778]",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-03-03T13:51:02.247Z",
              "EditorCaption": " [\uB514\uC790\uC778]"
            },
            {
              "$type": "Document",
              "DocumentIndex": 20,
              "Title": "ChattingForm.Designer.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\ChattingForm.Designer.cs",
              "RelativeDocumentMoniker": "ChattingForm.Designer.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\ChattingForm.Designer.cs",
              "RelativeToolTip": "ChattingForm.Designer.cs",
              "ViewState": "AgIAAC4AAAAAAAAAAIAwwEQAAAAPAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T07:15:58.345Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 21,
              "Title": "ChatWnd.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Chatting\\ChatWnd.cs",
              "RelativeDocumentMoniker": "Source\\Chatting\\ChatWnd.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\Source\\Chatting\\ChatWnd.cs",
              "RelativeToolTip": "Source\\Chatting\\ChatWnd.cs",
              "ViewState": "AgIAADoAAAAAAAAAAAAkwAwAAAAoAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T07:18:51.274Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 22,
              "Title": "DummyClient.cs [\uB514\uC790\uC778]",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\DummyClient.cs",
              "RelativeDocumentMoniker": "DummyClient.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\DummyClient.cs [\uB514\uC790\uC778]",
              "RelativeToolTip": "DummyClient.cs [\uB514\uC790\uC778]",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T23:37:13.682Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 24,
              "Title": "DummyClient",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\DummyClient.csproj",
              "RelativeDocumentMoniker": "DummyClient.csproj",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\DummyClient.csproj",
              "RelativeToolTip": "DummyClient.csproj",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000758|",
              "WhenOpened": "2025-02-17T11:43:33.536Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 25,
              "Title": "LoginForm.Designer.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\LoginForm.Designer.cs",
              "RelativeDocumentMoniker": "LoginForm.Designer.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\LoginForm.Designer.cs",
              "RelativeToolTip": "LoginForm.Designer.cs",
              "ViewState": "AgIAABYAAAAAAAAAAAAYwBYAAAAIAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T07:17:22.327Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 23,
              "Title": "DummyClient.Designer.cs",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DummyClient\\DummyClient.Designer.cs",
              "RelativeDocumentMoniker": "DummyClient.Designer.cs",
              "ToolTip": "C:\\github\\GameServer_Programming\\DummyClient\\DummyClient.Designer.cs",
              "RelativeToolTip": "DummyClient.Designer.cs",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABMAAAAkAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000738|",
              "WhenOpened": "2025-02-06T07:10:43.708Z"
            }
          ]
        }
      ]
    }
  ]
}
```

## DummyClient\bin\Debug\net6.0-windows7.0\DummyClient.deps.json
```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v6.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v6.0": {
      "DummyClient/1.0.0": {
        "runtime": {
          "DummyClient.dll": {}
        }
      }
    }
  },
  "libraries": {
    "DummyClient/1.0.0": {
      "type": "project",
      "serviceable": false,
      "sha512": ""
    }
  }
}
```

## DummyClient\bin\Debug\net6.0-windows7.0\DummyClient.runtimeconfig.json
```json
{
  "runtimeOptions": {
    "tfm": "net6.0",
    "frameworks": [
      {
        "name": "Microsoft.NETCore.App",
        "version": "6.0.0"
      },
      {
        "name": "Microsoft.WindowsDesktop.App",
        "version": "6.0.0"
      }
    ]
  }
}
```

## DummyClient\bin\Debug\net8.0-windows\DummyClient.deps.json
```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v8.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v8.0": {
      "DummyClient/1.0.0": {
        "runtime": {
          "DummyClient.dll": {}
        }
      }
    }
  },
  "libraries": {
    "DummyClient/1.0.0": {
      "type": "project",
      "serviceable": false,
      "sha512": ""
    }
  }
}
```

## DummyClient\bin\Debug\net8.0-windows\DummyClient.runtimeconfig.json
```json
{
  "runtimeOptions": {
    "tfm": "net8.0",
    "frameworks": [
      {
        "name": "Microsoft.NETCore.App",
        "version": "8.0.0"
      },
      {
        "name": "Microsoft.WindowsDesktop.App",
        "version": "8.0.0"
      }
    ],
    "configProperties": {
      "System.Runtime.Serialization.EnableUnsafeBinaryFormatterSerialization": true
    }
  }
}
```

## DummyClient\ChattingForm.cs
```cs
癤퓎sing System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DummyClient
{
    public partial class ChattingForm : Form
    {
        private ChatWnd chatWnd_ = null;

        public ChattingForm()
        {
            InitializeComponent();
            Control.CheckForIllegalCrossThreadCalls = false;
            chatWnd_ = new ChatWnd(richTextBox_view_);
            Program.programState_.putMessage_ += new ProgramState.putMessageDele(pushText);
        }

        ~ChattingForm()
        {
            base.Dispose();
            chatWnd_ = null;
        }

        private void textBox_input_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                String inputStr = textBox_input_.Text + Environment.NewLine;
                richTextBox_view_.Text += inputStr;
                textBox_input_.Clear();

                PK_C_REQ_CHATTING packet = new PK_C_REQ_CHATTING();
                packet.text_ = inputStr;
                Program.programState_.sendPacket(packet);
                packet = null;

            }
            e.Handled = true;
        }

        public void pushText(string text)
        {
            chatWnd_.pushText(text);
        }


        private void leaveUsers(object sender, EventArgs e)
        {
            //PK_C_REQ_EXIT exitPacket = new PK_C_REQ_EXIT();
            PK_C_REQ_CHAT_EXIT exitUserPacket = new PK_C_REQ_CHAT_EXIT();
            Program.programState_.sendPacket(exitUserPacket);
            // Program.programState_.sendPacket(exitPacket);
            Application.Exit();
        }


    }
}
```

## DummyClient\ChattingForm.Designer.cs
```cs
癤퓆amespace DummyClient
{
    partial class ChattingForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            textBox_input_ = new TextBox();
            richTextBox_view_ = new RichTextBox();
            exitButton_ = new Button();
            SuspendLayout();
            // 
            // textBox_input_
            // 
            textBox_input_.Location = new Point(20, 392);
            textBox_input_.Margin = new Padding(3, 4, 3, 4);
            textBox_input_.Name = "textBox_input_";
            textBox_input_.Size = new Size(456, 23);
            textBox_input_.TabIndex = 3;
            textBox_input_.KeyDown += textBox_input_KeyDown;
            // 
            // richTextBox_view_
            // 
            richTextBox_view_.BackColor = Color.Teal;
            richTextBox_view_.ForeColor = Color.White;
            richTextBox_view_.Location = new Point(20, 15);
            richTextBox_view_.Margin = new Padding(3, 4, 3, 4);
            richTextBox_view_.Name = "richTextBox_view_";
            richTextBox_view_.ReadOnly = true;
            richTextBox_view_.ScrollBars = RichTextBoxScrollBars.Vertical;
            richTextBox_view_.Size = new Size(457, 369);
            richTextBox_view_.TabIndex = 2;
            richTextBox_view_.Text = "";
            // 
            // exitButton_
            // 
            exitButton_.Location = new Point(208, 439);
            exitButton_.Name = "exitButton_";
            exitButton_.Size = new Size(75, 23);
            exitButton_.TabIndex = 4;
            exitButton_.Text = "Exit";
            exitButton_.UseVisualStyleBackColor = true;
            exitButton_.Click += leaveUsers;
            // 
            // ChattingForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            AutoSize = true;
            AutoSizeMode = AutoSizeMode.GrowAndShrink;
            ClientSize = new Size(498, 495);
            Controls.Add(exitButton_);
            Controls.Add(textBox_input_);
            Controls.Add(richTextBox_view_);
            FormBorderStyle = FormBorderStyle.None;
            Margin = new Padding(3, 4, 3, 4);
            Name = "ChattingForm";
            Text = "ChattingForm";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private System.Windows.Forms.TextBox textBox_input_;
        private System.Windows.Forms.RichTextBox richTextBox_view_;
        private Button exitButton_;
    }
}
```

## DummyClient\CreateCharacter.cs
```cs
癤퓎sing System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DummyClient
{
    public partial class CreateCharacterForm : Form
    {

        public CreateCharacterForm()
        {
        }

        ~CreateCharacterForm()
        {
            base.Dispose();

        }

     


    }
}
```

## DummyClient\CreateCharacter.Designer.cs
```cs
癤퓆amespace DummyClient
{
    partial class CreateCharacter
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Text = "Form1";
        }

        #endregion
    }
}
```

## DummyClient\DummyClient.cs
```cs
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DummyClient
{
    partial class DummyClient : Form
    {
        public DummyClient()
        {
            InitializeComponent();
            Control.CheckForIllegalCrossThreadCalls = false;
        }

        private void DummyClient_Shown(object sender, EventArgs e)
        {
            Program.programState_.setState(PROGRAM_STATE.LOGIN, null, 0);
        }

        private void DummyClient_FormClosing(object sender, FormClosingEventArgs e)
        {
            Program.programState_.close();
            this.Dispose();
            Application.Exit();
        }

        public void removePanelForm(ref Form form)
        {
            mainPanel_.Controls.Remove(form);
        }
    }
}
```

## DummyClient\DummyClient.Designer.cs
```cs
癤퓆amespace DummyClient
{
    partial class DummyClient
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.mainPanel_ = new System.Windows.Forms.Panel();
            this.SuspendLayout();
            // 
            // mainPanel_
            // 
            this.mainPanel_.Location = new System.Drawing.Point(5, 8);
            this.mainPanel_.Name = "mainPanel_";
            this.mainPanel_.Size = new System.Drawing.Size(608, 420);
            this.mainPanel_.TabIndex = 0;
            // 
            // DummyClient
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(624, 441);
            this.Controls.Add(this.mainPanel_);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.Name = "DummyClient";
            this.Text = "DummyClient";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.DummyClient_FormClosing);
            this.Shown += new System.EventHandler(this.DummyClient_Shown);
            this.ResumeLayout(false);

        }

        #endregion

        public System.Windows.Forms.Panel mainPanel_;

    }
}
```

## DummyClient\LoginForm.cs
```cs
癤퓎sing System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DummyClient
{
    public partial class LoginForm : Form
    {

        public LoginForm()
        {
            InitializeComponent();
        }

        private void button_login_Click(object sender, EventArgs e)
        {
            PK_C_REQ_ID_PW packet = new PK_C_REQ_ID_PW();
            packet.id_ = textBox_id_.Text;
            packet.password_ = textBox_pw_.Text;
            Program.programState_.sendPacket(packet);
        }

        private void button_quit(object sender, EventArgs e)
        {
            this.Dispose();
            Application.Exit();
        }

        private void Character_Click(object sender, EventArgs e)
        {
            PK_S_ANS_CREATECHARACTER_OPEN packet = new PK_S_ANS_CREATECHARACTER_OPEN();
            Program.programState_.sendPacket(packet);
        }
    }
}
```

## DummyClient\obj\Debug\net5.0-windows7.0\.NETCoreApp,Version=v5.0.AssemblyAttributes.cs
```cs
// <autogenerated />
using System;
using System.Reflection;
[assembly: global::System.Runtime.Versioning.TargetFrameworkAttribute(".NETCoreApp,Version=v5.0", FrameworkDisplayName = ".NET 5.0")]
```

## DummyClient\obj\Debug\net5.0-windows7.0\DummyClient.designer.deps.json
```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v5.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v5.0": {}
  },
  "libraries": {}
}
```

## DummyClient\obj\Debug\net5.0-windows7.0\DummyClient.GeneratedMSBuildEditorConfig.editorconfig
```editorconfig
is_global = true
build_property.ApplicationManifest = 
build_property.StartupObject = 
build_property.ApplicationDefaultFont = 
build_property.ApplicationHighDpiMode = 
build_property.ApplicationUseCompatibleTextRendering = 
build_property.ApplicationVisualStyles = 
build_property.TargetFramework = net5.0-windows7.0
build_property.TargetPlatformMinVersion = 7.0
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = DummyClient
build_property.ProjectDir = C:\github\GameServer_Programming\DummyClient\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

## DummyClient\obj\Debug\net5.0-windows7.0\DummyClient.GlobalUsings.g.cs
```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.Drawing;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
global using global::System.Windows.Forms;
```

## DummyClient\obj\Debug\net6.0-windows7.0\.NETCoreApp,Version=v6.0.AssemblyAttributes.cs
```cs
// <autogenerated />
using System;
using System.Reflection;
[assembly: global::System.Runtime.Versioning.TargetFrameworkAttribute(".NETCoreApp,Version=v6.0", FrameworkDisplayName = ".NET 6.0")]
```

## DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.csproj.BuildWithSkipAnalyzers
```BuildWithSkipAnalyzers

```

## DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.csproj.FileListAbsolute.txt
```txt
C:\github\GameServer_Programming\DummyClient\bin\Debug\net6.0-windows7.0\DummyClient.exe
C:\github\GameServer_Programming\DummyClient\bin\Debug\net6.0-windows7.0\DummyClient.deps.json
C:\github\GameServer_Programming\DummyClient\bin\Debug\net6.0-windows7.0\DummyClient.runtimeconfig.json
C:\github\GameServer_Programming\DummyClient\bin\Debug\net6.0-windows7.0\DummyClient.dll
C:\github\GameServer_Programming\DummyClient\bin\Debug\net6.0-windows7.0\DummyClient.pdb
C:\github\GameServer_Programming\DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.ChattingForm.resources
C:\github\GameServer_Programming\DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.DummyClient.resources
C:\github\GameServer_Programming\DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.LoginForm.resources
C:\github\GameServer_Programming\DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.csproj.GenerateResource.cache
C:\github\GameServer_Programming\DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.GeneratedMSBuildEditorConfig.editorconfig
C:\github\GameServer_Programming\DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.AssemblyInfoInputs.cache
C:\github\GameServer_Programming\DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.AssemblyInfo.cs
C:\github\GameServer_Programming\DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.csproj.CoreCompileInputs.cache
C:\github\GameServer_Programming\DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.sourcelink.json
C:\github\GameServer_Programming\DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.dll
C:\github\GameServer_Programming\DummyClient\obj\Debug\net6.0-windows7.0\refint\DummyClient.dll
C:\github\GameServer_Programming\DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.pdb
C:\github\GameServer_Programming\DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.genruntimeconfig.cache
C:\github\GameServer_Programming\DummyClient\obj\Debug\net6.0-windows7.0\ref\DummyClient.dll
```

## DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.designer.deps.json
```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v6.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v6.0": {}
  },
  "libraries": {}
}
```

## DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.GeneratedMSBuildEditorConfig.editorconfig
```editorconfig
is_global = true
build_property.ApplicationManifest = 
build_property.StartupObject = 
build_property.ApplicationDefaultFont = 
build_property.ApplicationHighDpiMode = 
build_property.ApplicationUseCompatibleTextRendering = 
build_property.ApplicationVisualStyles = 
build_property.TargetFramework = net6.0-windows7.0
build_property.TargetPlatformMinVersion = 7.0
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = DummyClient
build_property.ProjectDir = C:\github\GameServer_Programming\DummyClient\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

## DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.GlobalUsings.g.cs
```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.Drawing;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
global using global::System.Windows.Forms;
```

## DummyClient\obj\Debug\net6.0-windows7.0\DummyClient.sourcelink.json
```json
{"documents":{"C:\\github\\GameServer_Programming\\*":"https://raw.githubusercontent.com/rapidswap/GameServer_Programming/bcb4ea079adfcf5c0eca0b718694e0d7a054b67a/*"}}
```

## DummyClient\obj\Debug\net7.0-windows7.0\.NETCoreApp,Version=v7.0.AssemblyAttributes.cs
```cs
// <autogenerated />
using System;
using System.Reflection;
[assembly: global::System.Runtime.Versioning.TargetFrameworkAttribute(".NETCoreApp,Version=v7.0", FrameworkDisplayName = ".NET 7.0")]
```

## DummyClient\obj\Debug\net7.0-windows7.0\DummyClient.GeneratedMSBuildEditorConfig.editorconfig
```editorconfig
is_global = true
build_property.ApplicationManifest = 
build_property.StartupObject = 
build_property.ApplicationDefaultFont = 
build_property.ApplicationHighDpiMode = 
build_property.ApplicationUseCompatibleTextRendering = 
build_property.ApplicationVisualStyles = 
build_property.TargetFramework = net7.0-windows7.0
build_property.TargetPlatformMinVersion = 7.0
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = DummyClient
build_property.ProjectDir = C:\github\GameServer_Programming\DummyClient\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

## DummyClient\obj\Debug\net7.0-windows7.0\DummyClient.GlobalUsings.g.cs
```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.Drawing;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
global using global::System.Windows.Forms;
```

## DummyClient\obj\Debug\net8.0-windows\.NETCoreApp,Version=v8.0.AssemblyAttributes.cs
```cs
// <autogenerated />
using System;
using System.Reflection;
[assembly: global::System.Runtime.Versioning.TargetFrameworkAttribute(".NETCoreApp,Version=v8.0", FrameworkDisplayName = ".NET 8.0")]
```

## DummyClient\obj\Debug\net8.0-windows\DummyClient.csproj.BuildWithSkipAnalyzers
```BuildWithSkipAnalyzers

```

## DummyClient\obj\Debug\net8.0-windows\DummyClient.csproj.FileListAbsolute.txt
```txt
C:\github\GameServer_Programming\DummyClient\bin\Debug\net8.0-windows\DummyClient.exe
C:\github\GameServer_Programming\DummyClient\bin\Debug\net8.0-windows\DummyClient.deps.json
C:\github\GameServer_Programming\DummyClient\bin\Debug\net8.0-windows\DummyClient.runtimeconfig.json
C:\github\GameServer_Programming\DummyClient\bin\Debug\net8.0-windows\DummyClient.dll
C:\github\GameServer_Programming\DummyClient\bin\Debug\net8.0-windows\DummyClient.pdb
C:\github\GameServer_Programming\DummyClient\obj\Debug\net8.0-windows\DummyClient.ChattingForm.resources
C:\github\GameServer_Programming\DummyClient\obj\Debug\net8.0-windows\DummyClient.DummyClient.resources
C:\github\GameServer_Programming\DummyClient\obj\Debug\net8.0-windows\DummyClient.LoginForm.resources
C:\github\GameServer_Programming\DummyClient\obj\Debug\net8.0-windows\DummyClient.csproj.GenerateResource.cache
C:\github\GameServer_Programming\DummyClient\obj\Debug\net8.0-windows\DummyClient.GeneratedMSBuildEditorConfig.editorconfig
C:\github\GameServer_Programming\DummyClient\obj\Debug\net8.0-windows\DummyClient.AssemblyInfoInputs.cache
C:\github\GameServer_Programming\DummyClient\obj\Debug\net8.0-windows\DummyClient.AssemblyInfo.cs
C:\github\GameServer_Programming\DummyClient\obj\Debug\net8.0-windows\DummyClient.csproj.CoreCompileInputs.cache
C:\github\GameServer_Programming\DummyClient\obj\Debug\net8.0-windows\DummyClient.sourcelink.json
C:\github\GameServer_Programming\DummyClient\obj\Debug\net8.0-windows\DummyClient.dll
C:\github\GameServer_Programming\DummyClient\obj\Debug\net8.0-windows\refint\DummyClient.dll
C:\github\GameServer_Programming\DummyClient\obj\Debug\net8.0-windows\DummyClient.pdb
C:\github\GameServer_Programming\DummyClient\obj\Debug\net8.0-windows\DummyClient.genruntimeconfig.cache
C:\github\GameServer_Programming\DummyClient\obj\Debug\net8.0-windows\ref\DummyClient.dll
```

## DummyClient\obj\Debug\net8.0-windows\DummyClient.designer.deps.json
```json
{
  "runtimeTarget": {
    "name": ".NETCoreApp,Version=v8.0",
    "signature": ""
  },
  "compilationOptions": {},
  "targets": {
    ".NETCoreApp,Version=v8.0": {}
  },
  "libraries": {}
}
```

## DummyClient\obj\Debug\net8.0-windows\DummyClient.GeneratedMSBuildEditorConfig.editorconfig
```editorconfig
is_global = true
build_property.ApplicationManifest = 
build_property.StartupObject = 
build_property.ApplicationDefaultFont = 
build_property.ApplicationHighDpiMode = 
build_property.ApplicationUseCompatibleTextRendering = 
build_property.ApplicationVisualStyles = 
build_property.TargetFramework = net8.0-windows
build_property.TargetPlatformMinVersion = 7.0
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = DummyClient
build_property.ProjectDir = C:\github\GameServer_Programming\DummyClient\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

## DummyClient\obj\Debug\net8.0-windows\DummyClient.GlobalUsings.g.cs
```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.Drawing;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
global using global::System.Windows.Forms;
```

## DummyClient\obj\Debug\net8.0-windows\DummyClient.sourcelink.json
```json
{"documents":{"C:\\github\\GameServer_Programming\\*":"https://raw.githubusercontent.com/rapidswap/GameServer_Programming/8e3507c9f732037e3b7ff27868ce92c55273ddc7/*"}}
```

## DummyClient\obj\Debug\net8.0-windows7.0\.NETCoreApp,Version=v8.0.AssemblyAttributes.cs
```cs
// <autogenerated />
using System;
using System.Reflection;
[assembly: global::System.Runtime.Versioning.TargetFrameworkAttribute(".NETCoreApp,Version=v8.0", FrameworkDisplayName = ".NET 8.0")]
```

## DummyClient\obj\Debug\net8.0-windows7.0\DummyClient.GeneratedMSBuildEditorConfig.editorconfig
```editorconfig
is_global = true
build_property.ApplicationManifest = 
build_property.StartupObject = 
build_property.ApplicationDefaultFont = 
build_property.ApplicationHighDpiMode = 
build_property.ApplicationUseCompatibleTextRendering = 
build_property.ApplicationVisualStyles = 
build_property.TargetFramework = net8.0-windows7.0
build_property.TargetPlatformMinVersion = 7.0
build_property.UsingMicrosoftNETSdkWeb = 
build_property.ProjectTypeGuids = 
build_property.InvariantGlobalization = 
build_property.PlatformNeutralAssembly = 
build_property.EnforceExtendedAnalyzerRules = 
build_property._SupportedPlatformList = Linux,macOS,Windows
build_property.RootNamespace = DummyClient
build_property.ProjectDir = C:\github\GameServer_Programming\DummyClient\
build_property.EnableComHosting = 
build_property.EnableGeneratedComInterfaceComImportInterop =
```

## DummyClient\obj\Debug\net8.0-windows7.0\DummyClient.GlobalUsings.g.cs
```cs
// <auto-generated/>
global using global::System;
global using global::System.Collections.Generic;
global using global::System.Drawing;
global using global::System.IO;
global using global::System.Linq;
global using global::System.Net.Http;
global using global::System.Threading;
global using global::System.Threading.Tasks;
global using global::System.Windows.Forms;
```

## DummyClient\Program.cs
```cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DummyClient
{
    internal static class Program
    {
        public static DummyClient mainForm_ = null;
        public static ProgramState programState_= null;
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);

            mainForm_ = new DummyClient();
            programState_=new ProgramState();
            Application.Run(mainForm_);
            Application.Exit();
        }
    }
}
```

## DummyClient\Source\Chatting\ChatWnd.cs
```cs
癤퓎sing System;
using System.Windows.Forms;

namespace DummyClient
{
    internal class ChatWnd
    {
        private enum TextView
        {
            LINE_MAX = 5000,
        }

        private RichTextBox outputView_;

        public ChatWnd(RichTextBox richTextBox)
        {
            this.outputView_ = richTextBox;
        }

        private void chattingMessageResize()
        {
            String str = outputView_.Text;
            int textLine = 0;

            while (true)
            {
                int idx = str.IndexOf(Environment.NewLine);
                if (idx < 0)
                {
                    break;
                }
                str = str.Substring(idx + Environment.NewLine.Length);
                ++textLine;
            }

            if (textLine > (int)TextView.LINE_MAX)
            {
                String originalStr = outputView_.Text;

                int idx = originalStr.IndexOf(Environment.NewLine);
                originalStr = originalStr.Substring(idx + Environment.NewLine.Length);

                outputView_.Text = originalStr;
            }
        }

        public void textChanged(object sender, EventArgs e)
        {
            chattingMessageResize();

            String str = outputView_.Text;
            int len = str.LastIndexOf('\n');
            if (len < 0)
            {
                return;
            }
            outputView_.SelectionStart = len;
            outputView_.ScrollToCaret();
        }

        public void pushText(string text)
        {
            if (outputView_ == null)
            {
                return;
            }
            outputView_.AppendText(text + Environment.NewLine);
            outputView_.ScrollToCaret();
        }
    }
}
```

## DummyClient\Source\ContentsProcess.cs
```cs
癤퓎sing System.Windows.Forms;

namespace DummyClient
{
    internal abstract class ContentsProcess
    {
//怨듯넻泥섎━
    }
}
```

## DummyClient\Source\CreateCharacter\CreateCharacterContents.cs
```cs
癤퓎sing System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DummyClient
{
    class CreateCharacterContents : ContentsProcess
    {
        public void S_ANS_CREATECHARCTER(PacketInterface rowPacket)
        {

        }
    }
}
```

## DummyClient\Source\CreateCharacter\CreateCharacterProcess.cs
```cs
癤퓎sing System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DummyClient
{
    class CreateCharacterProcess : PacketProcess
    {
        CreateCharacterContents contents_ = null;

        public CreateCharacterProcess()
        {
            contents_ = new CreateCharacterContents();
        }
        public override void run(PacketInterface packet)
        {
        }
    }
}
```

## DummyClient\Source\Network\Packet.cs
```cs
癤퓎sing System;
using System.IO;

namespace DummyClient
{
    public interface PacketInterface
    {
        void encode();
        void decode(byte[] packet, ref int offset);

        Int64 type();
        MemoryStream getStream();
    }

    public class PacketData
    {
        protected MemoryStream packet_ = new MemoryStream();

        ~PacketData()
        {
            packet_ = null;
        }
    }
}
```

## DummyClient\Source\Network\PacketObfuscation.cs
```cs
癤퓎sing System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DummyClient
{
    static class PacketObfuscation
    {
        static Byte[] key_ = Encoding.ASCII.GetBytes(PacketMakeDate.stamp());

        static private void CalcXor(ref Byte[] packet, int packetOffset, int packetLen)
        {
            int keyIdx = packetOffset % key_.Length;
            for (int packetIdx = 0; packetIdx < packetLen; ++packetIdx)
            {
                packet[packetIdx] ^= key_[keyIdx++];
                if (keyIdx == key_.Length)
                {
                    keyIdx = 0;
                }
            }
        }

        static public void encodingHeader(ref Byte[] packet, int packetLen)
        {
            CalcXor(ref packet, 0, packetLen);
        }
        static public void encodingData(ref Byte[] packet, int packetLen)
        {
            CalcXor(ref packet, sizeof(Int32), packetLen);
        }

        static public void decodingHeader(ref Byte[] packet, int packetLen)
        {
            CalcXor(ref packet, 0, packetLen);
        }
        static public void decodingData(ref Byte[] packet, int packetLen)
        {
            CalcXor(ref packet, sizeof(Int32), packetLen);
        }
    }
}
```

## DummyClient\Source\PacketGen\PacketClass.cs
```cs
癤퓎sing System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.IO;
using System.Net.Sockets;

namespace DummyClient
{
    public class PK_C_REQ_EXIT : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_C_REQ_EXIT; }
        Int64 type() { return (Int64)PacketType.E_C_REQ_EXIT; }
        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_S_ANS_EXIT : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_EXIT; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_EXIT; }
        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_I_NOTIFY_TERMINAL : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_NOTIFY_TERMINAL; }
        Int64 type() { return (Int64)PacketType.E_I_NOTIFY_TERMINAL; }
        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_C_NOTIFY_HEARTBEAT : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_C_NOTIFY_HEARTBEAT; }
        Int64 type() { return (Int64)PacketType.E_C_NOTIFY_HEARTBEAT; }
        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_C_REQ_ID_PW : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_C_REQ_ID_PW; }
        Int64 type() { return (Int64)PacketType.E_C_REQ_ID_PW; }
        public string id_;
        public string password_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, id_);
            PacketUtil.encode(packet_, password_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            id_ = PacketUtil.decodestring(packet, ref offset);
            password_ = PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_S_ANS_ID_PW_FAIL : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_ID_PW_FAIL; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_ID_PW_FAIL; }
        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_S_ANS_ID_PW_SUCCESS : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_ID_PW_SUCCESS; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_ID_PW_SUCCESS; }
        public string ip_;
        public UInt32 port_;
        public string name_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, ip_);
            PacketUtil.encode(packet_, port_);
            PacketUtil.encode(packet_, name_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            ip_ = PacketUtil.decodestring(packet, ref offset);
            port_ = PacketUtil.decodeUInt32(packet, ref offset);
            name_ = PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_I_DB_REQ_ID_PW : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_DB_REQ_ID_PW; }
        Int64 type() { return (Int64)PacketType.E_I_DB_REQ_ID_PW; }
        public UInt64 clientId_;
        public string id_;
        public string password_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, id_);
            PacketUtil.encode(packet_, password_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            id_ = PacketUtil.decodestring(packet, ref offset);
            password_ = PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_I_DB_ANS_ID_PW : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_DB_ANS_ID_PW; }
        Int64 type() { return (Int64)PacketType.E_I_DB_ANS_ID_PW; }
        public UInt64 clientId_;
        public UInt64 oidAccountId_;
        public Byte result_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, oidAccountId_);
            PacketUtil.encode(packet_, result_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            oidAccountId_ = PacketUtil.decodeUInt64(packet, ref offset);
            result_ = PacketUtil.decodeByte(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_I_CHTTING_NOTIFY_ID : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_CHTTING_NOTIFY_ID; }
        Int64 type() { return (Int64)PacketType.E_I_CHTTING_NOTIFY_ID; }
        public UInt64 clientId_;
        public UInt64 oidAccountId_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, oidAccountId_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            oidAccountId_ = PacketUtil.decodeUInt64(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_I_DB_REQ_LOAD_DATA : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_DB_REQ_LOAD_DATA; }
        Int64 type() { return (Int64)PacketType.E_I_DB_REQ_LOAD_DATA; }
        public UInt64 clientId_;
        public UInt64 oidAccountId_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, oidAccountId_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            oidAccountId_ = PacketUtil.decodeUInt64(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_I_DB_ANS_PARSE_DATA : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_DB_ANS_PARSE_DATA; }
        Int64 type() { return (Int64)PacketType.E_I_DB_ANS_PARSE_DATA; }
        public UInt64 clientId_;
        public string name_;
        public Byte result_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, name_);
            PacketUtil.encode(packet_, result_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            name_ = PacketUtil.decodestring(packet, ref offset);
            result_ = PacketUtil.decodeByte(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_I_LOGIN_NOTIFY_ID_LOADED : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_LOGIN_NOTIFY_ID_LOADED; }
        Int64 type() { return (Int64)PacketType.E_I_LOGIN_NOTIFY_ID_LOADED; }
        public UInt64 clientId_;
        public string name_;
        public Byte result_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, name_);
            PacketUtil.encode(packet_, result_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            name_ = PacketUtil.decodestring(packet, ref offset);
            result_ = PacketUtil.decodeByte(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_C_REQ_REGIST_CHATTING_NAME : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_C_REQ_REGIST_CHATTING_NAME; }
        Int64 type() { return (Int64)PacketType.E_C_REQ_REGIST_CHATTING_NAME; }
        public string name_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, name_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            name_ = PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_C_REQ_CHATTING : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_C_REQ_CHATTING; }
        Int64 type() { return (Int64)PacketType.E_C_REQ_CHATTING; }
        public string text_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, text_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            text_ = PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_S_ANS_CHATTING : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_CHATTING; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_CHATTING; }
        public string name_;
        public string text_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, name_);
            PacketUtil.encode(packet_, text_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            name_ = PacketUtil.decodestring(packet, ref offset);
            text_ = PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_S_ANS_NEW_USER_NOTIFY : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_NEW_USER_NOTIFY; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_NEW_USER_NOTIFY; }
        public string name_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, name_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            name_ = PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_S_ANS_USER_LIST : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_USER_LIST; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_USER_LIST; }

        public List<string> names_ = new List<string>();

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());

            PacketUtil.encode(packet_, (Int32)names_.Count);

            foreach (string name in names_)
            {
                PacketUtil.encode(packet_, name);
            }
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            Int32 count = PacketUtil.decodeInt32(packet, ref offset);

            names_.Clear();

            for (int i = 0; i < count; i++)
            {
                string name = PacketUtil.decodestring(packet, ref offset);
                names_.Add(name);
            }
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_S_ANS_EXIT_USER : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_EXIT_USER; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_EXIT_USER; }
        public string name_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, name_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            name_ = PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_C_REQ_CHAT_EXIT : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_C_REQ_CHAT_EXIT; }
        Int64 type() { return (Int64)PacketType.E_C_REQ_CHAT_EXIT; }
        //public string name_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
           // PacketUtil.encode(packet_, name_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
           // name_ = PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_S_ANS_CREATECHARACTER_OPEN : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_CREATECHARACTER_OPEN; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_CREATECHARACTER_OPEN; }
        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
}
```

## DummyClient\Source\PacketGen\PacketFactory.cs
```cs
癤퓎sing System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.IO;
using System.Net.Sockets;

namespace DummyClient
{
    public static class PacketFactory
    {
        public static PacketInterface getPacket(Int64 packetType)
        {
            switch ((PacketType)packetType)
            {
                case PacketType.E_C_REQ_EXIT: return new PK_C_REQ_EXIT();
                case PacketType.E_S_ANS_EXIT: return new PK_S_ANS_EXIT();
                case PacketType.E_I_NOTIFY_TERMINAL: return new PK_I_NOTIFY_TERMINAL();
                case PacketType.E_C_NOTIFY_HEARTBEAT: return new PK_C_NOTIFY_HEARTBEAT();
                case PacketType.E_C_REQ_ID_PW: return new PK_C_REQ_ID_PW();
                case PacketType.E_S_ANS_ID_PW_FAIL: return new PK_S_ANS_ID_PW_FAIL();
                case PacketType.E_S_ANS_ID_PW_SUCCESS: return new PK_S_ANS_ID_PW_SUCCESS();
                case PacketType.E_I_DB_REQ_ID_PW: return new PK_I_DB_REQ_ID_PW();
                case PacketType.E_I_DB_ANS_ID_PW: return new PK_I_DB_ANS_ID_PW();
                case PacketType.E_I_CHTTING_NOTIFY_ID: return new PK_I_CHTTING_NOTIFY_ID();
                case PacketType.E_I_DB_REQ_LOAD_DATA: return new PK_I_DB_REQ_LOAD_DATA();
                case PacketType.E_I_DB_ANS_PARSE_DATA: return new PK_I_DB_ANS_PARSE_DATA();
                case PacketType.E_I_LOGIN_NOTIFY_ID_LOADED: return new PK_I_LOGIN_NOTIFY_ID_LOADED();
                case PacketType.E_C_REQ_REGIST_CHATTING_NAME: return new PK_C_REQ_REGIST_CHATTING_NAME();
                case PacketType.E_C_REQ_CHATTING: return new PK_C_REQ_CHATTING();
                case PacketType.E_S_ANS_CHATTING: return new PK_S_ANS_CHATTING();
                case PacketType.E_S_ANS_NEW_USER_NOTIFY:return new PK_S_ANS_NEW_USER_NOTIFY();
                case PacketType.E_S_ANS_USER_LIST:return new PK_S_ANS_USER_LIST();
                case PacketType.E_S_ANS_EXIT_USER:return new PK_S_ANS_EXIT_USER();
                case PacketType.E_C_REQ_CHAT_EXIT:return new PK_C_REQ_CHAT_EXIT();
                case PacketType.E_S_ANS_CREATECHARACTER_OPEN: return new PK_S_ANS_CREATECHARACTER_OPEN();
            }
            return null;
        }
    }
}
```

## DummyClient\Source\PacketGen\PacketHeader.cs
```cs
癤퓎sing System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.IO;

namespace DummyClient
{
    static class PacketMakeDate
    {
        static public string stamp()
        {
            return "2025/03/01 12:13:55";
        }
    }
    enum PacketType : long
    {
        E_C_REQ_EXIT = 128,
        E_S_ANS_EXIT = 129,
        E_I_NOTIFY_TERMINAL = 130,
        E_C_NOTIFY_HEARTBEAT = 131,
        E_C_REQ_ID_PW = 132,
        E_S_ANS_ID_PW_FAIL = 133,
        E_S_ANS_ID_PW_SUCCESS = 134,
        E_I_DB_REQ_ID_PW = 135,
        E_I_DB_ANS_ID_PW = 136,
        E_I_CHTTING_NOTIFY_ID = 137,
        E_I_DB_REQ_LOAD_DATA = 138,
        E_I_DB_ANS_PARSE_DATA = 139,
        E_I_LOGIN_NOTIFY_ID_LOADED = 140,
        E_C_REQ_REGIST_CHATTING_NAME = 141,
        E_C_REQ_CHATTING = 142,
        E_S_ANS_CHATTING = 143,
        E_S_ANS_NEW_USER_NOTIFY = 144,
        E_S_ANS_USER_LIST = 145,
        E_S_ANS_EXIT_USER = 146,
        E_C_REQ_CHAT_EXIT=147,
        E_S_ANS_CREATECHARACTER_OPEN=148,
        E_C_REQ_CREATECHARACTER=149,

    }
};
```

## DummyClient\Source\PacketProcess.cs
```cs
癤퓎sing System.Windows.Forms;

namespace DummyClient
{
    internal abstract class PacketProcess
    {
        public bool defaultRun(PacketInterface packet)
        {
            PacketType type = (PacketType)packet.type();

            return false;
        }

        public abstract void run(PacketInterface packet);
    }
}
```

## DummyClient\Source\ProgramState.cs
```cs
癤퓆amespace DummyClient
{
    internal enum PROGRAM_STATE
    {
        LOGIN,
        CHATTING,
        CREATECHARACTER,
        MAX,
    }

    internal class ProgramState
    {
        private PROGRAM_STATE state_;
        private FormState formState_ = null;
        private string name_;

        public delegate void putMessageDele(string msg);
        public event putMessageDele putMessage_;

        private void changeState()
        {
            switch (state_)
            {
                case PROGRAM_STATE.LOGIN:
                    formState_ = new LoginFormState();
                    break;

                case PROGRAM_STATE.CHATTING:
                    formState_ = new ChattingFormState();
                    break;

                case PROGRAM_STATE.CREATECHARACTER:
                    formState_=new CreateCharacterState();
                    break;
            }
        }

        public void setState(PROGRAM_STATE state, string ip, uint port)
        {
            if (formState_ != null)
                formState_.close();

            state_ = state;
            this.changeState();
            formState_.open(ip, port);
        }

        public void setName(string name)
        {
            name_ = name;
        }

        public string name()
        {
            return name_;
        }

        public void sendPacket(PacketInterface packet)
        {
            this.formState_.sendPacket(ref packet);
        }

        public void putMessage(string msg)
        {
            putMessage_(msg);
        }

        public void close()
        {
            this.formState_.close();
        }
    }
}
```

## LoginServer\LoginServer.cpp
```cpp
#include "stdafx.h"

class SystemReport : public Work
{
	void tick()
	{
		Monitoring &moniter = Monitoring::getInstance();
		SLog(L"### cpu usage : %2.2f%%, memory usage : %uByte", moniter.processCpuUsage(), moniter.processMemUsage());
	}
};

void serverProcess()
{
	shared_ptr<Server> server(new IOCPServer(new LoginProcess()));
	SystemReport systemReport;
	const int MONITOR_REPORTING_SEC = 1;
	TaskManager::getInstance().add(&systemReport, MONITOR_REPORTING_SEC, TICK_INFINTY);
	if (!server->run()) {
		SLog(L"! error: server start fail");
		return;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	shared_ptr<Thread> serverThread(new Thread(new thread_t(serverProcess), L"Server"));
	return 0;
}
```

## LoginServer\Server\LoginProcess.cpp
```cpp
#include "stdafx.h"
#include "LoginProcess.h"

LoginProcess::LoginProcess()
{
	this->registSubPacketFunc();
}

void LoginProcess::registSubPacketFunc()
{
#define INSERT_PACKET_PROCESS(type)		runFuncTable_.insert(make_pair(E_##type, &LoginProcess::##type))

	INSERT_PACKET_PROCESS(C_REQ_ID_PW);
	INSERT_PACKET_PROCESS(I_DB_ANS_ID_PW);
	INSERT_PACKET_PROCESS(I_LOGIN_NOTIFY_ID_LOADED);
}


void LoginProcess::C_REQ_ID_PW(Session *session, Packet *rowPacket)
{
	PK_C_REQ_ID_PW *packet = (PK_C_REQ_ID_PW *)rowPacket;

	PK_I_DB_REQ_ID_PW dbPacket;
	dbPacket.clientId_ = (UInt64)session->id();
	dbPacket.id_ = packet->id_;
	dbPacket.password_ = packet->password_;

	Terminal *terminal = _terminal.get(L"DBAgent");
	terminal->sendPacket(&dbPacket);
}

void LoginProcess::I_DB_ANS_ID_PW(Session *session, Packet *rowPacket)
{
	PK_I_DB_ANS_ID_PW *packet = (PK_I_DB_ANS_ID_PW  *)rowPacket;
	SLog(L"* id/ pw result = %d", packet->result_);

	Session *clientSession = _session_manager.session(packet->clientId_);
	if (clientSession == nullptr) {
		return;
	}

	const int authFail = 0;
	if (packet->result_ == authFail) {
		PK_S_ANS_ID_PW_FAIL ansPacket;
		clientSession->sendPacket(&ansPacket);
		return;
	}
	
	PK_I_CHTTING_NOTIFY_ID iPacket;
	iPacket.oidAccountId_ = packet->oidAccountId_;
	iPacket.clientId_ = packet->clientId_;
	Terminal *terminal = _terminal.get(L"ChattingServer");
	if (terminal == nullptr) {
		SLog(L"! Chatting Server terminal is not connected");
	}
	terminal->sendPacket(&iPacket);
}

void LoginProcess::I_LOGIN_NOTIFY_ID_LOADED(Session *session, Packet *rowPacket)
{
	PK_I_LOGIN_NOTIFY_ID_LOADED *packet = (PK_I_LOGIN_NOTIFY_ID_LOADED *)rowPacket;
	
	const int dataNull = 0;
	if (packet->result_ == dataNull) {
		return;
	}
	Session *clientSession = _session_manager.session(packet->clientId_);
	if (clientSession == nullptr) {
		return;
	}
	Terminal *terminal = _terminal.get(L"ChattingServer");
	if (terminal == nullptr) {
		SLog(L"! Chatting Server terminal is not connected");
	}
	PK_S_ANS_ID_PW_SUCCESS ansPacket;
	ansPacket.ip_ = terminal->ip();
	ansPacket.port_ = terminal->port();
	ansPacket.name_ = packet->name_;

	SLog(L"* loaded [%S] user name, from [%s]", ansPacket.name_.c_str(), session->clientAddress().c_str());
	clientSession->sendPacket(&ansPacket);
}
```

## LoginServer\Server\LoginProcess.h
```h
#pragma once
#include "stdafx.h"

class LoginProcess : public ContentsProcess
{
public:
	LoginProcess();
private:
	void registSubPacketFunc();
	static void C_REQ_ID_PW(Session *session, Packet *rowPacket);
	static void I_DB_ANS_ID_PW(Session *session, Packet *rowPacket);
	static void I_LOGIN_NOTIFY_ID_LOADED(Session *session, Packet *rowPacket);
};
```

## LoginServer\stdafx.cpp
```cpp
// stdafx.cpp : source file that includes just the standard includes
// LoginServer.pch will be the pre-compiled header
// stdafx.obj will contain the pre-compiled type information

#include "stdafx.h"

// TODO: reference any additional headers you need in STDAFX.H
// and not in this file
```

## LoginServer\stdafx.h
```h
// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently, but
// are changed infrequently
//

#pragma once

#include "targetver.h"

#include <stdio.h>
#include <tchar.h>


// 종속 serverLibrary
// TODO: reference additional headers your program requires here
#include "ServerLibrary.h"
#include "./Server/LoginProcess.h"
```

## LoginServer\targetver.h
```h
#pragma once

// Including SDKDDKVer.h defines the highest available Windows platform.

// If you wish to build your application for a previous Windows platform, include WinSDKVer.h and
// set the _WIN32_WINNT macro to the platform you wish to support before including SDKDDKVer.h.

#include <SDKDDKVer.h>
```

## LoginServer\x64\Debug\LoginServer.tlog\LoginServer.lastbuildstate
```lastbuildstate
PlatformToolSet=v143:VCToolArchitecture=Native64Bit:VCToolsVersion=14.41.34120:TargetPlatformVersion=10.0.26100.0:
Debug|x64|C:\github\GameServer_Programming\ServerLibrary\|
```

## ServerLibrary\.vs\ServerCore\v17\DocumentLayout.backup.json
```json
{
  "Version": 1,
  "WorkspaceRootPath": "C:\\github\\GameServer_Programming\\ServerLibrary\\",
  "Documents": [
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketFactory.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Packet\\PacketFactory.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketHeader.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Packet\\PacketHeader.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{1515F39A-0956-4F01-A163-2960DC0B49F3}|..\\LoginServer\\LoginServer.vcxproj|C:\\github\\GameServer_Programming\\LoginServer\\Server\\LoginProcess.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{E88085C2-D120-4E12-AA30-C848FF4B36AB}|..\\DBAgent\\DBAgent.vcxproj|C:\\github\\GameServer_Programming\\DBAgent\\Query\\QI_DB_REQ_ID_PW.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketClass.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Packet\\PacketClass.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\ADODatabase.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Database\\ADODatabase.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\ADODatabase.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Database\\ADODatabase.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{E88085C2-D120-4E12-AA30-C848FF4B36AB}|..\\DBAgent\\DBAgent.vcxproj|C:\\github\\GameServer_Programming\\DBAgent\\DBAgentProcess.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Contents\\ContentsProcess.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Contents\\ContentsProcess.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\Server\\UserManager.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\Server\\User.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\Server\\ChattingProcess.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketObfuscation.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Packet\\PacketObfuscation.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\Package.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Packet\\Package.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\ProgramValidation.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\ProgramValidation.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\ChattingServer.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\stdafx.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\Server\\ChattingProcess.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{E88085C2-D120-4E12-AA30-C848FF4B36AB}|..\\DBAgent\\DBAgent.vcxproj|C:\\github\\GameServer_Programming\\DBAgent\\Query\\QI_DB_REQ_LOAD_DATA.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{E88085C2-D120-4E12-AA30-C848FF4B36AB}|..\\DBAgent\\DBAgent.vcxproj|C:\\github\\GameServer_Programming\\DBAgent\\main.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{1515F39A-0956-4F01-A163-2960DC0B49F3}|..\\LoginServer\\LoginServer.vcxproj|C:\\github\\GameServer_Programming\\LoginServer\\Server\\LoginProcess.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{1515F39A-0956-4F01-A163-2960DC0B49F3}|..\\LoginServer\\LoginServer.vcxproj|C:\\github\\GameServer_Programming\\LoginServer\\LoginServer.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\ServerLibrary.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:ServerLibrary.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Shutdown.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Shutdown.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Shutdown.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Shutdown.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\CONTENTS\\CONTENTSPROCESS.H||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:CONTENTS\\CONTENTSPROCESS.H||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\QueryStatement.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Database\\QueryStatement.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\Query.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Database\\Query.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\Database.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Database\\Database.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Iocp\\IOCPSession.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Iocp\\IOCPSession.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Iocp\\IOCPServer.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Iocp\\IOCPServer.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketObfuscation.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Packet\\PacketObfuscation.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Terminal\\TerminalSession.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Terminal\\TerminalSession.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Terminal\\Terminal.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Terminal\\Terminal.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Server.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Server.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Session.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Session.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Session.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Session.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\SessionManager.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\SessionManager.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\SessionManager.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\SessionManager.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\WinSocket.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\WinSocket.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Clock.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Clock.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Clock.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Clock.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\GameObject.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\GameObject.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Lock.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Lock.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Lock.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Lock.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Logger.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Logger.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Logger.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Logger.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Memory_LowFragmentationHeap.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Memory_LowFragmentationHeap.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\MemoryLeak.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\MemoryLeak.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Minidump.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Minidump.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Minidump.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Minidump.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Monitoring.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Monitoring.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Table.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Table.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Task.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Task.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Task.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Task.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Thread.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Thread.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Thread.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Thread.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Type.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Type.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Util.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Util.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\ThreadJobQueue.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\ThreadJobQueue.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxml.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\tinyXml\\tinyxml.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxml.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\tinyXml\\tinyxml.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\targetver.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\csv_parser\\csv_parser.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\csv_parser\\csv_parser.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\config.xml||{FA3CD31E-987B-443A-9B81-186104E8DAC1}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\stdafx.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinystr.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\tinyXml\\tinystr.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\csv_parser\\csv_parser.hpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\csv_parser\\csv_parser.hpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxmlparser.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\tinyXml\\tinyxmlparser.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{1515F39A-0956-4F01-A163-2960DC0B49F3}|..\\LoginServer\\LoginServer.vcxproj|C:\\github\\GameServer_Programming\\LoginServer\\config.xml||{FA3CD31E-987B-443A-9B81-186104E8DAC1}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{E88085C2-D120-4E12-AA30-C848FF4B36AB}|..\\DBAgent\\DBAgent.vcxproj|C:\\github\\GameServer_Programming\\DBAgent\\config.xml||{FA3CD31E-987B-443A-9B81-186104E8DAC1}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{E88085C2-D120-4E12-AA30-C848FF4B36AB}|..\\DBAgent\\DBAgent.vcxproj|C:\\github\\GameServer_Programming\\DBAgent\\stdafx.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{1515F39A-0956-4F01-A163-2960DC0B49F3}|..\\LoginServer\\LoginServer.vcxproj|C:\\github\\GameServer_Programming\\LoginServer\\targetver.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{1515F39A-0956-4F01-A163-2960DC0B49F3}|..\\LoginServer\\LoginServer.vcxproj|C:\\github\\GameServer_Programming\\LoginServer\\stdafx.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{A2FE74E1-B743-11D0-AE1A-00A0C90FFFC3}|\u003CMiscFiles\u003E|C:\\github\\GameServer_Programming\\LoginServer\\pch.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{A2FE74E1-B743-11D0-AE1A-00A0C90FFFC3}|\u003CMiscFiles\u003E|C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xhash||{3B902123-F8A7-4915-9F01-361F908088D0}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{A2FE74E1-B743-11D0-AE1A-00A0C90FFFC3}|\u003CMiscFiles\u003E|C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xutility||{3B902123-F8A7-4915-9F01-361F908088D0}"
    }
  ],
  "DocumentGroupContainers": [
    {
      "Orientation": 0,
      "VerticalTabListWidth": 256,
      "DocumentGroups": [
        {
          "DockedWidth": 200,
          "SelectedChildIndex": 3,
          "Children": [
            {
              "$type": "Document",
              "DocumentIndex": 1,
              "Title": "PacketHeader.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketHeader.h",
              "RelativeDocumentMoniker": "Net\\Packet\\PacketHeader.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketHeader.h",
              "RelativeToolTip": "Net\\Packet\\PacketHeader.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABgAAAAaAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-17T10:08:49.845Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 6,
              "Title": "ADODatabase.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\ADODatabase.h",
              "RelativeDocumentMoniker": "Database\\ADODatabase.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\ADODatabase.h",
              "RelativeToolTip": "Database\\ADODatabase.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAA8AAAABAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T09:32:10.781Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 5,
              "Title": "ADODatabase.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\ADODatabase.cpp",
              "RelativeDocumentMoniker": "Database\\ADODatabase.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\ADODatabase.cpp",
              "RelativeToolTip": "Database\\ADODatabase.cpp",
              "ViewState": "AgIAAEgAAAAAAAAAAAAAAFEAAAALAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-08T08:47:11.348Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 0,
              "Title": "PacketFactory.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketFactory.h",
              "RelativeDocumentMoniker": "Net\\Packet\\PacketFactory.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketFactory.h",
              "RelativeToolTip": "Net\\Packet\\PacketFactory.h",
              "ViewState": "AgIAAAwAAAAAAAAAAAAAACEAAAAJAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-17T10:07:05.043Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 4,
              "Title": "PacketClass.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketClass.h",
              "RelativeDocumentMoniker": "Net\\Packet\\PacketClass.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketClass.h",
              "RelativeToolTip": "Net\\Packet\\PacketClass.h",
              "ViewState": "AgIAADYBAAAAAAAAAAAAAM0AAAAZAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-17T10:09:57.755Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 3,
              "Title": "QI_DB_REQ_ID_PW.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DBAgent\\Query\\QI_DB_REQ_ID_PW.h",
              "RelativeDocumentMoniker": "..\\DBAgent\\Query\\QI_DB_REQ_ID_PW.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\DBAgent\\Query\\QI_DB_REQ_ID_PW.h",
              "RelativeToolTip": "..\\DBAgent\\Query\\QI_DB_REQ_ID_PW.h",
              "ViewState": "AgIAAAkAAAAAAAAAAAAAAA4AAAA9AAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-03-05T13:05:21.978Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 2,
              "Title": "LoginProcess.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\LoginServer\\Server\\LoginProcess.cpp",
              "RelativeDocumentMoniker": "..\\LoginServer\\Server\\LoginProcess.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\LoginServer\\Server\\LoginProcess.cpp",
              "RelativeToolTip": "..\\LoginServer\\Server\\LoginProcess.cpp",
              "ViewState": "AgIAABgAAAAAAAAAAAAAABEAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-01-29T09:29:53.33Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 7,
              "Title": "DBAgentProcess.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DBAgent\\DBAgentProcess.cpp",
              "RelativeDocumentMoniker": "..\\DBAgent\\DBAgentProcess.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\DBAgent\\DBAgentProcess.cpp",
              "RelativeToolTip": "..\\DBAgent\\DBAgentProcess.cpp",
              "ViewState": "AgIAAAkAAAAAAAAAAAAAABMAAAA8AAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-03-04T15:49:10.709Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 8,
              "Title": "ContentsProcess.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Contents\\ContentsProcess.cpp",
              "RelativeDocumentMoniker": "Contents\\ContentsProcess.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Contents\\ContentsProcess.cpp",
              "RelativeToolTip": "Contents\\ContentsProcess.cpp",
              "ViewState": "AgIAAFEAAAAAAAAAAAAAAF4AAABLAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-01-23T09:50:33.079Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 9,
              "Title": "UserManager.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\Server\\UserManager.h",
              "RelativeDocumentMoniker": "..\\ChattingServer\\Server\\UserManager.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\Server\\UserManager.h",
              "RelativeToolTip": "..\\ChattingServer\\Server\\UserManager.h",
              "ViewState": "AgIAABUAAAAAAAAAAAAAACUAAAADAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-08T07:17:11.097Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 10,
              "Title": "User.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\Server\\User.h",
              "RelativeDocumentMoniker": "..\\ChattingServer\\Server\\User.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\Server\\User.h",
              "RelativeToolTip": "..\\ChattingServer\\Server\\User.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABMAAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-08T07:16:04.816Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 11,
              "Title": "ChattingProcess.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\Server\\ChattingProcess.cpp",
              "RelativeDocumentMoniker": "..\\ChattingServer\\Server\\ChattingProcess.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\Server\\ChattingProcess.cpp",
              "RelativeToolTip": "..\\ChattingServer\\Server\\ChattingProcess.cpp",
              "ViewState": "AgIAAGoAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-08T07:07:44.527Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 13,
              "Title": "Package.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\Package.h",
              "RelativeDocumentMoniker": "Net\\Packet\\Package.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\Package.h",
              "RelativeToolTip": "Net\\Packet\\Package.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAoAAAAqAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T09:52:32.638Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 14,
              "Title": "ProgramValidation.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\ProgramValidation.h",
              "RelativeDocumentMoniker": "Util\\ProgramValidation.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\ProgramValidation.h",
              "RelativeToolTip": "Util\\ProgramValidation.h",
              "ViewState": "AgIAAAkAAAAAAAAAAAAgwBgAAAAaAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T09:39:08.963Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 15,
              "Title": "ChattingServer.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\ChattingServer.cpp",
              "RelativeDocumentMoniker": "..\\ChattingServer\\ChattingServer.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\ChattingServer.cpp",
              "RelativeToolTip": "..\\ChattingServer\\ChattingServer.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAQAAAAMAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-08T07:00:40.383Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 16,
              "Title": "stdafx.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\stdafx.cpp",
              "RelativeDocumentMoniker": "..\\ChattingServer\\stdafx.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\stdafx.cpp",
              "RelativeToolTip": "..\\ChattingServer\\stdafx.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAcAAAAXAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-08T07:01:52.027Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 12,
              "Title": "PacketObfuscation.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketObfuscation.cpp",
              "RelativeDocumentMoniker": "Net\\Packet\\PacketObfuscation.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketObfuscation.cpp",
              "RelativeToolTip": "Net\\Packet\\PacketObfuscation.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAYAAAAYAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-03-05T13:01:21.008Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 17,
              "Title": "ChattingProcess.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\Server\\ChattingProcess.h",
              "RelativeDocumentMoniker": "..\\ChattingServer\\Server\\ChattingProcess.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\Server\\ChattingProcess.h",
              "RelativeToolTip": "..\\ChattingServer\\Server\\ChattingProcess.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABAAAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-08T07:04:03.833Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 18,
              "Title": "QI_DB_REQ_LOAD_DATA.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DBAgent\\Query\\QI_DB_REQ_LOAD_DATA.h",
              "RelativeDocumentMoniker": "..\\DBAgent\\Query\\QI_DB_REQ_LOAD_DATA.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\DBAgent\\Query\\QI_DB_REQ_LOAD_DATA.h",
              "RelativeToolTip": "..\\DBAgent\\Query\\QI_DB_REQ_LOAD_DATA.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAA8AAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-03-05T13:05:27.367Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 20,
              "Title": "LoginProcess.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\LoginServer\\Server\\LoginProcess.h",
              "RelativeDocumentMoniker": "..\\LoginServer\\Server\\LoginProcess.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\LoginServer\\Server\\LoginProcess.h",
              "RelativeToolTip": "..\\LoginServer\\Server\\LoginProcess.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAwAAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T09:30:08.514Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 21,
              "Title": "LoginServer.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\LoginServer\\LoginServer.cpp",
              "RelativeDocumentMoniker": "..\\LoginServer\\LoginServer.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\LoginServer\\LoginServer.cpp",
              "RelativeToolTip": "..\\LoginServer\\LoginServer.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAMAAAABAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-01-29T09:24:19.018Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 22,
              "Title": "ServerLibrary.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\ServerLibrary.h",
              "RelativeDocumentMoniker": "ServerLibrary.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\ServerLibrary.h",
              "RelativeToolTip": "ServerLibrary.h",
              "ViewState": "AgIAACcAAAAAAAAAAAAAAGUAAAArAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T08:24:45.855Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 23,
              "Title": "Shutdown.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Shutdown.cpp",
              "RelativeDocumentMoniker": "Shutdown.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Shutdown.cpp",
              "RelativeToolTip": "Shutdown.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAgAAAABAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-01-29T09:47:18.984Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 24,
              "Title": "Shutdown.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Shutdown.h",
              "RelativeDocumentMoniker": "Shutdown.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Shutdown.h",
              "RelativeToolTip": "Shutdown.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T09:47:12.512Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 25,
              "Title": "ContentsProcess.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Contents\\ContentsProcess.h",
              "RelativeDocumentMoniker": "Contents\\ContentsProcess.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Contents\\ContentsProcess.h",
              "RelativeToolTip": "Contents\\ContentsProcess.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAoAAAAKAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-23T09:44:32.255Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 26,
              "Title": "QueryStatement.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\QueryStatement.h",
              "RelativeDocumentMoniker": "Database\\QueryStatement.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\QueryStatement.h",
              "RelativeToolTip": "Database\\QueryStatement.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAB0AAAAYAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:49:39.936Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 19,
              "Title": "main.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DBAgent\\main.cpp",
              "RelativeDocumentMoniker": "..\\DBAgent\\main.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\DBAgent\\main.cpp",
              "RelativeToolTip": "..\\DBAgent\\main.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABIAAAABAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-06T06:28:51.427Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 27,
              "Title": "Query.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\Query.h",
              "RelativeDocumentMoniker": "Database\\Query.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\Query.h",
              "RelativeToolTip": "Database\\Query.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABQAAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:49:14.419Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 28,
              "Title": "Database.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\Database.h",
              "RelativeDocumentMoniker": "Database\\Database.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\Database.h",
              "RelativeToolTip": "Database\\Database.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAIAAAATAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-12T06:06:06.94Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 29,
              "Title": "IOCPSession.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\IOCP\\IOCPSession.cpp",
              "RelativeDocumentMoniker": "Net\\IOCP\\IOCPSession.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\IOCP\\IOCPSession.cpp",
              "RelativeToolTip": "Net\\IOCP\\IOCPSession.cpp",
              "ViewState": "AgIAAMAAAAAAAAAAAAAAAM8AAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-03-05T13:03:16.475Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 31,
              "Title": "PacketObfuscation.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketObfuscation.h",
              "RelativeDocumentMoniker": "Net\\Packet\\PacketObfuscation.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketObfuscation.h",
              "RelativeToolTip": "Net\\Packet\\PacketObfuscation.h",
              "ViewState": "AgIAAA8AAAAAAAAAAAAAAB0AAAA1AAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-03-05T13:02:53.305Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 32,
              "Title": "TerminalSession.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Terminal\\TerminalSession.cpp",
              "RelativeDocumentMoniker": "Net\\Terminal\\TerminalSession.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Terminal\\TerminalSession.cpp",
              "RelativeToolTip": "Net\\Terminal\\TerminalSession.cpp",
              "ViewState": "AgIAAAMAAAAAAAAAAAAAABcAAAABAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-03-05T13:00:44.208Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 34,
              "Title": "Server.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Server.cpp",
              "RelativeDocumentMoniker": "Net\\Server.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Server.cpp",
              "RelativeToolTip": "Net\\Server.cpp",
              "ViewState": "AgIAABIAAAAAAAAAAAAAACUAAABIAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-03-05T13:00:13.325Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 36,
              "Title": "Session.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Session.h",
              "RelativeDocumentMoniker": "Net\\Session.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Session.h",
              "RelativeToolTip": "Net\\Session.h",
              "ViewState": "AgIAAB4AAAAAAAAAAAAAACgAAAAPAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-03-05T12:59:59.978Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 37,
              "Title": "SessionManager.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\SessionManager.cpp",
              "RelativeDocumentMoniker": "Net\\SessionManager.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\SessionManager.cpp",
              "RelativeToolTip": "Net\\SessionManager.cpp",
              "ViewState": "AgIAAGwAAAAAAAAAAAAAAIAAAAAGAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-03-01T11:42:00.929Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 38,
              "Title": "SessionManager.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\SessionManager.h",
              "RelativeDocumentMoniker": "Net\\SessionManager.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\SessionManager.h",
              "RelativeToolTip": "Net\\SessionManager.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAcAAAA3AAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:50:26.828Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 30,
              "Title": "IOCPServer.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\IOCP\\IOCPServer.cpp",
              "RelativeDocumentMoniker": "Net\\IOCP\\IOCPServer.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\IOCP\\IOCPServer.cpp",
              "RelativeToolTip": "Net\\IOCP\\IOCPServer.cpp",
              "ViewState": "AgIAAJ8AAAAAAAAAAAAAAH0AAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-16T04:01:01.802Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 39,
              "Title": "WinSocket.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Winsocket.h",
              "RelativeDocumentMoniker": "Net\\Winsocket.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Winsocket.h",
              "RelativeToolTip": "Net\\Winsocket.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABEAAAAHAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-03-01T11:42:02.896Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 40,
              "Title": "Clock.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Clock.cpp",
              "RelativeDocumentMoniker": "Util\\Clock.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Clock.cpp",
              "RelativeToolTip": "Util\\Clock.cpp",
              "ViewState": "AgIAAF0AAAAAAAAAAAAAABcAAAADAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-06T07:51:06.732Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 41,
              "Title": "Clock.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Clock.h",
              "RelativeDocumentMoniker": "Util\\Clock.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Clock.h",
              "RelativeToolTip": "Util\\Clock.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAD8AAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T09:38:39.134Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 42,
              "Title": "GameObject.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\GameObject.h",
              "RelativeDocumentMoniker": "Util\\GameObject.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\GameObject.h",
              "RelativeToolTip": "Util\\GameObject.h",
              "ViewState": "AgIAABgAAAAAAAAAAAAAACcAAAAHAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-03-05T12:58:43.397Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 45,
              "Title": "Logger.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Logger.cpp",
              "RelativeDocumentMoniker": "Util\\Logger.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Logger.cpp",
              "RelativeToolTip": "Util\\Logger.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABYAAAAmAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-06T07:51:36.591Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 46,
              "Title": "Logger.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Logger.h",
              "RelativeDocumentMoniker": "Util\\Logger.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Logger.h",
              "RelativeToolTip": "Util\\Logger.h",
              "ViewState": "AgIAACEAAAAAAAAAAAAAAAcAAABSAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-28T17:03:08.281Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 47,
              "Title": "Memory_LowFragmentationHeap.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Memory_LowFragmentationHeap.h",
              "RelativeDocumentMoniker": "Util\\Memory_LowFragmentationHeap.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Memory_LowFragmentationHeap.h",
              "RelativeToolTip": "Util\\Memory_LowFragmentationHeap.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABgAAAADAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:52:10.5Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 33,
              "Title": "Terminal.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Terminal\\Terminal.cpp",
              "RelativeDocumentMoniker": "Net\\Terminal\\Terminal.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Terminal\\Terminal.cpp",
              "RelativeToolTip": "Net\\Terminal\\Terminal.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAADsAAAAWAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-12T08:33:23.215Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 48,
              "Title": "MemoryLeak.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\MemoryLeak.h",
              "RelativeDocumentMoniker": "Util\\MemoryLeak.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\MemoryLeak.h",
              "RelativeToolTip": "Util\\MemoryLeak.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAoAAAAGAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:52:17.42Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 35,
              "Title": "Session.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Session.cpp",
              "RelativeDocumentMoniker": "Net\\Session.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Session.cpp",
              "RelativeToolTip": "Net\\Session.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAACAAAAAbAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-06T07:50:02.425Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 49,
              "Title": "Minidump.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Minidump.cpp",
              "RelativeDocumentMoniker": "Util\\Minidump.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Minidump.cpp",
              "RelativeToolTip": "Util\\Minidump.cpp",
              "ViewState": "AgIAABsAAAAAAAAAAAAAACsAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-03-05T12:57:32.788Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 51,
              "Title": "Monitoring.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Monitoring.h",
              "RelativeDocumentMoniker": "Util\\Monitoring.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Monitoring.h",
              "RelativeToolTip": "Util\\Monitoring.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAADEAAAAeAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:52:43.592Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 52,
              "Title": "Table.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Table.h",
              "RelativeDocumentMoniker": "Util\\Table.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Table.h",
              "RelativeToolTip": "Util\\Table.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAACUAAAAFAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:53:11.545Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 53,
              "Title": "Task.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Task.cpp",
              "RelativeDocumentMoniker": "Util\\Task.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Task.cpp",
              "RelativeToolTip": "Util\\Task.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAGUAAAAkAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-06T07:53:22.451Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 54,
              "Title": "Task.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Task.h",
              "RelativeDocumentMoniker": "Util\\Task.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Task.h",
              "RelativeToolTip": "Util\\Task.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAADMAAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:53:31.045Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 55,
              "Title": "Thread.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Thread.cpp",
              "RelativeDocumentMoniker": "Util\\Thread.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Thread.cpp",
              "RelativeToolTip": "Util\\Thread.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAEwAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-06T07:53:38.486Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 44,
              "Title": "Lock.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Lock.h",
              "RelativeDocumentMoniker": "Util\\Lock.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Lock.h",
              "RelativeToolTip": "Util\\Lock.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T08:20:54.699Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 43,
              "Title": "Lock.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Lock.cpp",
              "RelativeDocumentMoniker": "Util\\Lock.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Lock.cpp",
              "RelativeToolTip": "Util\\Lock.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABIAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-01-29T09:14:54.386Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 56,
              "Title": "Thread.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Thread.h",
              "RelativeDocumentMoniker": "Util\\Thread.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Thread.h",
              "RelativeToolTip": "Util\\Thread.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAB8AAAAbAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-03-05T12:56:42.62Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 57,
              "Title": "Type.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Type.h",
              "RelativeDocumentMoniker": "Util\\Type.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Type.h",
              "RelativeToolTip": "Util\\Type.h",
              "ViewState": "AgIAAA8AAAAAAAAAAAAAACgAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:53:56.017Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 59,
              "Title": "ThreadJobQueue.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\ThreadJobQueue.h",
              "RelativeDocumentMoniker": "Util\\ThreadJobQueue.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\ThreadJobQueue.h",
              "RelativeToolTip": "Util\\ThreadJobQueue.h",
              "ViewState": "AgIAADwAAAAAAAAAAAAAAEsAAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-03-05T12:56:01.085Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 50,
              "Title": "Minidump.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Minidump.h",
              "RelativeDocumentMoniker": "Util\\Minidump.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Minidump.h",
              "RelativeToolTip": "Util\\Minidump.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAA4AAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:52:38.591Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 58,
              "Title": "Util.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Util.h",
              "RelativeDocumentMoniker": "Util\\Util.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Util.h",
              "RelativeToolTip": "Util\\Util.h",
              "ViewState": "AgIAAEgAAAAAAAAAAAAAAFYAAAABAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:54:06.985Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 67,
              "Title": "csv_parser.hpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\csv_parser\\csv_parser.hpp",
              "RelativeDocumentMoniker": "Util\\csv_parser\\csv_parser.hpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\csv_parser\\csv_parser.hpp",
              "RelativeToolTip": "Util\\csv_parser\\csv_parser.hpp",
              "ViewState": "AgIAAAAAAAAAAAAAAABhwAgAAAAQAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-16T04:01:00.752Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 76,
              "Title": "xutility",
              "DocumentMoniker": "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xutility",
              "RelativeDocumentMoniker": "..\\..\\..\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xutility",
              "ToolTip": "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xutility",
              "RelativeToolTip": "..\\..\\..\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xutility",
              "ViewState": "AgIAABgFAAAAAAAAAAAuwDAFAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.001001|",
              "WhenOpened": "2025-03-01T11:34:26.117Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 75,
              "Title": "xhash",
              "DocumentMoniker": "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xhash",
              "RelativeDocumentMoniker": "..\\..\\..\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xhash",
              "ToolTip": "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xhash",
              "RelativeToolTip": "..\\..\\..\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xhash",
              "ViewState": "AgIAAKwDAAAAAAAAAAAuwL0DAAAIAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.001001|",
              "WhenOpened": "2025-03-01T11:34:32.494Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 63,
              "Title": "csv_parser.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\csv_parser\\csv_parser.cpp",
              "RelativeDocumentMoniker": "Util\\csv_parser\\csv_parser.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\csv_parser\\csv_parser.cpp",
              "RelativeToolTip": "Util\\csv_parser\\csv_parser.cpp",
              "ViewState": "AgIAADIBAAAAAAAAAIBZwDgBAAArAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-16T04:00:59.139Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 66,
              "Title": "tinystr.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinystr.h",
              "RelativeDocumentMoniker": "Util\\tinyXml\\tinystr.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinystr.h",
              "RelativeToolTip": "Util\\tinyXml\\tinystr.h",
              "ViewState": "AgIAAKgAAAAAAAAAAAAYwLQAAAAUAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-16T04:01:02.723Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 61,
              "Title": "tinyxml.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxml.cpp",
              "RelativeDocumentMoniker": "Util\\tinyXml\\tinyxml.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxml.cpp",
              "RelativeToolTip": "Util\\tinyXml\\tinyxml.cpp",
              "ViewState": "AgIAADYAAAAAAAAAAAAawEYAAAAnAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-16T04:01:11.673Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 60,
              "Title": "tinyxml.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxml.h",
              "RelativeDocumentMoniker": "Util\\tinyXml\\tinyxml.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxml.h",
              "RelativeToolTip": "Util\\tinyXml\\tinyxml.h",
              "ViewState": "AgIAAP4BAAAAAAAAAAAawA4CAABMAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-16T04:01:14.062Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 69,
              "Title": "config.xml",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\LoginServer\\config.xml",
              "RelativeDocumentMoniker": "..\\LoginServer\\config.xml",
              "ToolTip": "C:\\github\\GameServer_Programming\\LoginServer\\config.xml",
              "RelativeToolTip": "..\\LoginServer\\config.xml",
              "ViewState": "AgIAAAAAAAAAAAAAAIBJwAQAAAAWAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.003576|",
              "WhenOpened": "2025-02-15T05:54:00.349Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 64,
              "Title": "config.xml",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\config.xml",
              "RelativeDocumentMoniker": "..\\ChattingServer\\config.xml",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\config.xml",
              "RelativeToolTip": "..\\ChattingServer\\config.xml",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAA0AAAANAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.003576|",
              "WhenOpened": "2025-02-15T05:52:47.057Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 62,
              "Title": "targetver.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\targetver.h",
              "RelativeDocumentMoniker": "..\\ChattingServer\\targetver.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\targetver.h",
              "RelativeToolTip": "..\\ChattingServer\\targetver.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-08T07:02:10.986Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 65,
              "Title": "stdafx.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\stdafx.h",
              "RelativeDocumentMoniker": "..\\ChattingServer\\stdafx.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\stdafx.h",
              "RelativeToolTip": "..\\ChattingServer\\stdafx.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAoAAAASAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-08T07:02:00.165Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 71,
              "Title": "stdafx.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DBAgent\\stdafx.h",
              "RelativeDocumentMoniker": "..\\DBAgent\\stdafx.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\DBAgent\\stdafx.h",
              "RelativeToolTip": "..\\DBAgent\\stdafx.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABAAAAAoAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-08T06:56:16.764Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 73,
              "Title": "stdafx.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\LoginServer\\stdafx.h",
              "RelativeDocumentMoniker": "..\\LoginServer\\stdafx.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\LoginServer\\stdafx.h",
              "RelativeToolTip": "..\\LoginServer\\stdafx.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T10:21:27.304Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 70,
              "Title": "config.xml",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DBAgent\\config.xml",
              "RelativeDocumentMoniker": "..\\DBAgent\\config.xml",
              "ToolTip": "C:\\github\\GameServer_Programming\\DBAgent\\config.xml",
              "RelativeToolTip": "..\\DBAgent\\config.xml",
              "ViewState": "AgIAAAAAAAAAAAAAACBjwAkAAAARAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.003576|",
              "WhenOpened": "2025-01-29T10:15:25.185Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 68,
              "Title": "tinyxmlparser.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxmlparser.cpp",
              "RelativeDocumentMoniker": "Util\\tinyXml\\tinyxmlparser.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxmlparser.cpp",
              "RelativeToolTip": "Util\\tinyXml\\tinyxmlparser.cpp",
              "ViewState": "AgIAAAACAAAAAAAAAAAqwA0CAAANAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-01-29T10:00:18.098Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 74,
              "Title": "pch.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\LoginServer\\pch.cpp",
              "RelativeDocumentMoniker": "..\\LoginServer\\pch.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\LoginServer\\pch.cpp",
              "RelativeToolTip": "..\\LoginServer\\pch.cpp",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-01-29T09:29:22.354Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 72,
              "Title": "targetver.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\LoginServer\\targetver.h",
              "RelativeDocumentMoniker": "..\\LoginServer\\targetver.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\LoginServer\\targetver.h",
              "RelativeToolTip": "..\\LoginServer\\targetver.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T09:28:42.604Z"
            }
          ]
        }
      ]
    }
  ]
}
```

## ServerLibrary\.vs\ServerCore\v17\DocumentLayout.json
```json
{
  "Version": 1,
  "WorkspaceRootPath": "C:\\github\\GameServer_Programming\\ServerLibrary\\",
  "Documents": [
    {
      "AbsoluteMoniker": "D:0:0:{1515F39A-0956-4F01-A163-2960DC0B49F3}|..\\LoginServer\\LoginServer.vcxproj|C:\\github\\GameServer_Programming\\LoginServer\\Server\\LoginProcess.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketFactory.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Packet\\PacketFactory.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketHeader.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Packet\\PacketHeader.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{E88085C2-D120-4E12-AA30-C848FF4B36AB}|..\\DBAgent\\DBAgent.vcxproj|C:\\github\\GameServer_Programming\\DBAgent\\Query\\QI_DB_REQ_ID_PW.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketClass.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Packet\\PacketClass.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\ADODatabase.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Database\\ADODatabase.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\ADODatabase.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Database\\ADODatabase.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{E88085C2-D120-4E12-AA30-C848FF4B36AB}|..\\DBAgent\\DBAgent.vcxproj|C:\\github\\GameServer_Programming\\DBAgent\\DBAgentProcess.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Contents\\ContentsProcess.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Contents\\ContentsProcess.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\Server\\UserManager.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\Server\\User.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\Server\\ChattingProcess.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketObfuscation.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Packet\\PacketObfuscation.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\Package.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Packet\\Package.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\ProgramValidation.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\ProgramValidation.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\ChattingServer.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\stdafx.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\Server\\ChattingProcess.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{E88085C2-D120-4E12-AA30-C848FF4B36AB}|..\\DBAgent\\DBAgent.vcxproj|C:\\github\\GameServer_Programming\\DBAgent\\Query\\QI_DB_REQ_LOAD_DATA.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{E88085C2-D120-4E12-AA30-C848FF4B36AB}|..\\DBAgent\\DBAgent.vcxproj|C:\\github\\GameServer_Programming\\DBAgent\\main.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{1515F39A-0956-4F01-A163-2960DC0B49F3}|..\\LoginServer\\LoginServer.vcxproj|C:\\github\\GameServer_Programming\\LoginServer\\Server\\LoginProcess.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{1515F39A-0956-4F01-A163-2960DC0B49F3}|..\\LoginServer\\LoginServer.vcxproj|C:\\github\\GameServer_Programming\\LoginServer\\LoginServer.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\ServerLibrary.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:ServerLibrary.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Shutdown.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Shutdown.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Shutdown.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Shutdown.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\CONTENTS\\CONTENTSPROCESS.H||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:CONTENTS\\CONTENTSPROCESS.H||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\QueryStatement.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Database\\QueryStatement.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\Query.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Database\\Query.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\Database.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Database\\Database.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Iocp\\IOCPSession.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Iocp\\IOCPSession.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Iocp\\IOCPServer.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Iocp\\IOCPServer.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketObfuscation.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Packet\\PacketObfuscation.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Terminal\\TerminalSession.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Terminal\\TerminalSession.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Terminal\\Terminal.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Terminal\\Terminal.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Server.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Server.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Session.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Session.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Session.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\Session.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\SessionManager.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\SessionManager.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\SessionManager.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\SessionManager.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\WinSocket.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Net\\WinSocket.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Clock.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Clock.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Clock.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Clock.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\GameObject.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\GameObject.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Lock.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Lock.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Lock.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Lock.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Logger.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Logger.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Logger.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Logger.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Memory_LowFragmentationHeap.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Memory_LowFragmentationHeap.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\MemoryLeak.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\MemoryLeak.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Minidump.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Minidump.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Minidump.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Minidump.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Monitoring.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Monitoring.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Table.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Table.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Task.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Task.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Task.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Task.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Thread.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Thread.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Thread.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Thread.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Type.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Type.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Util.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\Util.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\ThreadJobQueue.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\ThreadJobQueue.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxml.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\tinyXml\\tinyxml.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxml.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\tinyXml\\tinyxml.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\targetver.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\csv_parser\\csv_parser.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\csv_parser\\csv_parser.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\config.xml||{FA3CD31E-987B-443A-9B81-186104E8DAC1}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{D9687045-9147-4B36-816E-71C68E01C7EB}|..\\ChattingServer\\ChattingServer.vcxproj|C:\\github\\GameServer_Programming\\ChattingServer\\stdafx.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinystr.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\tinyXml\\tinystr.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\csv_parser\\csv_parser.hpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\csv_parser\\csv_parser.hpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxmlparser.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}",
      "RelativeMoniker": "D:0:0:{043F7836-D119-4491-88F1-DB6334219A32}|ServerLibrary.vcxproj|solutionrelative:Util\\tinyXml\\tinyxmlparser.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{1515F39A-0956-4F01-A163-2960DC0B49F3}|..\\LoginServer\\LoginServer.vcxproj|C:\\github\\GameServer_Programming\\LoginServer\\config.xml||{FA3CD31E-987B-443A-9B81-186104E8DAC1}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{E88085C2-D120-4E12-AA30-C848FF4B36AB}|..\\DBAgent\\DBAgent.vcxproj|C:\\github\\GameServer_Programming\\DBAgent\\config.xml||{FA3CD31E-987B-443A-9B81-186104E8DAC1}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{E88085C2-D120-4E12-AA30-C848FF4B36AB}|..\\DBAgent\\DBAgent.vcxproj|C:\\github\\GameServer_Programming\\DBAgent\\stdafx.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{1515F39A-0956-4F01-A163-2960DC0B49F3}|..\\LoginServer\\LoginServer.vcxproj|C:\\github\\GameServer_Programming\\LoginServer\\targetver.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{1515F39A-0956-4F01-A163-2960DC0B49F3}|..\\LoginServer\\LoginServer.vcxproj|C:\\github\\GameServer_Programming\\LoginServer\\stdafx.h||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{A2FE74E1-B743-11D0-AE1A-00A0C90FFFC3}|\u003CMiscFiles\u003E|C:\\github\\GameServer_Programming\\LoginServer\\pch.cpp||{D0E1A5C6-B359-4E41-9B60-3365922C2A22}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{A2FE74E1-B743-11D0-AE1A-00A0C90FFFC3}|\u003CMiscFiles\u003E|C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xhash||{3B902123-F8A7-4915-9F01-361F908088D0}"
    },
    {
      "AbsoluteMoniker": "D:0:0:{A2FE74E1-B743-11D0-AE1A-00A0C90FFFC3}|\u003CMiscFiles\u003E|C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xutility||{3B902123-F8A7-4915-9F01-361F908088D0}"
    }
  ],
  "DocumentGroupContainers": [
    {
      "Orientation": 0,
      "VerticalTabListWidth": 256,
      "DocumentGroups": [
        {
          "DockedWidth": 200,
          "SelectedChildIndex": 6,
          "Children": [
            {
              "$type": "Document",
              "DocumentIndex": 2,
              "Title": "PacketHeader.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketHeader.h",
              "RelativeDocumentMoniker": "Net\\Packet\\PacketHeader.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketHeader.h",
              "RelativeToolTip": "Net\\Packet\\PacketHeader.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABgAAAAaAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-17T10:08:49.845Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 6,
              "Title": "ADODatabase.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\ADODatabase.h",
              "RelativeDocumentMoniker": "Database\\ADODatabase.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\ADODatabase.h",
              "RelativeToolTip": "Database\\ADODatabase.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAA8AAAABAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T09:32:10.781Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 5,
              "Title": "ADODatabase.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\ADODatabase.cpp",
              "RelativeDocumentMoniker": "Database\\ADODatabase.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\ADODatabase.cpp",
              "RelativeToolTip": "Database\\ADODatabase.cpp",
              "ViewState": "AgIAAEgAAAAAAAAAAAAAAFEAAAALAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-08T08:47:11.348Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 1,
              "Title": "PacketFactory.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketFactory.h",
              "RelativeDocumentMoniker": "Net\\Packet\\PacketFactory.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketFactory.h",
              "RelativeToolTip": "Net\\Packet\\PacketFactory.h",
              "ViewState": "AgIAAAwAAAAAAAAAAAAAACEAAAAJAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-17T10:07:05.043Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 4,
              "Title": "PacketClass.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketClass.h",
              "RelativeDocumentMoniker": "Net\\Packet\\PacketClass.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketClass.h",
              "RelativeToolTip": "Net\\Packet\\PacketClass.h",
              "ViewState": "AgIAADYBAAAAAAAAAAAAAM0AAAAZAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-17T10:09:57.755Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 3,
              "Title": "QI_DB_REQ_ID_PW.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DBAgent\\Query\\QI_DB_REQ_ID_PW.h",
              "RelativeDocumentMoniker": "..\\DBAgent\\Query\\QI_DB_REQ_ID_PW.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\DBAgent\\Query\\QI_DB_REQ_ID_PW.h",
              "RelativeToolTip": "..\\DBAgent\\Query\\QI_DB_REQ_ID_PW.h",
              "ViewState": "AgIAAAkAAAAAAAAAAAAAAA4AAAA9AAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-03-05T13:05:21.978Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 0,
              "Title": "LoginProcess.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\LoginServer\\Server\\LoginProcess.cpp",
              "RelativeDocumentMoniker": "..\\LoginServer\\Server\\LoginProcess.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\LoginServer\\Server\\LoginProcess.cpp",
              "RelativeToolTip": "..\\LoginServer\\Server\\LoginProcess.cpp",
              "ViewState": "AgIAAA8AAAAAAAAAAAAAABEAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-01-29T09:29:53.33Z",
              "EditorCaption": ""
            },
            {
              "$type": "Document",
              "DocumentIndex": 7,
              "Title": "DBAgentProcess.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DBAgent\\DBAgentProcess.cpp",
              "RelativeDocumentMoniker": "..\\DBAgent\\DBAgentProcess.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\DBAgent\\DBAgentProcess.cpp",
              "RelativeToolTip": "..\\DBAgent\\DBAgentProcess.cpp",
              "ViewState": "AgIAAAkAAAAAAAAAAAAAABMAAAA8AAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-03-04T15:49:10.709Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 8,
              "Title": "ContentsProcess.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Contents\\ContentsProcess.cpp",
              "RelativeDocumentMoniker": "Contents\\ContentsProcess.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Contents\\ContentsProcess.cpp",
              "RelativeToolTip": "Contents\\ContentsProcess.cpp",
              "ViewState": "AgIAAFEAAAAAAAAAAAAAAF4AAABLAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-01-23T09:50:33.079Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 9,
              "Title": "UserManager.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\Server\\UserManager.h",
              "RelativeDocumentMoniker": "..\\ChattingServer\\Server\\UserManager.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\Server\\UserManager.h",
              "RelativeToolTip": "..\\ChattingServer\\Server\\UserManager.h",
              "ViewState": "AgIAABUAAAAAAAAAAAAAACUAAAADAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-08T07:17:11.097Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 10,
              "Title": "User.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\Server\\User.h",
              "RelativeDocumentMoniker": "..\\ChattingServer\\Server\\User.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\Server\\User.h",
              "RelativeToolTip": "..\\ChattingServer\\Server\\User.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABMAAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-08T07:16:04.816Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 11,
              "Title": "ChattingProcess.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\Server\\ChattingProcess.cpp",
              "RelativeDocumentMoniker": "..\\ChattingServer\\Server\\ChattingProcess.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\Server\\ChattingProcess.cpp",
              "RelativeToolTip": "..\\ChattingServer\\Server\\ChattingProcess.cpp",
              "ViewState": "AgIAAGoAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-08T07:07:44.527Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 13,
              "Title": "Package.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\Package.h",
              "RelativeDocumentMoniker": "Net\\Packet\\Package.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\Package.h",
              "RelativeToolTip": "Net\\Packet\\Package.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAoAAAAqAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T09:52:32.638Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 14,
              "Title": "ProgramValidation.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\ProgramValidation.h",
              "RelativeDocumentMoniker": "Util\\ProgramValidation.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\ProgramValidation.h",
              "RelativeToolTip": "Util\\ProgramValidation.h",
              "ViewState": "AgIAAAkAAAAAAAAAAAAgwBgAAAAaAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T09:39:08.963Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 15,
              "Title": "ChattingServer.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\ChattingServer.cpp",
              "RelativeDocumentMoniker": "..\\ChattingServer\\ChattingServer.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\ChattingServer.cpp",
              "RelativeToolTip": "..\\ChattingServer\\ChattingServer.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAQAAAAMAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-08T07:00:40.383Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 16,
              "Title": "stdafx.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\stdafx.cpp",
              "RelativeDocumentMoniker": "..\\ChattingServer\\stdafx.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\stdafx.cpp",
              "RelativeToolTip": "..\\ChattingServer\\stdafx.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAcAAAAXAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-08T07:01:52.027Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 12,
              "Title": "PacketObfuscation.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketObfuscation.cpp",
              "RelativeDocumentMoniker": "Net\\Packet\\PacketObfuscation.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketObfuscation.cpp",
              "RelativeToolTip": "Net\\Packet\\PacketObfuscation.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAYAAAAYAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-03-05T13:01:21.008Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 17,
              "Title": "ChattingProcess.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\Server\\ChattingProcess.h",
              "RelativeDocumentMoniker": "..\\ChattingServer\\Server\\ChattingProcess.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\Server\\ChattingProcess.h",
              "RelativeToolTip": "..\\ChattingServer\\Server\\ChattingProcess.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABAAAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-08T07:04:03.833Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 18,
              "Title": "QI_DB_REQ_LOAD_DATA.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DBAgent\\Query\\QI_DB_REQ_LOAD_DATA.h",
              "RelativeDocumentMoniker": "..\\DBAgent\\Query\\QI_DB_REQ_LOAD_DATA.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\DBAgent\\Query\\QI_DB_REQ_LOAD_DATA.h",
              "RelativeToolTip": "..\\DBAgent\\Query\\QI_DB_REQ_LOAD_DATA.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAA8AAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-03-05T13:05:27.367Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 20,
              "Title": "LoginProcess.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\LoginServer\\Server\\LoginProcess.h",
              "RelativeDocumentMoniker": "..\\LoginServer\\Server\\LoginProcess.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\LoginServer\\Server\\LoginProcess.h",
              "RelativeToolTip": "..\\LoginServer\\Server\\LoginProcess.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAwAAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T09:30:08.514Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 21,
              "Title": "LoginServer.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\LoginServer\\LoginServer.cpp",
              "RelativeDocumentMoniker": "..\\LoginServer\\LoginServer.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\LoginServer\\LoginServer.cpp",
              "RelativeToolTip": "..\\LoginServer\\LoginServer.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAMAAAABAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-01-29T09:24:19.018Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 22,
              "Title": "ServerLibrary.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\ServerLibrary.h",
              "RelativeDocumentMoniker": "ServerLibrary.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\ServerLibrary.h",
              "RelativeToolTip": "ServerLibrary.h",
              "ViewState": "AgIAACcAAAAAAAAAAAAAAGUAAAArAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T08:24:45.855Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 23,
              "Title": "Shutdown.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Shutdown.cpp",
              "RelativeDocumentMoniker": "Shutdown.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Shutdown.cpp",
              "RelativeToolTip": "Shutdown.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAgAAAABAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-01-29T09:47:18.984Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 24,
              "Title": "Shutdown.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Shutdown.h",
              "RelativeDocumentMoniker": "Shutdown.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Shutdown.h",
              "RelativeToolTip": "Shutdown.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T09:47:12.512Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 25,
              "Title": "ContentsProcess.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Contents\\ContentsProcess.h",
              "RelativeDocumentMoniker": "Contents\\ContentsProcess.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Contents\\ContentsProcess.h",
              "RelativeToolTip": "Contents\\ContentsProcess.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAoAAAAKAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-23T09:44:32.255Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 26,
              "Title": "QueryStatement.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\QueryStatement.h",
              "RelativeDocumentMoniker": "Database\\QueryStatement.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\QueryStatement.h",
              "RelativeToolTip": "Database\\QueryStatement.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAB0AAAAYAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:49:39.936Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 19,
              "Title": "main.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DBAgent\\main.cpp",
              "RelativeDocumentMoniker": "..\\DBAgent\\main.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\DBAgent\\main.cpp",
              "RelativeToolTip": "..\\DBAgent\\main.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABIAAAABAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-06T06:28:51.427Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 27,
              "Title": "Query.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\Query.h",
              "RelativeDocumentMoniker": "Database\\Query.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\Query.h",
              "RelativeToolTip": "Database\\Query.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABQAAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:49:14.419Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 28,
              "Title": "Database.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\Database.h",
              "RelativeDocumentMoniker": "Database\\Database.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Database\\Database.h",
              "RelativeToolTip": "Database\\Database.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAIAAAATAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-12T06:06:06.94Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 29,
              "Title": "IOCPSession.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\IOCP\\IOCPSession.cpp",
              "RelativeDocumentMoniker": "Net\\IOCP\\IOCPSession.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\IOCP\\IOCPSession.cpp",
              "RelativeToolTip": "Net\\IOCP\\IOCPSession.cpp",
              "ViewState": "AgIAAMAAAAAAAAAAAAAAAM8AAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-03-05T13:03:16.475Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 31,
              "Title": "PacketObfuscation.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketObfuscation.h",
              "RelativeDocumentMoniker": "Net\\Packet\\PacketObfuscation.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Packet\\PacketObfuscation.h",
              "RelativeToolTip": "Net\\Packet\\PacketObfuscation.h",
              "ViewState": "AgIAAA8AAAAAAAAAAAAAAB0AAAA1AAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-03-05T13:02:53.305Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 32,
              "Title": "TerminalSession.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Terminal\\TerminalSession.cpp",
              "RelativeDocumentMoniker": "Net\\Terminal\\TerminalSession.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Terminal\\TerminalSession.cpp",
              "RelativeToolTip": "Net\\Terminal\\TerminalSession.cpp",
              "ViewState": "AgIAAAMAAAAAAAAAAAAAABcAAAABAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-03-05T13:00:44.208Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 34,
              "Title": "Server.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Server.cpp",
              "RelativeDocumentMoniker": "Net\\Server.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Server.cpp",
              "RelativeToolTip": "Net\\Server.cpp",
              "ViewState": "AgIAABIAAAAAAAAAAAAAACUAAABIAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-03-05T13:00:13.325Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 36,
              "Title": "Session.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Session.h",
              "RelativeDocumentMoniker": "Net\\Session.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Session.h",
              "RelativeToolTip": "Net\\Session.h",
              "ViewState": "AgIAAB4AAAAAAAAAAAAAACgAAAAPAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-03-05T12:59:59.978Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 37,
              "Title": "SessionManager.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\SessionManager.cpp",
              "RelativeDocumentMoniker": "Net\\SessionManager.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\SessionManager.cpp",
              "RelativeToolTip": "Net\\SessionManager.cpp",
              "ViewState": "AgIAAGwAAAAAAAAAAAAAAIAAAAAGAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-03-01T11:42:00.929Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 38,
              "Title": "SessionManager.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\SessionManager.h",
              "RelativeDocumentMoniker": "Net\\SessionManager.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\SessionManager.h",
              "RelativeToolTip": "Net\\SessionManager.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAcAAAA3AAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:50:26.828Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 30,
              "Title": "IOCPServer.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\IOCP\\IOCPServer.cpp",
              "RelativeDocumentMoniker": "Net\\IOCP\\IOCPServer.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\IOCP\\IOCPServer.cpp",
              "RelativeToolTip": "Net\\IOCP\\IOCPServer.cpp",
              "ViewState": "AgIAAJ8AAAAAAAAAAAAAAH0AAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-16T04:01:01.802Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 39,
              "Title": "WinSocket.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Winsocket.h",
              "RelativeDocumentMoniker": "Net\\Winsocket.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Winsocket.h",
              "RelativeToolTip": "Net\\Winsocket.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABEAAAAHAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-03-01T11:42:02.896Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 40,
              "Title": "Clock.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Clock.cpp",
              "RelativeDocumentMoniker": "Util\\Clock.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Clock.cpp",
              "RelativeToolTip": "Util\\Clock.cpp",
              "ViewState": "AgIAAF0AAAAAAAAAAAAAABcAAAADAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-06T07:51:06.732Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 41,
              "Title": "Clock.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Clock.h",
              "RelativeDocumentMoniker": "Util\\Clock.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Clock.h",
              "RelativeToolTip": "Util\\Clock.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAD8AAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T09:38:39.134Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 42,
              "Title": "GameObject.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\GameObject.h",
              "RelativeDocumentMoniker": "Util\\GameObject.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\GameObject.h",
              "RelativeToolTip": "Util\\GameObject.h",
              "ViewState": "AgIAABgAAAAAAAAAAAAAACcAAAAHAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-03-05T12:58:43.397Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 45,
              "Title": "Logger.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Logger.cpp",
              "RelativeDocumentMoniker": "Util\\Logger.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Logger.cpp",
              "RelativeToolTip": "Util\\Logger.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABYAAAAmAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-06T07:51:36.591Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 46,
              "Title": "Logger.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Logger.h",
              "RelativeDocumentMoniker": "Util\\Logger.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Logger.h",
              "RelativeToolTip": "Util\\Logger.h",
              "ViewState": "AgIAACEAAAAAAAAAAAAAAAcAAABSAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-28T17:03:08.281Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 47,
              "Title": "Memory_LowFragmentationHeap.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Memory_LowFragmentationHeap.h",
              "RelativeDocumentMoniker": "Util\\Memory_LowFragmentationHeap.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Memory_LowFragmentationHeap.h",
              "RelativeToolTip": "Util\\Memory_LowFragmentationHeap.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABgAAAADAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:52:10.5Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 33,
              "Title": "Terminal.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Terminal\\Terminal.cpp",
              "RelativeDocumentMoniker": "Net\\Terminal\\Terminal.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Terminal\\Terminal.cpp",
              "RelativeToolTip": "Net\\Terminal\\Terminal.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAADsAAAAWAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-12T08:33:23.215Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 48,
              "Title": "MemoryLeak.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\MemoryLeak.h",
              "RelativeDocumentMoniker": "Util\\MemoryLeak.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\MemoryLeak.h",
              "RelativeToolTip": "Util\\MemoryLeak.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAoAAAAGAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:52:17.42Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 35,
              "Title": "Session.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Session.cpp",
              "RelativeDocumentMoniker": "Net\\Session.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Net\\Session.cpp",
              "RelativeToolTip": "Net\\Session.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAACAAAAAbAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-06T07:50:02.425Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 49,
              "Title": "Minidump.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Minidump.cpp",
              "RelativeDocumentMoniker": "Util\\Minidump.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Minidump.cpp",
              "RelativeToolTip": "Util\\Minidump.cpp",
              "ViewState": "AgIAABsAAAAAAAAAAAAAACsAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-03-05T12:57:32.788Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 51,
              "Title": "Monitoring.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Monitoring.h",
              "RelativeDocumentMoniker": "Util\\Monitoring.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Monitoring.h",
              "RelativeToolTip": "Util\\Monitoring.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAADEAAAAeAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:52:43.592Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 52,
              "Title": "Table.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Table.h",
              "RelativeDocumentMoniker": "Util\\Table.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Table.h",
              "RelativeToolTip": "Util\\Table.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAACUAAAAFAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:53:11.545Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 53,
              "Title": "Task.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Task.cpp",
              "RelativeDocumentMoniker": "Util\\Task.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Task.cpp",
              "RelativeToolTip": "Util\\Task.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAGUAAAAkAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-06T07:53:22.451Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 54,
              "Title": "Task.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Task.h",
              "RelativeDocumentMoniker": "Util\\Task.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Task.h",
              "RelativeToolTip": "Util\\Task.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAADMAAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:53:31.045Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 55,
              "Title": "Thread.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Thread.cpp",
              "RelativeDocumentMoniker": "Util\\Thread.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Thread.cpp",
              "RelativeToolTip": "Util\\Thread.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAEwAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-06T07:53:38.486Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 44,
              "Title": "Lock.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Lock.h",
              "RelativeDocumentMoniker": "Util\\Lock.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Lock.h",
              "RelativeToolTip": "Util\\Lock.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T08:20:54.699Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 43,
              "Title": "Lock.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Lock.cpp",
              "RelativeDocumentMoniker": "Util\\Lock.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Lock.cpp",
              "RelativeToolTip": "Util\\Lock.cpp",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABIAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-01-29T09:14:54.386Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 56,
              "Title": "Thread.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Thread.h",
              "RelativeDocumentMoniker": "Util\\Thread.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Thread.h",
              "RelativeToolTip": "Util\\Thread.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAB8AAAAbAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-03-05T12:56:42.62Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 57,
              "Title": "Type.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Type.h",
              "RelativeDocumentMoniker": "Util\\Type.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Type.h",
              "RelativeToolTip": "Util\\Type.h",
              "ViewState": "AgIAAA8AAAAAAAAAAAAAACgAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:53:56.017Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 59,
              "Title": "ThreadJobQueue.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\ThreadJobQueue.h",
              "RelativeDocumentMoniker": "Util\\ThreadJobQueue.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\ThreadJobQueue.h",
              "RelativeToolTip": "Util\\ThreadJobQueue.h",
              "ViewState": "AgIAADwAAAAAAAAAAAAAAEsAAAACAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-03-05T12:56:01.085Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 50,
              "Title": "Minidump.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Minidump.h",
              "RelativeDocumentMoniker": "Util\\Minidump.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Minidump.h",
              "RelativeToolTip": "Util\\Minidump.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAA4AAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:52:38.591Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 58,
              "Title": "Util.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Util.h",
              "RelativeDocumentMoniker": "Util\\Util.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\Util.h",
              "RelativeToolTip": "Util\\Util.h",
              "ViewState": "AgIAAEgAAAAAAAAAAAAAAFYAAAABAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-06T07:54:06.985Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 67,
              "Title": "csv_parser.hpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\csv_parser\\csv_parser.hpp",
              "RelativeDocumentMoniker": "Util\\csv_parser\\csv_parser.hpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\csv_parser\\csv_parser.hpp",
              "RelativeToolTip": "Util\\csv_parser\\csv_parser.hpp",
              "ViewState": "AgIAAAAAAAAAAAAAAABhwAgAAAAQAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-16T04:01:00.752Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 76,
              "Title": "xutility",
              "DocumentMoniker": "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xutility",
              "RelativeDocumentMoniker": "..\\..\\..\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xutility",
              "ToolTip": "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xutility",
              "RelativeToolTip": "..\\..\\..\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xutility",
              "ViewState": "AgIAABgFAAAAAAAAAAAuwDAFAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.001001|",
              "WhenOpened": "2025-03-01T11:34:26.117Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 75,
              "Title": "xhash",
              "DocumentMoniker": "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xhash",
              "RelativeDocumentMoniker": "..\\..\\..\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xhash",
              "ToolTip": "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xhash",
              "RelativeToolTip": "..\\..\\..\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.41.34120\\include\\xhash",
              "ViewState": "AgIAAKwDAAAAAAAAAAAuwL0DAAAIAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.001001|",
              "WhenOpened": "2025-03-01T11:34:32.494Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 63,
              "Title": "csv_parser.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\csv_parser\\csv_parser.cpp",
              "RelativeDocumentMoniker": "Util\\csv_parser\\csv_parser.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\csv_parser\\csv_parser.cpp",
              "RelativeToolTip": "Util\\csv_parser\\csv_parser.cpp",
              "ViewState": "AgIAADIBAAAAAAAAAIBZwDgBAAArAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-16T04:00:59.139Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 66,
              "Title": "tinystr.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinystr.h",
              "RelativeDocumentMoniker": "Util\\tinyXml\\tinystr.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinystr.h",
              "RelativeToolTip": "Util\\tinyXml\\tinystr.h",
              "ViewState": "AgIAAKgAAAAAAAAAAAAYwLQAAAAUAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-16T04:01:02.723Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 61,
              "Title": "tinyxml.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxml.cpp",
              "RelativeDocumentMoniker": "Util\\tinyXml\\tinyxml.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxml.cpp",
              "RelativeToolTip": "Util\\tinyXml\\tinyxml.cpp",
              "ViewState": "AgIAADYAAAAAAAAAAAAawEYAAAAnAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-02-16T04:01:11.673Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 60,
              "Title": "tinyxml.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxml.h",
              "RelativeDocumentMoniker": "Util\\tinyXml\\tinyxml.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxml.h",
              "RelativeToolTip": "Util\\tinyXml\\tinyxml.h",
              "ViewState": "AgIAAP4BAAAAAAAAAAAawA4CAABMAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-16T04:01:14.062Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 69,
              "Title": "config.xml",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\LoginServer\\config.xml",
              "RelativeDocumentMoniker": "..\\LoginServer\\config.xml",
              "ToolTip": "C:\\github\\GameServer_Programming\\LoginServer\\config.xml",
              "RelativeToolTip": "..\\LoginServer\\config.xml",
              "ViewState": "AgIAAAAAAAAAAAAAAIBJwAQAAAAWAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.003576|",
              "WhenOpened": "2025-02-15T05:54:00.349Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 64,
              "Title": "config.xml",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\config.xml",
              "RelativeDocumentMoniker": "..\\ChattingServer\\config.xml",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\config.xml",
              "RelativeToolTip": "..\\ChattingServer\\config.xml",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAA0AAAANAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.003576|",
              "WhenOpened": "2025-02-15T05:52:47.057Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 62,
              "Title": "targetver.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\targetver.h",
              "RelativeDocumentMoniker": "..\\ChattingServer\\targetver.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\targetver.h",
              "RelativeToolTip": "..\\ChattingServer\\targetver.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-08T07:02:10.986Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 65,
              "Title": "stdafx.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ChattingServer\\stdafx.h",
              "RelativeDocumentMoniker": "..\\ChattingServer\\stdafx.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\ChattingServer\\stdafx.h",
              "RelativeToolTip": "..\\ChattingServer\\stdafx.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAoAAAASAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-08T07:02:00.165Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 71,
              "Title": "stdafx.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DBAgent\\stdafx.h",
              "RelativeDocumentMoniker": "..\\DBAgent\\stdafx.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\DBAgent\\stdafx.h",
              "RelativeToolTip": "..\\DBAgent\\stdafx.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAABAAAAAoAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-02-08T06:56:16.764Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 73,
              "Title": "stdafx.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\LoginServer\\stdafx.h",
              "RelativeDocumentMoniker": "..\\LoginServer\\stdafx.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\LoginServer\\stdafx.h",
              "RelativeToolTip": "..\\LoginServer\\stdafx.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T10:21:27.304Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 70,
              "Title": "config.xml",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\DBAgent\\config.xml",
              "RelativeDocumentMoniker": "..\\DBAgent\\config.xml",
              "ToolTip": "C:\\github\\GameServer_Programming\\DBAgent\\config.xml",
              "RelativeToolTip": "..\\DBAgent\\config.xml",
              "ViewState": "AgIAAAAAAAAAAAAAACBjwAkAAAARAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.003576|",
              "WhenOpened": "2025-01-29T10:15:25.185Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 68,
              "Title": "tinyxmlparser.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxmlparser.cpp",
              "RelativeDocumentMoniker": "Util\\tinyXml\\tinyxmlparser.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\ServerLibrary\\Util\\tinyXml\\tinyxmlparser.cpp",
              "RelativeToolTip": "Util\\tinyXml\\tinyxmlparser.cpp",
              "ViewState": "AgIAAAACAAAAAAAAAAAqwA0CAAANAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-01-29T10:00:18.098Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 74,
              "Title": "pch.cpp",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\LoginServer\\pch.cpp",
              "RelativeDocumentMoniker": "..\\LoginServer\\pch.cpp",
              "ToolTip": "C:\\github\\GameServer_Programming\\LoginServer\\pch.cpp",
              "RelativeToolTip": "..\\LoginServer\\pch.cpp",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000677|",
              "WhenOpened": "2025-01-29T09:29:22.354Z"
            },
            {
              "$type": "Document",
              "DocumentIndex": 72,
              "Title": "targetver.h",
              "DocumentMoniker": "C:\\github\\GameServer_Programming\\LoginServer\\targetver.h",
              "RelativeDocumentMoniker": "..\\LoginServer\\targetver.h",
              "ToolTip": "C:\\github\\GameServer_Programming\\LoginServer\\targetver.h",
              "RelativeToolTip": "..\\LoginServer\\targetver.h",
              "ViewState": "AgIAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAA==",
              "Icon": "ae27a6b0-e345-4288-96df-5eaf394ee369.000680|",
              "WhenOpened": "2025-01-29T09:28:42.604Z"
            }
          ]
        }
      ]
    }
  ]
}
```

## ServerLibrary\Contents\ContentsProcess.cpp
```cpp
#pragma once
#include "stdafx.h"
#include "ContentsProcess.h"

ContentsProcess::ContentsProcess()
{
	xml_t config;
	if (!loadConfig(&config)) {
		return;
	}
	this->initialize(&config);
}

ContentsProcess::~ContentsProcess()
{
	SAFE_DELETE(packageQueue_);

	for (auto thread : threadPool_) {
		SAFE_DELETE(thread);
	}
	runFuncTable_.clear();
}

void ContentsProcess::initialize(xml_t *config)
{
	xmlNode_t *root = config->FirstChildElement("App")->FirstChildElement("Contents");
	if (!root) {
		SErrLog(L"* not exist process setting");
		return;
	}
	xmlNode_t *elem = root->FirstChildElement("ThreadCount");
	int processCount = 0;
	sscanf_s(elem->GetText(), "%d", &processCount);

	if (MAX_PACKET_THREAD_ < processCount) {
		SErrLog(L"! processThread limit[%d], but config setting [%d]", MAX_PACKET_THREAD_, processCount);
		return;
	}

	packageQueue_ = new ThreadJobQueue<Package *> (L"ContentsProcessQueue");
	for (int i = 0; i < processCount; ++i) {
		threadPool_[i] = MAKE_THREAD(ContentsProcess, process);
	}
	this->registDefaultPacketFunc();
}

void ContentsProcess::registDefaultPacketFunc()
{
	runFuncTable_.insert(make_pair(E_C_NOTIFY_HEARTBEAT, &ContentsProcess::Packet_HeartBeat));
	runFuncTable_.insert(make_pair(E_I_NOTIFY_TERMINAL, &ContentsProcess::Packet_Notify_Terminal));
	runFuncTable_.insert(make_pair(E_C_REQ_EXIT, &ContentsProcess::C_REQ_EXIT));
}

void ContentsProcess::putPackage(Package *package)
{
	packageQueue_->push(package);
}

void ContentsProcess::run(Package *package)
{
	PacketType type = package->packet_->type();
	auto itr = runFuncTable_.find(type);
	if (itr == runFuncTable_.end()) {
		SLog(L"! invalid packet runFunction. type[%d]", type);
		package->session_->onClose();
		return;
	}
	RunFunc runFunction = itr->second;
#ifdef _DEBUG
	SLog(L"*** [%d] packet run ***", type);
#endif //_DEBUG
	runFunction(package->session_, package->packet_);
}

void ContentsProcess::execute()
{
	Package *package = nullptr;
	if (packageQueue_->pop(package) == false) {
		return;
	}

	this->run(package);
	
	SAFE_DELETE(package);
}

void ContentsProcess::process()
{
	while (_shutdown == false) {
		this->execute();
		CONTEXT_SWITCH;
	}
}

void ContentsProcess::Packet_HeartBeat(Session *session, Packet *rowPacket)
{
	if (session->type() != SESSION_TYPE_CLIENT) {
		return;
	}
	session->updateHeartBeat();
}

void ContentsProcess::Packet_Notify_Terminal(Session *session, Packet *rowPacket)
{
	session->setType(SESSION_TYPE_TERMINAL);
	SLog(L"* [%s] Terminal accepted.", session->clientAddress().c_str());
}

void ContentsProcess::C_REQ_EXIT(Session *session, Packet *rowPacket)
{
	PK_C_REQ_EXIT *packet = (PK_C_REQ_EXIT *)rowPacket;
	PK_S_ANS_EXIT ansPacket;

	SLog(L"ContentsPro!!!test!!!");
	SLog(L"* recv exit packet by [%s]", session->clientAddress().c_str());
	session->sendPacket(&ansPacket);
}
```

## ServerLibrary\Contents\ContentsProcess.h
```h
#pragma once
#include "stdafx.h"

#define MAX_PACKET_THREAD_		SIZE_64
class ContentsProcess
{
private:
	array<Thread *, MAX_PACKET_THREAD_> threadPool_;
	ThreadJobQueue<Package *> *packageQueue_;

protected:
	typedef void(*RunFunc)(Session *session, Packet *rowPacket);
	unordered_map<PacketType, RunFunc> runFuncTable_;

private:
	void initialize(xml_t *config);
	void registDefaultPacketFunc();
	void run(Package *package);
	void execute();

	void process();
public:
	ContentsProcess();
	~ContentsProcess();
	void putPackage(Package *package);

	virtual void registSubPacketFunc() = 0;


	static void Packet_HeartBeat(Session *session, Packet *rowPacket);
	static void Packet_Notify_Terminal(Session *session, Packet *rowPacket);
	static void C_REQ_EXIT(Session *session, Packet *rowPacket);
};
```

## ServerLibrary\Database\ADODatabase.cpp
```cpp
#include "stdafx.h"
#include "ADODatabase.h"
#include "QueryStatement.h"
#include "DBManager.h"

ADODatabase::ADODatabase()
{
	::CoInitialize(NULL);
    state_ = DB_STOP;

	dbConnection_.CreateInstance(__uuidof(ADODB::Connection));
	if (dbConnection_ == NULL) {
		SErrLog(L"! Database init fail");
	}
    const int TIME_OUT = 30;
    this->setConnectTimeOut(TIME_OUT);
}

ADODatabase::~ADODatabase()
{
    this->disconnect();
    if (dbConnection_) {
        dbConnection_.Release();
    }
	SAFE_DELETE(thread_);
	::CoUninitialize();
}

HRESULT	ADODatabase::setConnectTimeOut(long second)
{
	if (!dbConnection_){
		return S_FALSE;
	}
	return dbConnection_->put_ConnectionTimeout(second);
}

void ADODatabase::comError(const WCHAR *actionName, _com_error &e)
{
    SLog(L"! [%s]DB [%s] fail [%s]", dbName_.c_str(), actionName, (WCHAR *)e.Description());
}

bool ADODatabase::connect()
{
	if (!dbConnection_) {
		return false;
	}
	
	try {
		HRESULT hr = dbConnection_->Open(connectionStr_.c_str(), _T(""), _T(""), NULL);
		if (SUCCEEDED(hr)) {
			
			dbConnection_->PutCursorLocation(ADODB::adUseClient);
			SLog(L"* [%s]DB connection success", dbName_.c_str());
			state_ = DB_STANDBY;
			return true;
		}
	}
	catch (_com_error &e) {
		this->comError(L"connction", e);
		
	}

	return false;
}

bool ADODatabase::connect(const WCHAR* provider, const WCHAR* serverName, const WCHAR* dbName, const WCHAR* id, const WCHAR* password)
{
	array<WCHAR, SIZE_128> buffer;
	snwprintf(buffer, L"Provider=%s;Server=%s;Database=%s;Uid=%s;Pwd=%s;", provider, serverName, dbName, id, password);

	connectionStr_ = buffer.data();

	SLog(L"* [%s]DB try connection provider = %s", dbName_.c_str(), provider);
	return this->connect(); // 실제 연결 메서드 호출
}

bool ADODatabase::connect(const WCHAR* serverName, const WCHAR* dbName, const WCHAR* id, const WCHAR* password)
{
	dbName_ = dbName;
	SLog(L"* connect try: %s, %s, %s", dbName, id, password);

	// SQLNCLI 프로바이더 연결 시도
	//for (int index = 10; index < 20; ++index) {
	//	array<WCHAR, SIZE_64> mssqlName;
	//	snwprintf(mssqlName, L"SQLNCLI%d", index);
	//	if (this->connect(mssqlName.data(), serverName, dbName, id, password)) {
	//		SLog(L"* database %s : %s connect", mssqlName.data(), dbName);
	//		return true;
	//	}
	//}

	// SQLOLEDB 프로바이더로 연결 시도
	//if (this->connect(L"SQLOLEDB", serverName, dbName, id, password)) {
	//	SLog(L"* database SQLOLEDB : %s connect", dbName);
	//	return true;
	//}
	if (this->connect(L"SQLNCLI11", serverName, dbName, id, password)) {
			SLog(L"* database SQLNCLI11 : %s connect", dbName);
			return true;
		}

	return false;
}


bool ADODatabase::connected()
{
    return dbConnection_->State != ADODB::adStateClosed ? true : false;
}

bool ADODatabase::disconnect()
{
	if (!dbConnection_) {
		return false;
	}
    if (state_ == DB_STOP) {
        return true;
    }
	try {
        this->execute();

        if (!dbConnection_) {
            return true;
        }
		dbConnection_->Close();
        state_ = DB_STOP;

        connectionStr_.clear();
        dbName_.clear();
        SLog(L"* database close");
		return true;
	} catch (...) {
        SLog(L"! Database[%s] disconnect fail", dbName_.c_str());
	}
	return false;
}

void ADODatabase::execute()
{
	if (DBManager::getInstance().runQueryCount() == 0){
		return;
	}

	Query *query = nullptr;
	if (DBManager::getInstance().popQuery(&query) == false) {
		return;
	}
	QueryStatement *statement = query->statement();

	const WCHAR *sqlQuery = statement->query();
	try {
		state_ = DB_RUNNING;
		QueryRecord record;

		ADODB::_CommandPtr command;
		command.CreateInstance(__uuidof(ADODB::Command));
		command->ActiveConnection = dbConnection_;
		command->CommandType = ADODB::adCmdText;
		command->CommandText = sqlQuery;
		_variant_t resultVal;

		switch (statement->type()) {
		case QUERY_NOT_RETURN:
			record = command->Execute(&resultVal, NULL, ADODB::adCmdText | ADODB::adExecuteNoRecords);
			break;
		case QUERY_WAIT_RETURN:
			record = command->Execute(&resultVal, NULL, ADODB::adCmdText | ADODB::adExecuteRecord);
			break;
		case QUERY_CALL_BACK:
			record = command->Execute(&resultVal, NULL, ADODB::adCmdText | ADODB::adAsyncFetchNonBlocking);
			break;
		}

		if (record.isEof()) {
			int quertResultVal = atol((char*)((_bstr_t)resultVal));
			
			if (quertResultVal < 1) {
				SLog(L"* query : [%s] have error code [%d] ", sqlQuery, quertResultVal);
			}
			else {
				record.setResultVal(quertResultVal);
			}
		}
		
		query->result() = record;
		state_ = DB_STANDBY;

		SLog(L"* Run query [%s] result [%d]", sqlQuery, record.resultVal());
	}
	catch (_com_error &e) {
		this->comError(L"execute", e);
	}

	SAFE_DELETE(query);
}

void ADODatabase::process()
{
    while (_shutdown == false) {
		if (!this->connected()) {
			SLog(L"! db[%s] connection disconnect", dbName_.c_str());
			ASSERT(FALSE);
		}
		this->execute();

		CONTEXT_SWITCH;
    }
}

void ADODatabase::run()
{
	thread_ = MAKE_THREAD(ADODatabase, process);
}
```

## ServerLibrary\Database\ADODatabase.h
```h
#pragma once
#include "stdafx.h"

#import "C:\Program Files\Common Files\System\ado\msado15.dll"	rename("EOF", "EndOfFile")
#include "Database.h"

typedef ADODB::_ConnectionPtr           dbConnectionPtr;
typedef ADODB::_CommandPtr				commandPtr;
typedef ADODB::_RecordsetPtr			recordPtr;

class ADODatabase : public Database
{
    dbConnectionPtr   			dbConnection_;
	wstr_t			            connectionStr_;
    wstr_t			            dbName_;
	
	Thread						*thread_;

public:
	ADODatabase();
	virtual ~ADODatabase();

	HRESULT	setConnectTimeOut(long second);
	void comError(const WCHAR *actionName, _com_error &e);

    bool connect(const WCHAR *provider, const WCHAR *serverName, const WCHAR *dbName, const WCHAR *id, const WCHAR *password);
    bool connect(const WCHAR *serverName, const WCHAR *dbName, const WCHAR *id, const WCHAR *password);
    bool connect();
    bool connected();
    bool disconnect();
    
	void run();

private:
    void execute();
    void process();
};
```

## ServerLibrary\Database\Database.h
```h
#pragma once
#include "stdafx.h"
#include <oledb.h> 
#include <comdef.h>
#include <comutil.h>

typedef enum
{
    DB_STOP,                // 정지
    DB_STANDBY,             // 쿼리 받을 준비
    DB_RUNNING,             // 쿼리 실행중
}DB_STATE;

class Database
{
protected:
    DB_STATE        state_;

public:
    Database()
    {
    }
    virtual ~Database()
    {
    }

    virtual bool connect(const WCHAR *serverName, const WCHAR *dbName, const WCHAR *id, const WCHAR *password) = 0;
    virtual bool connect() = 0;
    virtual bool connected() = 0;
    virtual bool disconnect() = 0;

    virtual void run() = 0;
    DB_STATE &state() { return state_; }
};
```

## ServerLibrary\Database\DBManager.cpp
```cpp
#include "stdafx.h"

DBManager::DBManager()
{
	xml_t config;
	if (!loadConfig(&config)) {
		return;
	}

	this->initialize(&config);
}

void DBManager::initialize(xml_t *config)
{
	xmlNode_t *root = config->FirstChildElement("App")->FirstChildElement("DataBase");
	if (!root) {
		SLog(L"@ not exist database setting");
		return;
	}
	xmlNode_t *elem = root->FirstChildElement("ThreadCount");
	sscanf_s(elem->GetText(), "%d", &workerCount_);

	array<WCHAR, SIZE_256> tmp;
	elem = root->FirstChildElement("ServerName");
	StrConvA2W((char *) elem->GetText(), tmp.data(), tmp.max_size());
	serverName_ = tmp.data();

	elem = root->FirstChildElement("DB");
	StrConvA2W((char *) elem->GetText(), tmp.data(), tmp.max_size());
	dbName_ = tmp.data();

	elem = root->FirstChildElement("Login");
	StrConvA2W((char *) elem->GetText(), tmp.data(), tmp.max_size());
	login_ = tmp.data();

	elem = root->FirstChildElement("Password");
	StrConvA2W((char *) elem->GetText(), tmp.data(), tmp.max_size());
	password_ = tmp.data();

	queryPool_ = new ThreadJobQueue<Query *>(L"DBQueueJob");

	for (int i = 0; i < workerCount_; ++i) {
		array<WCHAR, SIZE_128> patch = { 0, };
		ADODatabase *adodb = new ADODatabase();
		dbPool_.push_back(adodb);
	}
	this->run();
}

DBManager::~DBManager()
{
	SAFE_DELETE(queryPool_);

    for (auto db : dbPool_) {
        db->disconnect();
        SAFE_DELETE(db);
    }
}

size_t DBManager::runQueryCount()
{
	return queryPool_->size();
}

void DBManager::pushQuery(Query *query)
{
    queryPool_->push(query);
}

bool DBManager::popQuery(Query **query)
{
    return queryPool_->pop(*query);
}

void DBManager::run()
{
    for (auto db : dbPool_) {
        if (db->state() != DB_STOP) {
            continue;
        }

		if (!db->connect(serverName_.c_str(), dbName_.c_str(), login_.c_str(), password_.c_str())) {
			SErrLog(L"! db[%s] connection error", dbName_.c_str());
		}
        db->run();
    }
}
```

## ServerLibrary\Database\DBManager.h
```h
#pragma once
#include "stdafx.h"
#include "ADODatabase.h"

#define _db_manager		DBManager::getInstance()

class DBManager : public Singleton < DBManager >
{
	int                                 workerCount_;
	std::vector<Database *>             dbPool_;

	wstr_t								serverName_;
	wstr_t								dbName_;
	wstr_t								login_;
	wstr_t								password_;
	ThreadJobQueue<Query *>				*queryPool_;

public:
	DBManager();
	virtual ~DBManager();

	void initialize(xml_t *config);

	size_t runQueryCount();
	void pushQuery(Query *query);
	bool popQuery(Query **query);

	void run();
};
```

## ServerLibrary\Database\Query.cpp
```cpp
#pragma once
#include "stdafx.h"
#include "QueryStatement.h"
#include "QueryRecord.h"
#include "Query.h"
#include "ADODatabase.h"
#include "DBManager.h"

Query::Query()
{
	statement_ = new QueryStatement();
}
Query::~Query()
{
	record_.close();
	SAFE_DELETE(statement_);
}

void Query::setResult(recordPtr record)
{
	record_.setRecord(record);
}

QueryRecord& Query::result()
{
	return record_;
}

void Query::setStatement(QueryStatement *statement)
{
	statement_ = statement;
}

QueryStatement* Query::statement()
{
	return statement_;
}
```

## ServerLibrary\Database\Query.h
```h
#pragma once
#include "stdafx.h"
#include "ADODatabase.h"

#include "QueryRecord.h"
#include "QueryStatement.h"
class Query
{
protected:
	QueryStatement		*statement_;
	QueryRecord			record_;
public:
	Query();
	virtual ~Query();
	
	void setResult(recordPtr record);
	QueryRecord &result();

	void setStatement(QueryStatement *statement);
	QueryStatement *statement();
		
};
```

## ServerLibrary\Database\QueryRecord.cpp
```cpp
#include "stdafx.h"
#include "QueryRecord.h"

QueryRecord::QueryRecord()
{
    record_.CreateInstance(__uuidof(ADODB::Recordset));
}

QueryRecord::~QueryRecord()
{
    if (record_ == nullptr) {
        return;
    }
    record_.Release();
    record_ = nullptr;
}

void QueryRecord::errorReport(_com_error &e) {
    SLog(L"* Query error = %S", e.Description());
}

recordPtr &QueryRecord::resultRecord()
{
    return record_;
}

void QueryRecord::operator = (QueryRecord &lvalue)
{
	record_ = lvalue.resultRecord();
}

void QueryRecord::operator = (recordPtr &lvalue)
{
    record_ = lvalue;
}

void QueryRecord::setRecord(recordPtr record)
{
    record_ = record;
}

bool QueryRecord::opened()
{
    return record_->State == ADODB::adStateOpen ? true : false;
}

void QueryRecord::close()
{
    try{
        if (record_ != nullptr && this->opened())
            record_->Close();
    }
    catch (_com_error &e){
        this->errorReport(e);
    }
}

int QueryRecord::resultVal()
{
	return resultVal_;
}

void QueryRecord::setResultVal(int result)
{
	resultVal_ = result;
}

bool QueryRecord::isEof()
{
	if (record_ == nullptr) {
		return true;
	}
	try {
		return record_->EndOfFile ? true : false;
	}
	catch (_com_error &e) {
		this->errorReport(e);
	}
	return false;
}

HRESULT QueryRecord::moveNext()
{
	try {
		return record_->MoveNext();
	}
	catch (_com_error &e) {
		this->errorReport(e);
	}
	return S_FALSE;
}

HRESULT QueryRecord::movePrevious()
{
	try {
		return record_->MovePrevious();
	}
	catch (_com_error &e) {
		this->errorReport(e);
	}
	return S_FALSE;
}

HRESULT QueryRecord::moveFirst()
{
	try {
		return record_->MoveFirst();
	}
	catch (_com_error &e) {
		this->errorReport(e);
	}
	return S_FALSE;
}

HRESULT QueryRecord::moveLast()
{
	try {
		return record_->MoveLast();
	}
	catch (_com_error &e) {
		this->errorReport(e);
	}
	return S_FALSE;
}

bool QueryRecord::get(char* fieldName, char* fieldValue)
{
	try {
		_variant_t  vtValue;
		vtValue = record_->Fields->GetItem(fieldName)->GetValue();
		sprintf_s(fieldValue, DB_PARAM_SIZE, "%s", (LPCSTR)((_bstr_t)vtValue.bstrVal));
		return true;
	}
	catch (_com_error &e) {
		this->errorReport(e);
		SLog(L"! error query field : %S", fieldName);
	}
	return false;
}

bool QueryRecord::get(char* fieldName, wchar_t* fieldValue)
{
	try {
		_variant_t  vtValue;
		vtValue = record_->Fields->GetItem(fieldName)->GetValue();
		swprintf_s(fieldValue, DB_PARAM_SIZE, L"%s", (LPWSTR)((_bstr_t)vtValue.bstrVal));
		return true;
	}
	catch (_com_error &e) {
		this->errorReport(e);
		SLog(L"! error query field : %S", fieldName);
	}
	return false;
}

bool QueryRecord::get(char* fieldName, int32_t& fieldValue)
{
	try {
		_variant_t  vtValue;
		vtValue = record_->Fields->GetItem(fieldName)->GetValue();
		fieldValue = vtValue.intVal;
		return true;
	}
	catch (_com_error &e) {
		this->errorReport(e);
		SLog(L"! error query field : %S", fieldName);
	}
	return false;
}

bool QueryRecord::get(char* fieldName, int64_t& fieldValue)
{
	try {
		_variant_t  vtValue;
		vtValue = record_->Fields->GetItem(fieldName)->GetValue();
		fieldValue = vtValue.intVal;
		return true;
	}
	catch (_com_error &e) {
		this->errorReport(e);
		SLog(L"! error query field : %S", fieldName);
	}
	return false;
}

bool QueryRecord::get(char* fieldName, float& fieldValue)
{
	try {
		_variant_t  vtValue;
		vtValue = record_->Fields->GetItem(fieldName)->GetValue();
		fieldValue = vtValue.fltVal;
		return true;
	}
	catch (_com_error &e) {
		this->errorReport(e);
		SLog(L"! error query field : %S", fieldName);
	}
	return false;
}

bool QueryRecord::get(char* fieldName, double& fieldValue)
{
	try {
		_variant_t  vtValue;
		vtValue = record_->Fields->GetItem(fieldName)->GetValue();
		fieldValue = vtValue.dblVal;
		return true;
	}
	catch (_com_error &e) {
		this->errorReport(e);
		SLog(L"! error query field : %S", fieldName);
	}
	return false;
}

bool QueryRecord::get(char* fieldName, long& fieldValue)
{
	try {
		_variant_t  vtValue;
		vtValue = record_->Fields->GetItem(fieldName)->GetValue();
		fieldValue = vtValue.lVal;
		return true;
	}
	catch (_com_error &e) {
		this->errorReport(e);
		SLog(L"! error query field : %S", fieldName);
	}
	return false;
}
```

## ServerLibrary\Database\QueryRecord.h
```h
#pragma once
#include "stdafx.h"
#include "ADODatabase.h"

class QueryRecord
{
    recordPtr		record_;
	int				resultVal_;		//쿼리 결과값
public:	
    QueryRecord();
    ~QueryRecord();

    void errorReport(_com_error &e);

    void operator = (QueryRecord &lvalue);
    void operator = (recordPtr &lvalue);
    recordPtr &resultRecord();

    bool        opened();
    void        close();
    void        setRecord(recordPtr record);
	bool		isEof();

	int			resultVal();
	void		setResultVal(int result);

	HRESULT		moveNext();
	HRESULT		movePrevious();
	HRESULT		moveFirst();
	HRESULT		moveLast();

	bool		get(char* fieldName, char* fieldValue);
	bool		get(char* fieldName, wchar_t* fieldValue);
	bool		get(char* fieldName, int32_t& fieldValue);
	bool		get(char* fieldName, int64_t& fieldValue);
	bool		get(char* fieldName, float& fieldValue);
	bool		get(char* fieldName, double& fieldValue);
	bool		get(char* fieldName, long& fieldValue);
};
```

## ServerLibrary\Database\QueryStatement.cpp
```cpp
#pragma once
#include "stdafx.h"
#include "ADODatabase.h"
#include "QueryRecord.h"
#include "QueryStatement.h"

QueryStatement::QueryStatement()
{
	paramCount_ = 0;
	query_.clear();
}

QueryStatement::~QueryStatement()
{
}

void QueryStatement::setQuery(WCHAR *query, QUERY_TYPE type)
{
	query_ = query;
	type_ = type;
}

const WCHAR* QueryStatement::query()
{
	return query_.c_str();
}
QUERY_TYPE QueryStatement::type()
{
	return type_;
}

//------------------ 파라메터 추가 -----------------/
template<typename T>
void QueryStatement::addArg(WCHAR *fmt, T value)
{
	array<WCHAR, DB_PARAM_SIZE> buffer;
	snwprintf(buffer, fmt, value);
	if (paramCount_++) {
		query_ += L", ";
	}
	else {
		query_ += L" ";
	}
	query_ += buffer.data();
}

void QueryStatement::addParam(CHAR *value)
{
	this->addArg(L"'%S'", value);
}

void QueryStatement::addParam(WCHAR *value)
{
	this->addArg(L"'%s'", value);
}

void QueryStatement::addParam(INT32 value)
{
	this->addArg(L"'%d'", value);
}

void QueryStatement::addParam(UINT32 value)
{
	this->addArg(L"'%u'", value);
}

void QueryStatement::addParam(INT64 value)
{
	this->addArg(L"'%lld'", value);
}

void QueryStatement::addParam(UINT64 value)
{
	this->addArg(L"'%llu'", value);
}

void QueryStatement::addParam(FLOAT value)
{
	this->addArg(L"'%f'", value);
}

void QueryStatement::addParam(DOUBLE value)
{
	this->addArg(L"'%lf'", value);
}
```

## ServerLibrary\Database\QueryStatement.h
```h
#pragma once
#include "stdafx.h"
#include "ADODatabase.h"

typedef enum
{
    QUERY_NOT_RETURN,				
    QUERY_WAIT_RETURN,				
    QUERY_CALL_BACK,				
}QUERY_TYPE;

class QueryStatement
{
    ADODB::_CommandPtr		command_;
    QUERY_TYPE				type_;

    wstr_t					query_;
    int						paramCount_;

public:
    QueryStatement();
    ~QueryStatement();

    void setQuery(WCHAR *query, QUERY_TYPE type = QUERY_NOT_RETURN);

    const WCHAR *query();
    QUERY_TYPE type();

    //------------------ 파라메터 추가 -----------------/
    template<typename T>
    void addArg(WCHAR *fmt, T value);

    void addParam(CHAR *value);
    void addParam(WCHAR *value);
    void addParam(INT32 value);
    void addParam(UINT32 value);
    void addParam(INT64 value);
    void addParam(UINT64 value);
    void addParam(FLOAT value);
    void addParam(DOUBLE value);
};
```

## ServerLibrary\item.csv
```csv
종류,이름 ,착용Lv,Att,Def,Dex,착용부위
반지,집중,65,250,700,250,손가락
대검,엑스칼리안,70,2400,600,500,무기
마법봉,워의마법봉,70,2200,750,7000,무기
가슴방어구,잉거풀외투,70,700,540,550,가슴
```

## ServerLibrary\Net\IOCP\IOCPServer.cpp
```cpp
#include "stdafx.h"
#include "IOCPServer.h"
#include "IOCPSession.h"

IOCPServer::IOCPServer(ContentsProcess *contentsProcess)
:Server(contentsProcess)
{
}

IOCPServer::~IOCPServer()
{
	::closesocket(listenSocket_);
}

bool IOCPServer::createListenSocket()
{
    listenSocket_ = WSASocket(AF_INET, SOCK_STREAM, NULL, NULL, 0, WSA_FLAG_OVERLAPPED);
    if (listenSocket_ == INVALID_SOCKET) {
        SErrLog(L"! listenSocket fail");
        return false;
    }

    SOCKADDR_IN serverAddr;
    serverAddr.sin_family = AF_INET;
	serverAddr.sin_port = htons((u_short)port_);
	inet_pton(AF_INET, ip_, &(serverAddr.sin_addr));

	int reUseAddr = 1;
	setsockopt(listenSocket_, SOL_SOCKET, SO_REUSEADDR, (char *)&reUseAddr, (int)sizeof(reUseAddr));

    int retval = ::bind(listenSocket_, (SOCKADDR *)&serverAddr, sizeof(serverAddr));
    if (retval == SOCKET_ERROR) {
        SErrLog(L"! bind fail");
        return false;
    }

    const int BACK_SOCKETS = 5;
    retval = ::listen(listenSocket_, BACK_SOCKETS);
    if (retval == SOCKET_ERROR) {
        SErrLog(L"! listen fail");
        return false;
    }

	array<char, SIZE_64> ip;
	inet_ntop(AF_INET, &(serverAddr.sin_addr), ip.data(), ip.size());
	SLog(L"* server listen socket created, ip: %S, port: %d", ip.data(), port_);
    return true;
}

bool IOCPServer::run()
{
	if (MAX_IOCP_THREAD < workerThreadCount_) {
		SErrLog(L"! workerThread limit[%d], but config setting [%d]", MAX_IOCP_THREAD, workerThreadCount_);
		return false;
	}

	iocp_ = CreateIoCompletionPort(INVALID_HANDLE_VALUE, NULL, 0, workerThreadCount_);
	if (iocp_ == nullptr) {
		return false;
	}
	this->createListenSocket();
	
	acceptThread_ = MAKE_THREAD(IOCPServer, acceptThread);
	for (int i = 0; i < workerThreadCount_; ++i) {
		workerThread_[i] = MAKE_THREAD(IOCPServer, workerThread);
	}
	this->status_ = SERVER_READY;

	while (!_shutdown) {
		wstring cmdLine;
		std::getline(std::wcin, cmdLine);

		SLog(L"Input was: %s", cmdLine.c_str());
		_session_manager.runCommand(cmdLine);
	}
	return true;
}

SOCKET IOCPServer::listenSocket()
{
    return listenSocket_;
}

HANDLE IOCPServer::iocp()
{
    return iocp_;
}

void IOCPServer::onAccept(SOCKET accepter, SOCKADDR_IN addrInfo)
{
    IOCPSession *session = new IOCPSession();
	if (session == nullptr) {
		SLog(L"! accept session create fail");
		return;
	}
	if (!session->onAccept(accepter, addrInfo)) {
		SAFE_DELETE(session);
		return;
	}
	if (!_session_manager.addSession(session)) {
		SAFE_DELETE(session);
		return;
	}
	session->ioData_[IO_READ].clear();

	HANDLE handle = CreateIoCompletionPort((HANDLE)accepter, this->iocp(), (ULONG_PTR)&(*session), NULL);
	if (!handle) {
		SAFE_DELETE(session);
		return;
	}
    
    SLog(L"* client accecpt from [%s]", session->clientAddress().c_str());
	session->recvStandBy();
}

DWORD WINAPI IOCPServer::acceptThread(LPVOID serverPtr)
{
	IOCPServer	*server = (IOCPServer *)serverPtr;
	
    while (!_shutdown) {
		SOCKET		acceptSocket = INVALID_SOCKET;
		SOCKADDR_IN recvAddr;
		static int addrLen = sizeof(recvAddr);
		acceptSocket = WSAAccept(server->listenSocket(), (struct sockaddr *)&recvAddr, &addrLen, NULL, 0);
		if (acceptSocket == SOCKET_ERROR) {
			if (!server->status() == SERVER_STOP) {
				SLog(L"! Accept fail");
				break;
			}
		}
		server->onAccept(acceptSocket, recvAddr);

		if (server->status() != SERVER_READY) {
			break;
		}
	}
	return 0;
}

DWORD WINAPI IOCPServer::workerThread(LPVOID serverPtr)
{
	IOCPServer *server = (IOCPServer *)serverPtr;

	while (!_shutdown) {
		IoData			*ioData = nullptr;
		IOCPSession	*session = nullptr;
		DWORD			transferSize;

		BOOL ret = GetQueuedCompletionStatus(server->iocp(), &transferSize, (PULONG_PTR)&session, (LPOVERLAPPED *)&ioData, INFINITE);
		if (!ret) {
			continue;
		}
		if (session == nullptr) {
			SLog(L"! socket data broken");
			return 0;
		}
		if (transferSize == 0) {
			SLog(L"* close by client[%d][%s]", session->id(), session->clientAddress().c_str());
			_session_manager.closeSession(session);
			continue;
		}

		switch (ioData->type()) {
		case IO_WRITE:
			session->onSend((size_t)transferSize);
			continue;

		case IO_READ:
			{
				Package *package = session->onRecv((size_t)transferSize);
				if (package != nullptr) {
					server->putPackage(package);
				}
			}
			continue;

		case IO_ERROR:
			SLog(L"* close by client error [%d][%s]", session->id(), session->clientAddress().c_str());
			_session_manager.closeSession(session);
			continue;
		}
	}
	return 0;
}
```

## ServerLibrary\Net\IOCP\IOCPServer.h
```h
#pragma once
#include "stdafx.h"
#include "../Server.h"

#define MAX_IOCP_THREAD		SIZE_64

class IOCPServer : public Server, public Singleton<IOCPServer>
{
    SOCKET					listenSocket_;
    HANDLE					iocp_;
	Thread					*acceptThread_;
	array<Thread *, SIZE_64> workerThread_;

private:
	bool					createListenSocket();

    static DWORD WINAPI		acceptThread(LPVOID serverPtr);
	static DWORD WINAPI		workerThread(LPVOID serverPtr);

public:
	IOCPServer(ContentsProcess *contentsProcess);
    virtual ~IOCPServer();

	bool					run();

    SOCKET					listenSocket();
    HANDLE					iocp();
	void					onAccept(SOCKET accepter, SOCKADDR_IN addrInfo);
};
```

## ServerLibrary\Net\IOCP\IOCPSession.cpp
```cpp
#include "stdafx.h"
#include "../Session.h"
#include "IOCPSession.h"
#include "../SessionManager.h"
#include "../Packet/PacketAnalyzer.h"

IoData::IoData()
{
	ZeroMemory(&overlapped_, sizeof(overlapped_));
	ioType_ = IO_ERROR;
	
	this->clear();
}

void IoData::clear()
{
	buffer_.fill(0);
	totalBytes_ = 0;
	currentBytes_ = 0;
}

bool IoData::needMoreIO(size_t transferSize)
{
	currentBytes_ += transferSize;
	if (currentBytes_ < totalBytes_) {
		return true;
	}
	return false;
}

int32_t IoData::setupTotalBytes()
{
	packet_size_t offset = 0;
	packet_size_t packetLen[1] = { 0, };
	if (totalBytes_ == 0) {
		memcpy_s((void *)packetLen, sizeof(packetLen), (void *)buffer_.data(), sizeof(packetLen));
		PacketObfuscation::getInstance().decodingHeader((Byte*)&packetLen, sizeof(packetLen));

		totalBytes_ = (size_t)packetLen[0];
	}
	offset += sizeof(packetLen);

	return offset;
}
size_t IoData::totalByte()
{
	return totalBytes_;
}

IO_OPERATION &IoData::type()
{
	return ioType_;
}

void IoData::setType(IO_OPERATION type)
{
	ioType_ = type;
}

char* IoData::data()
{
	return buffer_.data();
}

bool IoData::setData(Stream &stream)
{
	this->clear();

	if (buffer_.max_size() <= stream.size()) {
		SLog(L"! packet size too big [%d]byte", stream.size());
		return false;
	}

	const size_t packetHeaderSize = sizeof(packet_size_t);
	packet_size_t offset = 0;

	char *buf = buffer_.data();
	packet_size_t packetLen[1] = { (packet_size_t)packetHeaderSize + (packet_size_t)stream.size(), };
	memcpy_s(buf + offset, buffer_.max_size(), (void *)packetLen, packetHeaderSize);
	offset += packetHeaderSize;

	PacketObfuscation::getInstance().encodingHeader((Byte*)buf, packetHeaderSize);
	PacketObfuscation::getInstance().encodingData((Byte*)stream.data(), stream.size());

	memcpy_s(buf + offset, buffer_.max_size(), stream.data(), (int32_t)stream.size());
	offset += (packet_size_t)stream.size();

	totalBytes_ = offset;
	return true;
}

LPWSAOVERLAPPED IoData::overlapped()
{
	return &overlapped_;
}

WSABUF IoData::wsabuf()
{
	WSABUF wsaBuf;
	wsaBuf.buf = buffer_.data() + currentBytes_;
	wsaBuf.len = (ULONG)(totalBytes_ - currentBytes_);
	return wsaBuf;
}

//-----------------------------------------------------------------//
IOCPSession::IOCPSession()
: Session()
{
	this->initialize();
}

void IOCPSession::initialize()
{
	ZeroMemory(&socketData_, sizeof(SOCKET_DATA));
	ioData_[IO_READ].setType(IO_READ);
	ioData_[IO_WRITE].setType(IO_WRITE);
}

void IOCPSession::checkErrorIO(DWORD ret)
{
	if (ret == SOCKET_ERROR
		&& (WSAGetLastError() != ERROR_IO_PENDING)) {
        SLog(L"! socket error: %d", WSAGetLastError());
	}
}

void IOCPSession::recv(WSABUF wsaBuf)
{
	DWORD flags = 0;
	DWORD recvBytes;
	DWORD errorCode = WSARecv(socketData_.socket_, &wsaBuf, 1, &recvBytes, &flags, ioData_[IO_READ].overlapped(), NULL);
	this->checkErrorIO(errorCode);
}

bool IOCPSession::isRecving(size_t transferSize)
{
	if (ioData_[IO_READ].needMoreIO(transferSize)) {
		this->recv(ioData_[IO_READ].wsabuf());
		return true;
	}
	return false;
}

void IOCPSession::recvStandBy()
{
	ioData_[IO_READ].clear();

	WSABUF wsaBuf;
	wsaBuf.buf = ioData_[IO_READ].data();
	wsaBuf.len = SOCKET_BUF_SIZE;

	this->recv(wsaBuf);
}

void IOCPSession::send(WSABUF wsaBuf)
{
	DWORD flags = 0;
	DWORD sendBytes;
	DWORD errorCode = WSASend(socketData_.socket_, &wsaBuf, 1, &sendBytes, flags, ioData_[IO_WRITE].overlapped(), NULL);
	this->checkErrorIO(errorCode);
}

void IOCPSession::onSend(size_t transferSize)
{
	if (ioData_[IO_WRITE].needMoreIO(transferSize)) {
		this->send(ioData_[IO_WRITE].wsabuf());
	}
}

void IOCPSession::sendPacket(Packet *packet)
{
	Stream stream;
	packet->encode(stream);
	if (!ioData_[IO_WRITE].setData(stream)) {
		return;
	}
	
	WSABUF wsaBuf;
	wsaBuf.buf = ioData_[IO_WRITE].data();
	wsaBuf.len = (ULONG) stream.size();

	this->send(wsaBuf);
    this->recvStandBy();
}

Package *IOCPSession::onRecv(size_t transferSize)
{
	packet_size_t offset = 0;
	offset += ioData_[IO_READ].setupTotalBytes();

	if (this->isRecving(transferSize)) {
		return nullptr;
	}

	const size_t packetHeaderSize = sizeof(packet_size_t);
	packet_size_t packetDataSize = (packet_size_t)(ioData_[IO_READ].totalByte() - packetHeaderSize);
	Byte *packetData = (Byte*) ioData_[IO_READ].data() + offset;

	PacketObfuscation::getInstance().decodingData(packetData, packetDataSize);
	Packet *packet = PacketAnalyzer::getInstance().analyzer((const char *)packetData, packetDataSize);
	if (packet == nullptr) {
		SLog(L"! invaild packet");
		this->onClose(true);
		return nullptr;
	}

	this->recvStandBy();

	Package *package = new Package(this, packet);
	return package;
}
```

## ServerLibrary\Net\IOCP\IOCPSession.h
```h
#pragma once
#include "stdafx.h"
class Session;
class SessionManager;
class Package;

typedef enum {
	IO_READ,
	IO_WRITE,
	IO_ERROR,
} IO_OPERATION;
#define IO_DATA_MAX     (2)

class IoData
{
	OVERLAPPED		overlapped_;
	IO_OPERATION	ioType_;
    size_t  		totalBytes_;
	size_t			currentBytes_;
	array<char, SOCKET_BUF_SIZE> buffer_;

public:
	IoData();

	void clear();

	bool needMoreIO(size_t transferSize);
	int32_t setupTotalBytes();
	size_t totalByte();

	IO_OPERATION &type();
	void setType(IO_OPERATION type);

	WSABUF wsabuf();
	char *data();
	bool setData(Stream &stream);
	LPWSAOVERLAPPED overlapped();
};

//-----------------------------------------------------------------//
class IOCPSession : public Session
{
public:
	array<IoData, IO_DATA_MAX> ioData_;

private:
	void			initialize();

	void			checkErrorIO(DWORD ret);

	void			recv(WSABUF wsaBuf);
	bool			isRecving(size_t transferSize);

	void			send(WSABUF wsaBuf);

public:
    IOCPSession();

	void			onSend(size_t transferSize);
	void		    sendPacket(Packet *packet);
	
	Package*		onRecv(size_t transferSize);
    void			recvStandBy();

};
```

## ServerLibrary\Net\Packet\Package.h
```h
#pragma once
#include "stdafx.h"

class Session;
class Package
{
public:
	Session *session_;
	Packet *packet_;

	Package(Session *session, Packet *packet)
	{
		session_ = session;
		packet_ = packet;
	}

	~Package()
	{
		session_ = nullptr;
		SAFE_DELETE(packet_);
	}
};
```

## ServerLibrary\Net\Packet\PacketAnalyzer.cpp
```cpp
#pragma once
#include "stdafx.h"
#include "PacketClass.h"
#include "PacketAnalyzer.h"
#include "PacketFactory.h"

Packet* PacketAnalyzer::analyzer(const char *rowPacket, size_t size)
{
	size_t offset = 0;
	PacketType type[1] = { (PacketType)0, };
	memcpy_s((void *)type, sizeof(type), (void *)rowPacket, sizeof(type));
	offset += sizeof(type);

	Packet *packet = _packet_factory.getPacket(type[0]);
	if (packet) {
		if (offset < size) {
			Stream stream((UCHAR *)(rowPacket + offset), size - offset);
			packet->decode(stream);
		}
	}

	return packet;
}
```

## ServerLibrary\Net\Packet\PacketAnalyzer.h
```h
#pragma once
#include "stdafx.h"

class PacketAnalyzer : public Singleton < PacketAnalyzer >
{
public:
	Packet* analyzer(const char *rowPacket, size_t size);
};
```

## ServerLibrary\Net\Packet\PacketClass.h
```h
#pragma once
#include "stdafx.h"
#include "packetHeader.h"
#include "Stream.h"

class Packet {
public:
    virtual PacketType type() = 0;
    virtual void encode(Stream &stream) { stream << (Int64) this->type(); };
    virtual void decode(Stream &stream) { };
};

class PK_C_REQ_EXIT : public Packet
{
public:
    PacketType type() { return E_C_REQ_EXIT; }

};

class PK_S_ANS_EXIT : public Packet
{

public:
    PacketType type() { return E_S_ANS_EXIT; }

};

class PK_I_NOTIFY_TERMINAL : public Packet
{
public:
    PacketType type() { return E_I_NOTIFY_TERMINAL; }

};

class PK_C_NOTIFY_HEARTBEAT : public Packet
{
public:
    PacketType type() { return E_C_NOTIFY_HEARTBEAT; }

};

class PK_C_REQ_ID_PW : public Packet
{
public:
    PacketType type() { return E_C_REQ_ID_PW; }

    std::string     id_;
    std::string     password_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << id_;
        stream << password_;
    }

    void decode(Stream &stream) {
        stream >> &id_;
        stream >> &password_;
    }
};

class PK_S_ANS_ID_PW_FAIL : public Packet
{
public:
    PacketType type() { return E_S_ANS_ID_PW_FAIL; }

};

class PK_S_ANS_ID_PW_SUCCESS : public Packet
{
public:
    PacketType type() { return E_S_ANS_ID_PW_SUCCESS; }

    std::string     ip_;
    UInt32     port_;
    std::string     name_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << ip_;
        stream << port_;
        stream << name_;
    }

    void decode(Stream &stream) {
        stream >> &ip_;
        stream >> &port_;
        stream >> &name_;
    }
};

class PK_I_DB_REQ_ID_PW : public Packet
{
public:
    PacketType type() { return E_I_DB_REQ_ID_PW; }

    UInt64     clientId_;
    std::string     id_;
    std::string     password_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << clientId_;
        stream << id_;
        stream << password_;
    }

    void decode(Stream &stream) {
        stream >> &clientId_;
        stream >> &id_;
        stream >> &password_;
    }
};

class PK_I_DB_ANS_ID_PW : public Packet
{
public:
    PacketType type() { return E_I_DB_ANS_ID_PW; }

    UInt64     clientId_;
    UInt64     oidAccountId_;
    Byte     result_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << clientId_;
        stream << oidAccountId_;
        stream << result_;
    }

    void decode(Stream &stream) {
        stream >> &clientId_;
        stream >> &oidAccountId_;
        stream >> &result_;
    }
};

class PK_I_CHTTING_NOTIFY_ID : public Packet
{
public:
    PacketType type() { return E_I_CHTTING_NOTIFY_ID; }

    UInt64     clientId_;
    UInt64     oidAccountId_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << clientId_;
        stream << oidAccountId_;
    }

    void decode(Stream &stream) {
        stream >> &clientId_;
        stream >> &oidAccountId_;
    }
};

class PK_I_DB_REQ_LOAD_DATA : public Packet
{
public:
    PacketType type() { return E_I_DB_REQ_LOAD_DATA; }

    UInt64     clientId_;
    UInt64     oidAccountId_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << clientId_;
        stream << oidAccountId_;
    }

    void decode(Stream &stream) {
        stream >> &clientId_;
        stream >> &oidAccountId_;
    }
};

class PK_I_DB_ANS_PARSE_DATA : public Packet
{
public:
    PacketType type() { return E_I_DB_ANS_PARSE_DATA; }

    UInt64     clientId_;
    std::string     name_;
    Byte     result_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << clientId_;
        stream << name_;
        stream << result_;
    }

    void decode(Stream &stream) {
        stream >> &clientId_;
        stream >> &name_;
        stream >> &result_;
    }
};

class PK_I_LOGIN_NOTIFY_ID_LOADED : public Packet
{
public:
    PacketType type() { return E_I_LOGIN_NOTIFY_ID_LOADED; }

    UInt64     clientId_;
    std::string     name_;
    Byte     result_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << clientId_;
        stream << name_;
        stream << result_;
    }

    void decode(Stream &stream) {
        stream >> &clientId_;
        stream >> &name_;
        stream >> &result_;
    }
};

class PK_C_REQ_REGIST_CHATTING_NAME : public Packet
{
public:
    PacketType type() { return E_C_REQ_REGIST_CHATTING_NAME; }

    std::string     name_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << name_;
    }

    void decode(Stream &stream) {
        stream >> &name_;
    }
};

class PK_C_REQ_CHATTING : public Packet
{
public:
    PacketType type() { return E_C_REQ_CHATTING; }

    std::string     text_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << text_;
    }

    void decode(Stream &stream) {
        stream >> &text_;
    }
};

class PK_S_ANS_CHATTING : public Packet
{
public:
    PacketType type() { return E_S_ANS_CHATTING; }

    std::string     name_;
    std::string     text_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << name_;
        stream << text_;
    }

    void decode(Stream &stream) {
        stream >> &name_;
        stream >> &text_;
    }
};

class PK_S_ANS_NEW_USER_NOTIFY :public Packet
{
public:
    PacketType type() { return E_S_ANS_NEW_USER_NOTIFY; }

    std::string name_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << name_;
    }

    void decode(Stream& stream) {
        stream >> &name_;
    }
};

class PK_S_ANS_USER_LIST :public Packet
{
public:
    PacketType type() { return E_S_ANS_USER_LIST; }

    std::vector<std::string> names_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << (Int32)names_.size();
        for (const auto& name : names_) {
            stream << name;
        }
    }

    void decode(Stream& stream) {
        Int32 size;
        stream >> &size;

        names_.clear();
        for (Int32 i = 0; i < size; i++) {
            std::string name;
            stream >> &name;
            names_.push_back(name);
        }
    }
};

class PK_S_ANS_EXIT_USER :public Packet
{
public:
    PacketType type() { return E_S_ANS_EXIT_USER; }

    std::string name_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << name_;
    }

    void decode(Stream& stream) {
        stream >> &name_;
    }
};
class PK_C_REQ_CHAT_EXIT :public Packet
{
public:
    PacketType type() { return E_C_REQ_CHAT_EXIT; }
    std::string name_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << name_;
    }

    void decode(Stream& stream) {
        stream >> &name_;
    }
};
```

## ServerLibrary\Net\Packet\PacketFactory.h
```h
#pragma once
#include "stdafx.h"
#include "packetHeader.h"
#include "packetClass.h"

#define _packet_factory		PacketFactory::getInstance()

class PacketFactory : public Singleton<PacketFactory>
{
public:
    Packet* getPacket(Int64 packetType) 
    {
        switch (packetType) {
            case E_C_REQ_EXIT:    return new PK_C_REQ_EXIT();
            case E_S_ANS_EXIT:    return new PK_S_ANS_EXIT();
            case E_I_NOTIFY_TERMINAL:    return new PK_I_NOTIFY_TERMINAL();
            case E_C_NOTIFY_HEARTBEAT:    return new PK_C_NOTIFY_HEARTBEAT();
            case E_C_REQ_ID_PW:    return new PK_C_REQ_ID_PW();
            case E_S_ANS_ID_PW_FAIL:    return new PK_S_ANS_ID_PW_FAIL();
            case E_S_ANS_ID_PW_SUCCESS:    return new PK_S_ANS_ID_PW_SUCCESS();
            case E_I_DB_REQ_ID_PW:    return new PK_I_DB_REQ_ID_PW();
            case E_I_DB_ANS_ID_PW:    return new PK_I_DB_ANS_ID_PW();
            case E_I_CHTTING_NOTIFY_ID:    return new PK_I_CHTTING_NOTIFY_ID();
            case E_I_DB_REQ_LOAD_DATA:    return new PK_I_DB_REQ_LOAD_DATA();
            case E_I_DB_ANS_PARSE_DATA:    return new PK_I_DB_ANS_PARSE_DATA();
            case E_I_LOGIN_NOTIFY_ID_LOADED:    return new PK_I_LOGIN_NOTIFY_ID_LOADED();
            case E_C_REQ_REGIST_CHATTING_NAME:    return new PK_C_REQ_REGIST_CHATTING_NAME();
            case E_C_REQ_CHATTING:    return new PK_C_REQ_CHATTING();
            case E_S_ANS_CHATTING:    return new PK_S_ANS_CHATTING();
            case E_S_ANS_NEW_USER_NOTIFY: return new PK_S_ANS_NEW_USER_NOTIFY();
            case E_S_ANS_USER_LIST: return new PK_S_ANS_USER_LIST();
            case E_S_ANS_EXIT_USER:return new PK_S_ANS_EXIT_USER();
            case E_C_REQ_CHAT_EXIT:return new PK_C_REQ_CHAT_EXIT();
        }
        return nullptr;
    }
};
```

## ServerLibrary\Net\Packet\PacketHeader.h
```h
#pragma once
#include "stdafx.h"

#define PACKET_MAKE_DATE "2025/03/01 12:13:55" 
enum PacketType : Int64 {
    E_C_REQ_EXIT = 128,
    E_S_ANS_EXIT = 129,
    E_I_NOTIFY_TERMINAL = 130,
    E_C_NOTIFY_HEARTBEAT = 131,
    E_C_REQ_ID_PW = 132,
    E_S_ANS_ID_PW_FAIL = 133,
    E_S_ANS_ID_PW_SUCCESS = 134,
    E_I_DB_REQ_ID_PW = 135,
    E_I_DB_ANS_ID_PW = 136,
    E_I_CHTTING_NOTIFY_ID = 137,
    E_I_DB_REQ_LOAD_DATA = 138,
    E_I_DB_ANS_PARSE_DATA = 139,
    E_I_LOGIN_NOTIFY_ID_LOADED = 140,
    E_C_REQ_REGIST_CHATTING_NAME = 141,
    E_C_REQ_CHATTING = 142,
    E_S_ANS_CHATTING = 143,
    E_S_ANS_NEW_USER_NOTIFY = 144,
    E_S_ANS_USER_LIST = 145,
    E_S_ANS_EXIT_USER=146,
    E_C_REQ_CHAT_EXIT=147,

};
```

## ServerLibrary\Net\Packet\PacketObfuscation.cpp
```cpp
#pragma once
#include "stdafx.h"
#include "PacketObfuscation.h"

XorObfuscation::XorObfuscation()
{
	key_ = PACKET_MAKE_DATE;
	keyLength_ = (int)key_.length();
}

void XorObfuscation::CalcXor(Byte *packet, int packetOffset, size_t packetLen)
{
	int keyIdx = packetOffset % keyLength_;
	for (int packetIdx = 0; packetIdx < packetLen; ++packetIdx) {
		packet[packetIdx] ^= (Byte)key_[keyIdx++];

		if (keyIdx == keyLength_) {
			keyIdx = 0;
		}
	}
}

void XorObfuscation::encodingHeader(Byte *packet, size_t packetLen)
{
	this->CalcXor(packet, 0, packetLen);
}

void XorObfuscation::encodingData(Byte *packet, size_t packetLen)
{
	this->CalcXor(packet, sizeof(packet_size_t), packetLen);
}

void XorObfuscation::decodingHeader(Byte *packet, size_t packetLen)
{
	this->CalcXor(packet, 0, packetLen);
}

void XorObfuscation::decodingData(Byte *packet, size_t packetLen)
{
	this->CalcXor(packet, sizeof(packet_size_t), packetLen);
}
//--------------------------------------------------------//
PacketObfuscation::PacketObfuscation()
{
	obfuscation_ = new XorObfuscation();
}

PacketObfuscation::~PacketObfuscation()
{
	SAFE_DELETE(obfuscation_);
}

void PacketObfuscation::encodingHeader(Byte *packet, size_t len)
{
	obfuscation_->encodingHeader(packet, len);
}

void PacketObfuscation::encodingData(Byte *packet, size_t len)
{
	obfuscation_->encodingData(packet, len);
}

void PacketObfuscation::decodingHeader(Byte *packet, size_t len)
{
	obfuscation_->decodingHeader(packet, len);
}

void PacketObfuscation::decodingData(Byte *packet, size_t len)
{
	obfuscation_->decodingData(packet, len);
}
```

## ServerLibrary\Net\Packet\PacketObfuscation.h
```h
#pragma once
#include "stdafx.h"


// 난독화 최상위, 다른 난독화 알고리즘은 이 클래스를 상속 받을것
class Obfuscation
{
public:
	virtual void encodingHeader(Byte *packet, size_t packetLen) = 0;
	virtual void encodingData(Byte *packet, size_t packetLen) = 0;
	
	virtual void decodingHeader(Byte *packet, size_t packetLen) = 0;
	virtual void decodingData(Byte *packet, size_t packetLen) = 0;
};

//--------------------------------------------------------//
class XorObfuscation : public Obfuscation
{
	str_t	key_;
	int		keyLength_;

public:
	XorObfuscation();
private:
	void CalcXor(Byte *packet, int packetOffset, size_t packetLen);

	void encodingHeader(Byte *packet, size_t packetLen);
	void encodingData(Byte *packet, size_t packetLen);

	void decodingHeader(Byte *packet, size_t packetLen);
	void decodingData(Byte *packet, size_t packetLen);
};

//--------------------------------------------------------//
// 패킷 난독화용
class PacketObfuscation : public Singleton < PacketObfuscation >
{
	Obfuscation		*obfuscation_;
public:
	PacketObfuscation();
	~PacketObfuscation();

	void encodingHeader(Byte *packet, size_t packetLen);
	void encodingData(Byte *packet, size_t packetLen);

	void decodingHeader(Byte *packet, size_t packetLen);
	void decodingData(Byte *packet, size_t packetLen);
};
```

## ServerLibrary\Net\Packet\Stream.cpp
```cpp
#pragma once
#include "stdafx.h"
#include "Stream.h"

Stream::Stream()
{
	this->initialize();
}

Stream::Stream(UCHAR *stream, size_t size)
{
	this->initialize();
	this->set(stream, size);
}

void Stream::initialize()
{
	readPt_ = 0;
	offset_ = 0;
	ZeroMemory(&stream_, sizeof(stream_));
}

UCHAR *Stream::data()
{
	return stream_.data();
}

size_t Stream::size()
{
	return offset_;
}

void Stream::operator = (Stream &stream)
{
	this->set(stream.data(), stream.size());
}

void Stream::set(UCHAR *data, size_t size)
{
	this->offset_ = size;
	memcpy_s(this->stream_.data(), stream_.size(), (void *)data, size);
}

// write
//------------------------------------------------------------------------//
bool Stream::checkWriteBound(size_t len)
{
	if (offset_ + len > sizeof(stream_)) {
		SLog(L"! socket stream over.");
		ASSERT(FALSE);
		return false;
	}
	return true;
}

#define STREAM_WRITE(value)						\
	INT32 size = sizeof(value);					\
	if (this->checkWriteBound(size) == false) {	\
		return;									\
	}											\
	memcpy_s((void *)(stream_.data() + offset_), stream_.size() - offset_, (const void *)&value, size);\
	offset_ += size;

template<class T>
void Stream::operator << (const T &value)
{
	STREAM_WRITE(value);
}
void Stream::operator << (const bool &value)
{
	STREAM_WRITE(value);
}
void Stream::operator << (const INT8 &value)
{
	STREAM_WRITE(value);
}
void Stream::operator << (const UINT8 &value)
{
	STREAM_WRITE(value);
}
void Stream::operator << (const INT16 &value)
{
	STREAM_WRITE(value);
}
void Stream::operator << (const UINT16 &value)
{
	STREAM_WRITE(value);
}
void Stream::operator << (const INT32 &value)
{
	STREAM_WRITE(value);
}
void Stream::operator << (const UINT32 &value)
{
	STREAM_WRITE(value);
}
void Stream::operator << (const INT64 &value)
{
	STREAM_WRITE(value);
}
void Stream::operator << (const UINT64 &value)
{
	STREAM_WRITE(value);
}

void Stream::operator << (const std::vector<wstr_t> &value)
{
	*this << value.size();
	for (auto i : value) {
		*this << i;
	}
}

void Stream::operator << (const str_t value)
{
	*this << (Int32)value.length();
	for (auto i : value) {
		*this << i;
	}
}

void Stream::operator << (const wstr_t value)
{
	*this << (Int32)(value.length());
	for (auto i : value) {
		*this << i;
	}
}

// read
//------------------------------------------------------------------------//
bool Stream::checkReadBound(size_t len)
{
	if (readPt_ + len > offset_) {
		SLog(L"! readOffset : %d, size: %d, totalOffset = %d", readPt_, len, offset_);
		SLog(L"! socket stream has not more memory.");
		ASSERT(FALSE);
		return false;
	}
	return true;
}

void Stream::read(void *retVal, size_t len)
{
	memcpy_s(retVal, len, (void *)(stream_.data() + readPt_), len);
	readPt_ += len;
}

#define STREAM_READ(type, retVal)				\
	size_t size = sizeof(type);					\
	if (this->checkReadBound(size) == false) {	\
		return;									\
	}											\
	this->read((void *)(retVal), size);	

template<class T>
void Stream::operator >> (T *retVal)
{
	STREAM_READ(T, retVal);
}

void Stream::operator >> (bool *retVal)
{
	STREAM_READ(bool, retVal);
}
void Stream::operator >> (INT8 *retVal)
{
	STREAM_READ(INT8, retVal);
}
void Stream::operator >> (UINT8 *retVal)
{
	STREAM_READ(UINT8, retVal);
}
void Stream::operator >> (INT16 *retVal)
{
	STREAM_READ(INT16, retVal);
}
void Stream::operator >> (UINT16 *retVal)
{
	STREAM_READ(UINT16, retVal);
}
void Stream::operator >> (INT32 *retVal)
{
	STREAM_READ(INT32, retVal);
}
void Stream::operator >> (UINT32 *retVal)
{
	STREAM_READ(UINT32, retVal);
}
void Stream::operator >> (INT64 *retVal)
{
	STREAM_READ(INT64, retVal);
}
void Stream::operator >> (UINT64 *retVal)
{
	STREAM_READ(UINT64, retVal);
}

void Stream::operator >> (std::vector<wstr_t> *retVal)
{
	size_t size;
	*this >> &size;

	for (size_t i = 0; i < size; ++i) {
		wstr_t tmp;
		*this >> &tmp;
		retVal->push_back(tmp);
	}
}

void Stream::operator >> (str_t *retVal)
{
	INT32 size;
	*this >> &size;
	if (this->checkReadBound(size) == false) {
		return;
	}

	char *buf = new char[size + 1];
	this->read((void *)(buf), size * sizeof(CHAR));
	buf[size] = '\0';

	retVal->clear();
	*retVal = buf;

	delete buf;
}

void Stream::operator >> (wstr_t *retVal)
{
	INT32 size;
	*this >> &size;
	if (this->checkReadBound(size) == false) {
		return;
	}

	WCHAR *buf = new WCHAR[size + 1];
	this->read((void *)(buf), size * sizeof(WCHAR));
	buf[size] = '\0';

	retVal->clear();
	*retVal = buf;

	delete buf;
}
```

## ServerLibrary\Net\Packet\Stream.h
```h
#pragma once
#include "stdafx.h"

class Stream
{
	size_t offset_;
	size_t readPt_;
	array <UCHAR, SOCKET_BUF_SIZE> stream_;

public:
	Stream();
	Stream(UCHAR *stream, size_t size);
	void initialize();

	UCHAR *data();
	size_t size();

	void operator = (Stream &stream);
	void set(UCHAR *stream, size_t size);

	// write
	//------------------------------------------------------------------------//
	bool checkWriteBound(size_t len);


	template<class T>
	void operator << (const T &value);
	void operator << (const bool &value);
	void operator << (const INT8 &value);
	void operator << (const UINT8 &value);
	void operator << (const INT16 &value);
	void operator << (const UINT16 &value);
	void operator << (const INT32 &value);
	void operator << (const UINT32 &value);
	void operator << (const INT64 &value);
	void operator << (const UINT64 &value);

	void operator << (const std::vector<wstr_t> &value);

	void operator << (const str_t value);
	void operator << (const wstr_t value);

	// read
	//------------------------------------------------------------------------//
	bool checkReadBound(size_t len);
	void read(void *retVal, size_t len);

	template<class T>
	void operator >> (T *retVal);

	void operator >> (bool *retVal);
	void operator >> (INT8 *retVal);
	void operator >> (UINT8 *retVal);
	void operator >> (INT16 *retVal);
	void operator >> (UINT16 *retVal);
	void operator >> (INT32 *retVal);
	void operator >> (UINT32 *retVal);
	void operator >> (INT64 *retVal);
	void operator >> (UINT64 *retVal);

	void operator >> (std::vector<wstr_t> *retVal);

	void operator >> (str_t *retVal);
	void operator >> (wstr_t *retVal);
};
```

## ServerLibrary\Net\Packet.h
```h
#include "packetHeader.h"
#include "Stream.h"

struct Packet {
    void encode(Stream &stream) {}
    void decode(Stream &stream) {}
};

struct PK_C_REQ_ID_PW : Packet
{
    int packetType() { return E_C_REQ_ID_PW; }
    std::string     id;
    std::string     password;

    void encode(Stream &stream) {
        stream << id;
        stream << password;
    }

    void decode(Stream &stream) {
        stream >> &id;
        stream >> &password;
    }
};

struct PK_S_REQ_ID_ID_PW : Packet
{
    int packetType() { return E_S_REQ_ID_ID_PW; }
    bool     result;

    void encode(Stream &stream) {
        stream << result;
    }

    void decode(Stream &stream) {
        stream >> &result;
    }
};

struct PK_C_NOTIFY_HEARTBEET : Packet
{
    int packetType() { return E_C_NOTIFY_HEARTBEET; }
};

struct PK_C_REQ_CHATTING : Packet
{
    int packetType() { return E_C_REQ_CHATTING; }
    std::string     text;

    void encode(Stream &stream) {
        stream << text;
    }

    void decode(Stream &stream) {
        stream >> &text;
    }
};

struct PK_S_REQ_CHATTING : Packet
{
    int packetType() { return E_S_REQ_CHATTING; }
    std::string     id;
    std::string     text;

    void encode(Stream &stream) {
        stream << id;
        stream << text;
    }

    void decode(Stream &stream) {
        stream >> &id;
        stream >> &text;
    }
};
```

## ServerLibrary\Net\PacketHeader.h
```h
#pragma once
#include "../stdafx.h"

enum EPacket {
    /*0*/    E_C_REQ_ID_PW,
    /*1*/    E_S_REQ_ID_ID_PW,
    /*2*/    E_C_NOTIFY_HEARTBEET,
    /*3*/    E_C_REQ_CHATTING,
    /*4*/    E_S_REQ_CHATTING,
};
```

## ServerLibrary\Net\PacketManager.h
```h
#pragma once
#include "stdafx.h"

class Packet
{
	void encode()
	{
		

	}

	void decode()
	{

	}
};

class PacketManager
{
	ThreadJobQueue<Packet *> packetQueue_;

public:
	bool inputPacket(Packet *packet)
	{
		packetQueue_.push(packet);
	}

	// 큐에서 하나 뽑아서 워커에게 나눠준다.
	Packet *getPacket()
	{
		Packet *packet;
		if (!packetQueue_.pop(packet)) {
			packetQueue_.swap();
			return nullptr;
		}
		return packet;
	}
};
```

## ServerLibrary\Net\Server.cpp
```cpp
#include "stdafx.h"
#include "Server.h"

Server::Server(ContentsProcess *contentsProcess)
{
	SLog(L"# Initialze network base");
	
	contentsProcess_ = contentsProcess;
	status_ = SERVER_STOP;

	xml_t config;
	if (!loadConfig(&config)) {
		return;
	}
	this->initialize(&config);


	_db_manager;
}

Server::~Server()
{
	shutdownServer();

	status_ = SERVER_STOP;
	SAFE_DELETE(contentsProcess_);

	SLog(L"# End network base");
}

void Server::initialize(xml_t *config)
{
	_terminal.run(this);

	TaskManager::getInstance();

	//서버 설정
	xmlNode_t *root = config->FirstChildElement("App")->FirstChildElement("Server");
	if (!root) {
		SLog(L"@ not exist server setting");
		return;
	}
	xmlNode_t *elem = root->FirstChildElement("IP");
	strcpy_s(ip_, elem->GetText());

	elem = root->FirstChildElement("Port");
	sscanf_s(elem->GetText(), "%d", &port_);

	elem = root->FirstChildElement("ThreadCount");
	sscanf_s(elem->GetText(), "%d", &workerThreadCount_);

	status_ = SERVER_INITIALZE;
	SLog(L"* IO worker thread count : %d", workerThreadCount_);

	root = config->FirstChildElement("App");
	elem = root->FirstChildElement("Name");

	SLog(L"### %S start!!! ###", elem->GetText());
}

SERVER_STATUS &Server::status()
{
	return status_;
}

void Server::putPackage(Package *package)
{
	contentsProcess_->putPackage(package);
}
```

## ServerLibrary\Net\Server.h
```h
#pragma once
#include "stdafx.h"
#include "SessionManager.h"

// 서버의 공통 모듈 처리

enum SERVER_STATUS {
	SERVER_STOP,
	SERVER_INITIALZE,
	SERVER_READY,
};

class Server
{
protected:
	char					ip_[16];
	int						port_;
	int						workerThreadCount_;

	SERVER_STATUS			status_;
	ContentsProcess			*contentsProcess_;

public:
	Server(ContentsProcess *contentsProcess);
	virtual ~Server();

	virtual void			initialize(xml_t *config);

	virtual bool			run() = 0;
	SERVER_STATUS			&status();

	void					putPackage(Package *package);
};
```

## ServerLibrary\Net\Session.cpp
```cpp
#include "stdafx.h"
#include "Session.h"
#include "./Iocp/IOCPServer.h"

Session::Session()
{
	type_ = SESSION_TYPE_CLIENT;
	this->updateHeartBeat();
}

Session::~Session()
{
	this->onClose();
}

bool Session::setSocketOpt()
{
#ifdef linux
	int keepAlive = 1;
	int keepAliveIdle = 1;
	int keepAliveCnt = 3;
	int keepAliveInterval = 3;

	int ret;
	ret = ::setsockopt(socketData_.socket_, SOL_SOCKET, SO_KEEPALIVE, &keepAlive, sizeof(keepAlive));
	if (ret == SOCKET_ERROR) {
		return false;
	}
	ret = ::setsockopt(socketData_.socket_, SOL_TCP, SO_KEEPIDLE, &keepAliveIdle, sizeof(keepAliveIdle));
	if (ret == SOCKET_ERROR) {
		return false;
	}
	ret = ::setsockopt(socketData_.socket_, SOL_TCP, SO_KEEPCNT, &keepAliveCnt, sizeof(keepAliveCnt));
	if (ret == SOCKET_ERROR) {
		return false;
	}
	ret = ::setsockopt(socketData_.socket_, SOL_TCP, SO_KEEPINTVL, &keepAliveInterval, sizeof(keepAliveInterval));
	if (ret == SOCKET_ERROR) {
		return false;
	}
#else
	tcp_keepalive keepAliveSet = { 0 }, returned = { 0 };
	keepAliveSet.onoff = 1;
	keepAliveSet.keepalivetime = 3000;        
	keepAliveSet.keepaliveinterval = 3000;    

	DWORD dwBytes;
	if (WSAIoctl(socketData_.socket_, SIO_KEEPALIVE_VALS, &keepAliveSet, sizeof(keepAliveSet), &returned, sizeof(returned), &dwBytes, NULL, NULL) != 0) {
		return false;
	}
#endif
	return true;
}

bool Session::onAccept(SOCKET socket, SOCKADDR_IN addrInfo)
{
	socketData_.socket_ = socket;
	int addrLen;
	getpeername(socketData_.socket_, (struct sockaddr *)&socketData_.addrInfo_, &addrLen);
	socketData_.addrInfo_ = addrInfo;
	if (!this->setSocketOpt()) {
		return false;
	}
	return true;
}

void Session::onClose(bool force)
{
	if (force) {
		_session_manager.forceCloseSession(this);
	}
	else {
		_session_manager.closeSession(this);
	}
}

SOCKET& Session::socket()
{
	return socketData_.socket_;
}

wstr_t Session::clientAddress()
{
	array<char, SIZE_64> ip;
	inet_ntop(AF_INET, &(socketData_.addrInfo_.sin_addr), ip.data(), ip.size());

	array<WCHAR, SIZE_64> wip;
	StrConvA2W(ip.data(), wip.data(), wip.max_size());
	wstr_t stringData = wip.data();

	return stringData;
}

oid_t Session::id()
{
	return id_;
}

void Session::setId(oid_t id)
{
	id_ = id;
}

int8_t Session::type()
{
	return type_;
}

void Session::setType(int8_t type)
{
	type_ = type;
}

tick_t Session::heartBeat()
{
	return lastHeartBeat_;
}

void Session::updateHeartBeat()
{
	lastHeartBeat_ = CLOCK.systemTick();
}
```

## ServerLibrary\Net\Session.h
```h
#pragma once
#include "stdafx.h"


struct SOCKET_DATA {
	SOCKET				socket_;
	SOCKADDR_IN			addrInfo_;
};

enum {
	SESSION_TYPE_TERMINAL,
	SESSION_TYPE_CLIENT,
};

class Session
{
protected:
	SOCKET_DATA		    socketData_;
	oid_t				id_;
	int8_t				type_;
	tick_t				lastHeartBeat_;
	bool				setSocketOpt();

public:
    Session();
    virtual ~Session();

	virtual bool		onAccept(SOCKET socket, SOCKADDR_IN addrInfo);

	virtual void		onSend(size_t transferSize) = 0;
	virtual void		sendPacket(Packet *packet) = 0;
	
	virtual Package*	onRecv(size_t transferSize) = 0;
	virtual void		recvStandBy() {};

    virtual void		onClose(bool force = false);

	SOCKET&				socket();
    wstr_t				clientAddress();

	oid_t				id();
	void				setId(oid_t id);

	int8_t				type();
	void				setType(int8_t type);

	tick_t				heartBeat();
	void				updateHeartBeat();
};
```

## ServerLibrary\Net\SessionManager.cpp
```cpp
#include "stdafx.h"
#include "SessionManager.h"
#include "./Iocp/IOCPServer.h"

SessionManager::SessionManager(int maxConnection)
	: lock_(L"SessionManager")
{
	sessionSeed_ = 1;
	maxConnection_ = maxConnection;
	this->commandFuncInitialize();
}

SessionManager::~SessionManager()
{
	vector<Session *> removeSessionVec;
	removeSessionVec.resize(sessionList_.size());
	std::copy(sessionList_.begin(), sessionList_.end(), removeSessionVec.begin());
	for (auto session : removeSessionVec) {
		session->onClose();
	}
	sessionList_.clear();
}

list<Session*>& SessionManager::sessionList()
{
	return sessionList_;
}

oid_t SessionManager::createSessionId()
{
	return sessionSeed_++;
}

bool SessionManager::addSession(Session *session)
{
	SAFE_LOCK(lock_);
	auto findSession = std::find(sessionList_.begin(), sessionList_.end(), session);
	if (findSession != sessionList_.end()) {
		return false;
	}
	if (sessionCount_ > maxConnection_) {
		SLog(L"* session so busy. count[%d]", sessionCount_);
		return false;
	}

	session->setId(this->createSessionId());
	sessionList_.push_back(session);
	++sessionCount_;
	return true;
}


bool SessionManager::closeSession(Session *session)
{
	SAFE_LOCK(lock_);
	if (session == nullptr) {
		return false;
	}
	auto findSession = std::find(sessionList_.begin(), sessionList_.end(), session);
	if (findSession != sessionList_.end()) {
		Session *delSession = *findSession;
		SLog(L"* detected close by client [%s]", delSession->clientAddress().c_str());
		::closesocket(delSession->socket());

		sessionList_.remove(delSession);
		--sessionCount_;
		SAFE_DELETE(delSession);
		return true;
	}
	return false;
}


void SessionManager::forceCloseSession(Session *session)
{
	SAFE_LOCK(lock_);
	if (!session) {
		return;
	}

	//우아한 종료 유도. 
	LINGER linger;
	linger.l_onoff = 1;   //사용
	linger.l_linger = 0;  //대기시간, 0일시 완료 안된 패킷 버리고 즉시 종료.

	::setsockopt(session->socket(), SOL_SOCKET, SO_LINGER, (char *)&linger, sizeof(linger));
	this->closeSession(session);
}

Session* SessionManager::session(oid_t id)
{
	SAFE_LOCK(lock_);
	Session *findSession = nullptr;

	for (auto session : sessionList_) {
		if (session->id() == id) {
			findSession = session;
			break;
		}
	}
	
	return findSession;
}

void SessionManager::runCommand(wstr_t cmdLine)
{
	std::size_t found = cmdLine.find(L' ');
	wstr_t command;
	wstr_t arg;
	if (found != wstr_t::npos) {
		command = cmdLine.substr(0, found);
		arg = cmdLine.substr(found);
	}
	else {
		command = cmdLine;
	}

	auto itr = serverCommand_.find(command);
	if (itr == serverCommand_.end()) {
		return;
	}

	auto cmdFunc = serverCommand_.at(command);
	if (cmdFunc) {
		cmdFunc(&sessionList_, &arg);
	}
}

// 치트키
void SessionManager::commandFuncInitialize()
{
#if 0

    auto notiyFunc = [](SessionList *sessionList, wstr_t *arg) {
        auto eachFunc = [arg](void *atom) {
            Session *session = (Session*)atom;
			if (session->type() == SESSION_TYPE_TERMINAL) {
				return;
			}
            array<CHAR, SIZE_256> tmpBuf;
            StrConvW2A((WCHAR*)arg->c_str(), tmpBuf.data(), tmpBuf.size());

			PK_S_ANS_CHATTING retPacket;
			retPacket.id_ = "Server";
			retPacket.text_ = "* Notity : ";
			retPacket.text_ += tmpBuf.data();

			session->sendPacket(&retPacket);
        };

		for (auto session : *sessionList) {
			eachFunc(session);
		}
    };

    auto kickoffFunc = [](SessionList *sessionList, wstr_t *arg){
        vector<Session *> removeSessionVec;
        auto eachFunc = [&removeSessionVec, arg](void *atom) {
            Session *session = (Session*)atom;
			if (session->type() == SESSION_TYPE_TERMINAL) {
				return;
			}

			PK_S_ANS_CHATTING retPacket;
			retPacket.id_ = "Server";
			retPacket.text_ = "! Kick off by Server";
			session->sendPacket(&retPacket);

            removeSessionVec.push_back(session);
        }; 
		for (auto session : *sessionList) {
			eachFunc(session);
		}

        for (auto session : removeSessionVec) {
			session->onClose();
        }
    };

    auto exitFunc = [](SessionList *sessionList, wstr_t *arg){
        _shutdown = true;
    };

    //명령어 등록
    serverCommand_.insert(make_pair(L"/notify", notiyFunc));
	serverCommand_.insert(make_pair(L"/kickoff", kickoffFunc));
	serverCommand_.insert(make_pair(L"/exit", exitFunc));
#endif
}
```

## ServerLibrary\Net\SessionManager.h
```h
#pragma once
#include "stdafx.h"
#include "Session.h"



#define SESSION_CAPACITY		(5000)
#define _session_manager		SessionManager::getInstance()

class SessionManager : public Singleton<SessionManager>
{
    typedef list<Session*>		SessionList;

    SessionList		            sessionList_;
	int									sessionCount_;
	int									maxConnection_;
    Lock								lock_;

	oid_t								sessionSeed_;			

	// 서버 수동 명령어
    typedef std::function<void (SessionList *sessionList, wstr_t *arg)> cmdFunc;
	unordered_map<wstr_t, cmdFunc>   serverCommand_;

public:
	SessionManager(int maxConnection = SESSION_CAPACITY);
	~SessionManager();
	oid_t				createSessionId();

	bool				addSession(Session *session);

	list<Session*>		&sessionList();
	bool				closeSession(Session *session);
	void				forceCloseSession(Session *session);

	Session				*session(oid_t id);

    void                runCommand(wstr_t cmd);
    void                commandFuncInitialize();
};
```

## ServerLibrary\Net\SessionMonitor.cpp
```cpp
#include "stdafx.h"
#include "SessionMonitor.h"

SessionMonitor::SessionMonitor() 
{
	static bool init = false;
	if (init) {
		return;
	}
	init = true;

	const int MONITOR_REPORTING_SEC = 1;
	TaskManager::getInstance().add(this, MONITOR_REPORTING_SEC, TICK_INFINTY);
}

void SessionMonitor::tick()
{
	//15초간 반응 없으면 끊기
	const int MAX_HEART_BEAT = 15 * 1000;
	auto list = _session_manager.sessionList();
	tick_t now = CLOCK.systemTick();

	for (auto session : list) {
		if (session->type() != SESSION_TYPE_CLIENT) {
			continue;
		}

		tick_t lastTick = session->heartBeat();
		if (now - lastTick > MAX_HEART_BEAT) {
			SLog(L"* [%s] Closing by heartBeat", session->clientAddress().c_str());
			session->onClose(true);
		}
	}
}
```

## ServerLibrary\Net\SessionMonitor.h
```h
#pragma once
#include "stdafx.h"

class SessionMonitor : public Work
{
public :
	SessionMonitor();
	void tick();
};
static SessionMonitor sessionMonitor;
```

## ServerLibrary\Net\Stream.h
```h
#pragma once
#include "stdafx.h"
using namespace std;

class Stream
{
	size_t offset_;
	size_t readPt_;
	array <UCHAR, SOCKET_BUF_SIZE> stream_;

public:
	Stream()
	{
		readPt_ = 0;
		offset_ = 0;
		ZeroMemory(&stream_, sizeof(stream_));
	}

	UCHAR *stream()
	{
		return stream_.data();
	}

	size_t size()
	{
		return offset_;
	}

	void operator = (Stream &stream)
	{
		this->set(stream.stream(), stream.size());
	}

	void set(UCHAR *stream, size_t size)
	{
		this->offset_ = size;
		memcpy_s(this->stream_.data(), stream_.size(), (void *)stream, size);
	}

	// write
	//------------------------------------------------------------------------//
	bool checkWriteBound(size_t len)
	{
		if (offset_ + len > sizeof(stream_)) {
			SLog(L"! socket stream over.");
			ASSERT(FALSE);
			return false;
		}
		return true;
	}

	template<typename T>
	void operator << (const T &value)
	{
		size_t size = sizeof(value);
		if (this->checkWriteBound(size) == false) {
			return;
		}
		
		memcpy_s((void *)(stream_.data() + offset_), stream_.size() - offset_, (const void *)&value, size);
		offset_ += size;
	}

	template<class T>
	void operator << (const std::vector<T> &value)
	{
		*this << value.size();
		for (auto i : value) {
			*this << i;
		}
	}

	void operator << (std::string value)
	{
		*this << value.length();
		for (auto i : value) {
			*this << i;
		}
	}

	void operator << (wstr_t value)
	{
		*this << (value.length());
		for (auto i : value) {
			*this << i;
		}
	}

	// read
	//------------------------------------------------------------------------//
	bool checkReadBound(size_t len) 
	{
		if (readPt_ + len > offset_) {
			SLog(L"! readOffset : %d, size: %d, totalOffset = %d", readPt_, len, offset_);
			SLog(L"! socket stream has not more memory.");
			ASSERT(FALSE);
			return false;
		}
		return true;
	}

	void read(void *retVal, size_t len)
	{
		memcpy_s(retVal, len, (void *)(stream_.data() + readPt_), len);
		readPt_ += len;
	}

	template<typename T>
	void operator >> (T *retVal)
	{
		size_t size = sizeof(*retVal);
		if (this->checkReadBound(size) == false) {
			return;
		}
		this->read((void *)(retVal), sizeof(T));
	}

	void operator >> (std::string *retVal)
	{
		size_t size;
		*this >> &size;
		if (this->checkReadBound(size) == false) {
			return;
		}

		char *buf = new char[size + 1];
		this->read((void *)(buf), size * sizeof(CHAR));
		buf[size] = '\0';

		retVal->clear();
		*retVal = buf;

		delete buf;
	}

	void operator >> (wstr_t *retVal)
	{
		size_t size;
		*this >> &size;
		if (this->checkReadBound(size) == false) {
			return;
		}

		WCHAR *buf = new WCHAR[size + 1];
		this->read((void *)(buf), size * sizeof(WCHAR));
		buf[size] = '\0';

		retVal->clear();
		*retVal = buf;

		delete buf;
	}

	template<class T>
	void operator >> (std::vector<T> *retVal)
	{
		size_t size;
		*this >> &size;

		for (size_t i = 0; i < size; ++i) {
			T tmp;
			*this >> &tmp;
			retVal->push_back(tmp);
		}
	}
};
```

## ServerLibrary\Net\Terminal\Terminal.cpp
```cpp
#include "stdafx.h"
#include "Terminal.h"
#include "../Packet/PacketAnalyzer.h"

Terminal::Terminal(Server *server, wstr_t name)
{
	server_ = server;
	name_ = name;
}

Terminal::~Terminal()
{
	status_ = TERMINAL_STOP;
}

void Terminal::initialize(xmlNode_t *config)
{
	xmlNode_t *elem;

	elem = config->FirstChildElement("IP");
	strcpy_s(ip_, elem->GetText());

	elem = config->FirstChildElement("Port");
	sscanf_s(elem->GetText(), "%d", &port_);

	this->run();
}

TERMINAL_STATUS& Terminal::status()
{
	return status_;
}

void Terminal::sendPacket(Packet *packet)
{
	if (status_ == TERMINAL_READY) {
		session_.sendPacket(packet);
	}
}

const char *Terminal::ip()
{
	return ip_;
}

int Terminal::port()
{
	return port_;
}

void Terminal::connectProcess()
{
CONNECT_START:
	int tryCount = 0;
	while (_shutdown == false) {
		if (session_.connectTo(ip_, port_)) {
			break;
		}
		SLog(L"* try connect [%s] server[%S]:[%d]... [%d]", name_.c_str(), ip_, port_, tryCount++);
		Sleep(1000);        
	}
	status_ = TERMINAL_READY;

	// 자신이 터미널 세션임을 알려준다.
	PK_I_NOTIFY_TERMINAL terminalPacket;
	this->sendPacket(&terminalPacket);

	SLog(L"* [%s]terminal connect [%S]:[%d] ready", name_.c_str(), ip_, port_);
	while (_shutdown == false) {
		Package *package = session_.onRecv(0);

		if (package == nullptr) {
			SLog(L"! termnal [%s] disconnected ! IP[%S] Port[%d]", name_.c_str(),ip_,port_);
			session_.onClose();
			goto CONNECT_START;
		}

		server_->putPackage(package);
	}
}

void Terminal::run()
{
	processThread_ = MAKE_THREAD(Terminal, connectProcess);
}
```

## ServerLibrary\Net\Terminal\Terminal.h
```h
#pragma once
#include "stdafx.h"

// 터미널 쓰레드, 타 서버와 연결해서 데이터 송수신에 사용한다.
enum TERMINAL_STATUS {
	TERMINAL_STOP,
	TERMINAL_READY,
};

class Server;
class Terminal
{
protected:
	Server					*server_;
	wstr_t					name_;
	TERMINAL_STATUS			status_;

	char					ip_[16];
	int						port_;

	TerminalSession			session_;

	Thread					*processThread_;

public:
	Terminal(Server *server, wstr_t name);
	virtual ~Terminal();
	TERMINAL_STATUS &status();

	void		initialize(xmlNode_t *config);
	void		sendPacket(Packet *packet);
	const char *ip();
	int			port();

private:
	void		connectProcess();
	void		run();
};
```

## ServerLibrary\Net\Terminal\TerminalManager.cpp
```cpp
#pragma once
#include "stdafx.h"

TerminalManager::TerminalManager()
{
}

TerminalManager::~TerminalManager()
{
	for (auto itr : terminalPool_) {
		auto terminal = itr.second;
		SAFE_DELETE(terminal);
	}
}

void TerminalManager::initialize(xml_t *config)
{
	xmlNode_t *root = config->FirstChildElement("App")->FirstChildElement("Terminal");
	xmlHandle_t terminalNode = TiXmlHandle(root);
	if (!root) {
		SLog(L"@ not exist terminal setting");
		return;
	}

	xmlNode_t *elem = terminalNode.FirstChildElement().Element();
	while (elem) {
		array<WCHAR, _MAX_PATH> terminalName;
		StrConvA2W((char *)elem->Value(), terminalName.data(), terminalName.max_size());

		Terminal *terminal = new Terminal(server_, terminalName.data());
		terminal->initialize(elem);
		this->put(terminalName.data(), terminal);

		elem = elem->NextSiblingElement();
	}

	SLog(L"### Terminal set ###");
}

void TerminalManager::put(wstr_t serverName, Terminal *terminal)
{
	terminalPool_.insert(make_pair(serverName, terminal));
}

Terminal* TerminalManager::get(wstr_t name)
{
	auto itr = terminalPool_.find(name);
	if (itr == terminalPool_.end()) {
		return nullptr;
	}
	return terminalPool_.at(name);
}

bool TerminalManager::isTerminal(const char *ip)
{
	for (auto terminal : terminalPool_) {
		if (!strcmp(terminal.second->ip(), ip)) {
			return true;
		}
	}
	return false;
}

void TerminalManager::run(Server *server)
{
	server_ = server;

	xml_t config;
	if (!loadConfig(&config)) {
		return;
	}
	this->initialize(&config);
}
```

## ServerLibrary\Net\Terminal\TerminalManager.h
```h
#pragma once
#include "stdafx.h"

#define _terminal			TerminalManager::getInstance()

// 다른 서버간의 연결을 위한 통로
class TerminalManager : public Singleton<TerminalManager>
{
	unordered_map<wstr_t, Terminal*> terminalPool_;
	Server						*server_;

public:
	TerminalManager();
	virtual ~TerminalManager();

	void initialize(xml_t *config);

	void put(wstr_t serverName, Terminal *terminal);
	Terminal* get(wstr_t name);
	
	bool isTerminal(const char *ip);
	void run(Server *server);
};
```

## ServerLibrary\Net\Terminal\TerminalSession.cpp
```cpp
#pragma once
#include "stdafx.h"

bool TerminalSession::connectTo(char *ip, int port)
{
	socketData_.socket_ = ::socket(AF_INET, SOCK_STREAM, 0);
	if (socketData_.socket_ == INVALID_SOCKET) {
		SLog(L"! terminal socket fail");
		return false;
	}
	ZeroMemory(&socketData_.addrInfo_, sizeof(socketData_.addrInfo_));
	socketData_.addrInfo_.sin_family = AF_INET;
	socketData_.addrInfo_.sin_port = htons(port);
	inet_pton(AF_INET, ip, &(socketData_.addrInfo_.sin_addr));
	
	this->setSocketOpt();

	int ret = ::connect(socketData_.socket_, (sockaddr *)&socketData_.addrInfo_, sizeof(socketData_.addrInfo_));
	if (ret == SOCKET_ERROR) {
		SLog(L"! terminal socket connect fail");
		return false;
	}
	return true;
}

void TerminalSession::onSend(size_t transferSize)
{
}

void TerminalSession::sendPacket(Packet *packet)
{
	Stream stream;
	packet->encode(stream);

	packet_size_t offset = 0;
	array<char, SOCKET_BUF_SIZE> buffer;
	const size_t packetHeaderSize = sizeof(packet_size_t);


	packet_size_t packetLen[1] = { (packet_size_t)packetHeaderSize + (packet_size_t)stream.size(), };
	memcpy_s(buffer.data() + offset, buffer.max_size(), (void *)packetLen, packetHeaderSize);
	offset += packetHeaderSize;

	PacketObfuscation::getInstance().encodingHeader((Byte*)buffer.data(), packetHeaderSize);
	PacketObfuscation::getInstance().encodingData((Byte*)stream.data(), stream.size());

	memcpy_s(buffer.data() + offset, buffer.max_size(), stream.data(), packetLen[0]);
	offset += (packet_size_t)stream.size();

	::send(socketData_.socket_, buffer.data(), offset, 0);
}

Package* TerminalSession::onRecv(size_t transferSize)
{
	array<Byte, SOCKET_BUF_SIZE> rowData;
	int ret = ::recv(socketData_.socket_, (char *)rowData.data(), (int)rowData.size(), 0);
	if (ret <= 0) {
		return nullptr;
	}
    
	packet_size_t offset = 0;
	packet_size_t packetLen[1] = { 0, };

	memcpy_s((void *)packetLen, sizeof(packetLen), (void *)rowData.data(), sizeof(packetLen));
	PacketObfuscation::getInstance().decodingHeader((Byte*)packetLen, sizeof(packetLen));

	while (ret < (int)packetLen[0]) {
		int len = ret;
		ret += ::recv(socketData_.socket_, (char *)rowData.data() + len, (int)rowData.size() - len, 0);
	}

	offset += sizeof(packetLen);
	PacketObfuscation::getInstance().decodingData((Byte*)rowData.data() + offset, packetLen[0] - offset);

	Packet *packet = PacketAnalyzer::getInstance().analyzer((char *)rowData.data() + offset, packetLen[0]);
	if (packet == nullptr) {
		return nullptr;
	}

	Package *package = new Package(this, packet);
	return package;
}
```

## ServerLibrary\Net\Terminal\TerminalSession.h
```h
#pragma once
#include "stdafx.h"

class TerminalSession : public Session
{
public:
	bool		connectTo(char *ip, int port);
	void		onSend(size_t transferSize);
	void		sendPacket(Packet *packet);

	Package*	onRecv(size_t transferSize);
};
```

## ServerLibrary\Net\Winsocket.h
```h
#pragma once
#include "stdafx.h"

class WinSocket
{
	WSADATA            wsa_;

public:
	WinSocket()
	{
		static bool init = false;
		if (init) {
			return;
		}

		if (WSAStartup(MAKEWORD(2, 2), &wsa_) != 0) {
			printf("! wsa startup fail\n");
			exit(0);
		}

		init = true;
		printf("### WSA 2.2 set complet.\n");
	}
	~WinSocket()
	{
		WSACleanup();
	}
};

static WinSocket winsocket;
```

## ServerLibrary\ServerLibrary\x64\Debug\ServerLibrary.tlog\ServerLibrary.lastbuildstate
```lastbuildstate
PlatformToolSet=v143:VCToolArchitecture=Native64Bit:VCToolsVersion=14.41.34120:TargetPlatformVersion=10.0.26100.0:
Debug|x64|C:\github\GameServer_Programming\ServerLibrary\|
```

## ServerLibrary\ServerLibrary\x64\Debug\ServerLibrary.tlog\unsuccessfulbuild
```

```

## ServerLibrary\ServerLibrary\x64\Debug\ServerLibrary.vcxproj.FileListAbsolute.txt
```txt

```

## ServerLibrary\ServerLibrary.h
```h
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
// TODO: 공용 매크로

#if _DEBUG
#define CONTEXT_SWITCH		Sleep(1)
#else
#define CONTEXT_SWITCH		::SwitchToThread()
#endif

typedef void(*Function)(void *);

//기타 유틸
#include "./Util/csv_parser/csv_parser.hpp"
#include "./Util/tinyXml/tinyxml.h"

// TODO: 필수 헤더 파일
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

//패킷들
#include "./Net/Packet/Stream.h"
#include "./Net/Packet/PacketHeader.h"
#include "./Net/Packet/PacketClass.h"
#include "./Net/Packet/PacketAnalyzer.h"
#include "./Net/Packet/PacketFactory.h"
#include "./Net/Packet/Package.h"
#include "./Net/Packet/PacketObfuscation.h"

//컨텐츠 관련
#include "./Contents/ContentsProcess.h"

//서버
#include "./Net/Session.h"
#include "./Net/SessionManager.h"
#include "./Net/Server.h"

#include "./Net/Iocp/IOCPServer.h"
#include "./Net/Iocp/IOCPSession.h"
#include "./Net/SessionMonitor.h"

//터미널
#include "./Net/Terminal/TerminalSession.h"
#include "./Net/Terminal/Terminal.h"
#include "./Net/Terminal/TerminalManager.h"

//DB
#include "./Database/ADODatabase.h"
#include "./Database/Query.h"
#include "./Database/DBManager.h"

// 전역 변수
#include "Shutdown.h"
```

## ServerLibrary\Shutdown.cpp
```cpp
#include "stdafx.h"
#include "Shutdown.h"

bool _shutdown = false;
void shutdownServer()
{
	SLog(L"### server shutdown!!! ###");

}
```

## ServerLibrary\Shutdown.h
```h
#pragma once
#include "stdafx.h"
//-------------------------------------------------------------------//
extern bool _shutdown;
extern void shutdownServer();
```

## ServerLibrary\stdafx.cpp
```cpp
// stdafx.cpp : source file that includes just the standard includes
// ServerLibrary.pch will be the pre-compiled header
// stdafx.obj will contain the pre-compiled type information

#include "stdafx.h"

// TODO: reference any additional headers you need in STDAFX.H
// and not in this file
```

## ServerLibrary\stdafx.h
```h
// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently, but
// are changed infrequently
//

#pragma once

#include "targetver.h"

#define WIN32_LEAN_AND_MEAN             // Exclude rarely-used stuff from Windows headers

#include "ServerLibrary.h"
```

## ServerLibrary\targetver.h
```h
#pragma once

// Including SDKDDKVer.h defines the highest available Windows platform.

// If you wish to build your application for a previous Windows platform, include WinSDKVer.h and
// set the _WIN32_WINNT macro to the platform you wish to support before including SDKDDKVer.h.

#include <SDKDDKVer.h>
```

## ServerLibrary\Util\Assert.cpp
```cpp
#include "stdafx.h"
#include "Assert.h"

void Assert(int condition, LPCWSTR conditionStr, LPCWSTR fileName, int lineNo)
{
    if (condition) {
        return;
    }
    shutdownServer();

    wstr_t	msg;
    msg = L" Assert: ";
    msg += conditionStr;
    msg += L", file : ";
    msg += fileName;
    msg += L", line : ";

    WCHAR buf[16];
    _itow_s(lineNo, buf, 10);
    msg += buf;
    SLog(L"! error %s", msg.c_str());
    MiniDump::getInstance().execptionFilter(NULL);
}
```

## ServerLibrary\Util\Assert.h
```h
#pragma once
#include "stdafx.h"

#undef ASSERT
#define ASSERT(x)	            Assert(x, _W(#x), _W(__FILE__), __LINE__)				   				

void Assert(int condition, LPCWSTR conditionStr, LPCWSTR fileName, int lineNo);
```

## ServerLibrary\Util\Clock.cpp
```cpp
#include "stdafx.h"
#include "Clock.h"

Clock::Clock()
{
    serverStartTick_ = this->systemTick();
}

Clock::~Clock()
{
}

tick_t Clock::strToTick(wstr_t str, WCHAR *fmt)
{
    int	year = 0;
    int	month = 0;
    int	day = 0;
    int	hour = 0;
    int	minute = 0;
    int	second = 0;

    swscanf_s(str.c_str(), fmt, &year, &month, &day, &hour, &minute, &second);

   
    tm time = { second, minute, hour, day, month - 1, year - 1900 };

    return mktime(&time);
}

tick_t Clock::serverStartTick()
{
    return serverStartTick_;
}

tick_t Clock::systemTick()
{
    return system_clock::to_time_t(system_clock::now());
}

wstr_t Clock::tickToStr(tick_t tick, WCHAR *fmt)
{
    array<WCHAR, SIZE_128> timeStr;

    tm time;
    localtime_s(&time, &tick);
    wcsftime(timeStr.data(), timeStr.size(), fmt, &time);

    return timeStr.data();
}

wstr_t Clock::nowTime(WCHAR *fmt)
{
    return this->tickToStr(this->systemTick(), fmt);
}

wstr_t Clock::nowTimeWithMilliSec(WCHAR *fmt)
{
#if 0
    timePoint now = system_clock::now();
    timePoint oldSecond = system_clock::from_time_t(this->systemTick());

    duration<double> milliSecond = now - oldSecond;
	array<WCHAR, SIZE_8> milliStr;
	snwprintf(milliStr, L"%03d", (int)(milliSecond.count() * 1000));
#else
	high_resolution_clock::time_point point = high_resolution_clock::now();
	milliseconds ms = duration_cast<milliseconds>(point.time_since_epoch());

	seconds s = duration_cast<seconds>(ms);
	tick_t t = s.count();
	std::size_t fractionalSeconds = ms.count() % 1000;
	array<WCHAR, SIZE_8> milliStr;
	snwprintf(milliStr, L"%03d", (int)(fractionalSeconds));
#endif
    wstr_t timeString = this->tickToStr(this->systemTick(), fmt);
    timeString += L".";
	timeString += milliStr.data();
    return timeString;
}

wstr_t Clock::today()
{
    return this->tickToStr(this->systemTick(), DATE_FORMAT);
}

wstr_t Clock::tomorrow()
{
    return this->tickToStr(this->systemTick() + DAY_TO_TICK(1), DATE_FORMAT);
}

wstr_t Clock::yesterday()
{
    return this->tickToStr(this->systemTick() - DAY_TO_TICK(1), DATE_FORMAT);
}

DayOfTheWeek Clock::todayOfTheWeek()
{
    tm time;
    tick_t tick = this->systemTick();
    localtime_s(&time, &tick);
    return (DayOfTheWeek)time.tm_wday;
}
```

## ServerLibrary\Util\Clock.h
```h
#pragma once
#include "stdafx.h"
#include <chrono>
#include <ctime>

#define CLOCK					Clock::getInstance()
#define NOW_TICK				CLOCK.systemTick
#define NOW_STRING				CLOCK.nowTime

#define TICK_MIN                (60)
#define TICK_HOUR               (TICK_MIN * 60)
#define TICK_DAY                (TICK_HOUR * 24)

#define TICK_TO_MIN(x)          (x / TICK_MIN)
#define MIN_TO_TICK(x)          (x * TICK_MIN)

#define TICK_TO_HOUR(x)         (x / TICK_HOUR)        
#define HOUR_TO_TICK(x)         (x * TICK_HOUR)

#define TICK_TO_DAY(x)          (x / TICK_DAY)
#define DAY_TO_TICK(x)          (x * TICK_DAY)

typedef enum {
    DAY_SUNDAY      = 0,
    DAY_MONDAY      = 1,        
    DAY_TUESDAY     = 2,        
    DAY_WEDNESDAY   = 3,        
    DAY_THURSDAY    = 4,
    DAY_FRIDAY      = 5,
    DAY_SATURDAY    = 6,
}DayOfTheWeek;

#define DATETIME_FORMAT         L"D%Y-%m-%dT%H:%M:%S"
#define DATE_FORMAT             L"%Y-%m-%d"
#define TIME_FORMAT             L"%H:%M:%S"
#define DB_TIME_FORMAT          L"%4d-%2d-%2d %2d:%2d:%2d"

using namespace std::chrono;
using namespace std;
typedef system_clock::time_point timePoint;

class Clock : public Singleton<Clock>
{
    tick_t	serverStartTick_;
    
    wstr_t	tickToStr(tick_t tick, WCHAR *fmt = DATETIME_FORMAT);

public:
    Clock();
    ~Clock();

    tick_t	serverStartTick();
    tick_t	systemTick();
    tick_t	strToTick(wstr_t str, WCHAR *fmt = DB_TIME_FORMAT);
    
    wstr_t	nowTime(WCHAR *fmt = DATETIME_FORMAT);
    wstr_t	nowTimeWithMilliSec(WCHAR *fmt = DATETIME_FORMAT);

    wstr_t today();
    wstr_t tomorrow();
    wstr_t yesterday();
    
    DayOfTheWeek todayOfTheWeek();
};
```

## ServerLibrary\Util\Config.cpp
```cpp
#include "stdafx.h"
#include "Config.h"

bool loadConfig(xml_t *config)
{
	if (!config->LoadFile("./config.xml")) {
		printf("! not exist config file.");
		return false;
	}
	return true;
}
```

## ServerLibrary\Util\Config.h
```h
#pragma once
#include "stdafx.h"

extern bool loadConfig(xml_t *config);
```

## ServerLibrary\Util\csv_parser\csv_parser.cpp
```cpp
#include "stdafx.h"
/* INCLUDING HEADER FILES */
//#include <csv_parser/csv_parser.hpp>


/* BEGIN DEFINITION FOR PUBLIC METHODS */
bool csv_parser::init(FILE * input_file_pointer)
{
	input_fp = input_file_pointer;

	if (input_fp == NULL)
	{
		fprintf(stderr, "Fatal error : unable to open input file from file pointer");

		return false;
	}

	/* Resetting the internal pointer to the beginning of the stream */
	rewind(input_fp);

	more_rows = true;

	_skip_lines();

	return true;
}

bool csv_parser::init(const char * input_file)
{
	const size_t filename_length = strlen(input_file);

	if (!filename_length)
	{
		fprintf(stderr, "Fatal error : invalid input file %s", input_file);

		return false;
	}

	input_filename = (char *) malloc(filename_length + 1);

	if (input_filename == NULL)
	{
		fprintf(stderr, "Fatal error : unable to allocate memory for file name buffer %s", input_file);

		return false;
	}

	memset(input_filename, 0, filename_length + 1);

    strcpy_s(input_filename, filename_length + 1, input_file);

    fopen_s(&input_fp, input_file, "r");

	if (input_fp == NULL)
	{
		fprintf(stderr, "Fatal error : unable to open input file %s", input_file);

		CSV_PARSER_FREE_BUFFER_PTR(input_filename);

		return false;
	}

	more_rows = true;

	_skip_lines();

	return true;
}

void csv_parser::set_enclosed_char(char fields_enclosed_by, enclosure_type_t enclosure_mode)
{
	if (fields_enclosed_by != 0)
	{
		enclosed_char   = fields_enclosed_by;
		enclosed_length = 1U;
		enclosure_type  = enclosure_mode;
	}
}

void csv_parser::set_field_term_char(char fields_terminated_by)
{
	if (fields_terminated_by != 0)
	{
		field_term_char   = fields_terminated_by;
		field_term_length = 1U;
	}
}

void csv_parser::set_line_term_char(char lines_terminated_by)
{
	if (lines_terminated_by != 0)
	{
		line_term_char   = lines_terminated_by;
		line_term_length = 1U;
	}
}

csv_row csv_parser::get_row(void)
{
	csv_row current_row;

	/* This will store the length of the buffer */
	unsigned int line_length = 0U;

	/* Character array buffer for the current record */
	char * line = NULL;

	/* Grab one record */
	_read_single_line(&line, &line_length);

	/* Select the most suitable field extractor based on the enclosure length */
	switch(enclosure_type)
	{
		case ENCLOSURE_NONE : 	 /* The fields are not enclosed by any character */
			_get_fields_without_enclosure(&current_row, line, &line_length);
		break;

		case ENCLOSURE_REQUIRED : /* The fields are enclosed by a character */
			_get_fields_with_enclosure(&current_row, line, &line_length);
		break;

		case ENCLOSURE_OPTIONAL : /* The fields may or may not be enclosed */
			_get_fields_with_optional_enclosure(&current_row, line, &line_length);
		break;

		default :
			_get_fields_with_optional_enclosure(&current_row, line, &line_length);
		break;
	}

	/* Deallocate the current buffer */
	CSV_PARSER_FREE_BUFFER_PTR(line);

	/* Keeps track of how many times this has method has been called */
	record_count++;

	return current_row;
}

/* BEGIN DEFINITION FOR PROTECTED METHODS */


/* BEGIN DEFINITION FOR PRIVATE METHODS */

void csv_parser::_skip_lines(void)
{
	/* Just in case the user accidentally sets ignore_num_lines to a negative number */
	unsigned int number_of_lines_to_ignore = abs((int) ignore_num_lines);

	while(has_more_rows() && number_of_lines_to_ignore)
	{
		const csv_row row = get_row();

		number_of_lines_to_ignore--;
	}

	record_count = 0U;
}

void csv_parser::_get_fields_without_enclosure(csv_row_ptr row, const char * line, const unsigned int * line_length)
{
	char * field = NULL;

	if (*line_length > 0)
	{
		field = (char *) malloc(*line_length);

		memset(field, 0, *line_length);

		register unsigned int field_start   = 0U;
		register unsigned int field_end     = 0U;
		register unsigned int char_pos 		= 0U;

		while(char_pos < *line_length)
		{
			char curr_char = line[char_pos];

			if (curr_char == field_term_char)
			{
				field_end = char_pos;

				const char * field_starts_at = line + field_start;

				/* Field width must exclude field delimiter characters */
				const unsigned int field_width = field_end - field_start;

				/* Copy exactly field_width bytes from field_starts_at to field */
				memcpy(field, field_starts_at, field_width);

				/* This must be a null-terminated character array */
				field[field_width] = 0x00;

				string field_string_obj = field;

				row->push_back(field_string_obj);

				/* This is the starting point of the next field */
				field_start = char_pos + 1;

			} else if (curr_char == line_term_char)
			{
				field_end = char_pos;

				const char * field_starts_at = line + field_start;

				/* Field width must exclude line terminating characters */
				const unsigned int field_width = field_end - field_start;

				/* Copy exactly field_width bytes from field_starts_at to field */
				memcpy(field, field_starts_at, field_width);

				/* This must be a null-terminated character array */
				field[field_width] = 0x00;

				string field_string_obj = field;

				row->push_back(field_string_obj);
			}

			/* Move to the next character in the current line */
			char_pos++;
		}

		/* Deallocate memory for field buffer */
		CSV_PARSER_FREE_BUFFER_PTR(field);
	}
}

void csv_parser::_get_fields_with_enclosure(csv_row_ptr row, const char * line, const unsigned int * line_length)
{
	char * field = NULL;

	if (*line_length > 0)
	{
		field = (char *) malloc(*line_length);

		memset(field, 0, *line_length);

		register unsigned int current_state = 0U;
		register unsigned int field_start   = 0U;
		register unsigned int field_end     = 0U;
		register unsigned int char_pos 		= 0U;

		while(char_pos < *line_length)
		{
			char curr_char = line[char_pos];

			if (curr_char == enclosed_char)
			{
				current_state++;

				/* Lets find out if the enclosure character encountered is
				 * a 'real' enclosure character or if it is an embedded character that
				 * has been escaped within the field.
				 */
				register char previous_char = 0x00;

				if (char_pos > 0U)
				{
					/* The escaped char will have to be the 2rd or later character. */
					previous_char = line[char_pos - 1];

					if (previous_char == escaped_char)
					{
						--current_state;
					}
				}

				if (current_state == 1U && previous_char != escaped_char)
				{
					/* This marks the beginning of the column */
					field_start = char_pos;

				} else if (current_state == 2U)
				{
					/* We have found the end of the current field */
					field_end = char_pos;

					/* We do not need the enclosure characters */
					const char * field_starts_at = line + field_start + 1U;

					/* Field width must exclude beginning and ending enclosure characters */
					const unsigned int field_width = field_end - field_start - 1U;

					/* Copy exactly field_width bytes from field_starts_at to field */
					memcpy(field, field_starts_at, field_width);

					/* This must be a null-terminated character array */
					field[field_width] = 0x00;

					string field_string_obj = field;

					row->push_back(field_string_obj);

					/* Reset the state to zero value for the next field */
					current_state = 0U;
				}
			}

			/* Move to the next character in the current line */
			char_pos++;
		}

		/* If no enclosures were found in this line, the entire line becomes the only field. */
		if (0 == row->size())
		{
			string entire_line = line;

			row->push_back(entire_line);

		} else if (current_state == 1U)
		{
			/* The beginning enclosure character was found but
			 * we could not locate the closing enclosure in the current line
			 * So we need to copy the remainder of the line into the last field.
			 */

			/* We do not need the starting enclosure character */
			const char * field_starts_at = line + field_start + 1U;

			/* Field width must exclude beginning characters */
			const unsigned int field_width = *line_length - field_start - 1U;

			/* Copy exactly field_width bytes from field_starts_at to field */
			memcpy(field, field_starts_at, field_width);

			/* This must be a null-terminated character array */
			field[field_width] = 0x00;

			string field_string_obj = field;

			row->push_back(field_string_obj);
		}

		/* Release the buffer for the field */
		CSV_PARSER_FREE_BUFFER_PTR(field);
	}
}

void csv_parser::_get_fields_with_optional_enclosure(csv_row_ptr row, const char * line, const unsigned int * line_length)
{
	char * field = NULL;

	/*
	 * How to extract the fields, when the enclosure char is optional.
	 *
	 * This is very similar to parsing the document without enclosure but with the following conditions.
	 *
	 * If the beginning char is an enclosure character, adjust the starting position of the string by + 1.
	 * If the ending char is an enclosure character, adjust the ending position by -1
	 */
	if (*line_length > 0)
	{
		field = (char *) malloc(*line_length);

		memset(field, 0, *line_length);

		register unsigned int field_start   = 0U;
		register unsigned int field_end     = 0U;
		register unsigned int char_pos 		= 0U;

		while(char_pos < *line_length)
		{
			char curr_char = line[char_pos];

			if (curr_char == field_term_char)
			{
				field_end = char_pos;

				const char * field_starts_at = line + field_start;

				/* Field width must exclude field delimiter characters */
				unsigned int field_width = field_end - field_start;

				const char line_first_char = field_starts_at[0];
				const char line_final_char = field_starts_at[field_width - 1];

				/* If the enclosure char is found at either ends of the string */
				unsigned int first_adjustment = (line_first_char == enclosed_char) ? 1U : 0U;
				unsigned int final_adjustment = (line_final_char == enclosed_char) ? 2U : 0U;

				/* We do not want to have any negative or zero field widths */
				field_width = (field_width > 2U) ? (field_width - final_adjustment) : field_width;

				/* Copy exactly field_width bytes from field_starts_at to field */
				memcpy(field, field_starts_at + first_adjustment, field_width);

				/* This must be a null-terminated character array */
				field[field_width] = 0x00;

				string field_string_obj = field;

				row->push_back(field_string_obj);

				/* This is the starting point of the next field */
				field_start = char_pos + 1;

			} else if (curr_char == line_term_char)
			{
				field_end = char_pos;

				const char * field_starts_at = line + field_start;

				/* Field width must exclude line terminating characters */
				unsigned int field_width = field_end - field_start;

				const char line_first_char = field_starts_at[0];
				const char line_final_char = field_starts_at[field_width - 1];

				/* If the enclosure char is found at either ends of the string */
				unsigned int first_adjustment = (line_first_char == enclosed_char) ? 1U : 0U;
				unsigned int final_adjustment = (line_final_char == enclosed_char) ? 2U : 0U;

				/* We do not want to have any negative or zero field widths */
				field_width = (field_width > 2U) ? (field_width - final_adjustment) : field_width;

				/* Copy exactly field_width bytes from field_starts_at to field */
				memcpy(field, field_starts_at + first_adjustment, field_width);

				/* This must be a null-terminated character array */
				field[field_width] = 0x00;

				string field_string_obj = field;

				row->push_back(field_string_obj);
			}

			/* Move to the next character in the current line */
			char_pos++;
		}

		/* Deallocate memory for field buffer */
		CSV_PARSER_FREE_BUFFER_PTR(field);
	}
}

void csv_parser::_read_single_line(char ** buffer, unsigned int * buffer_len)
{
	long int original_pos = ftell(input_fp);
	long int current_pos  = original_pos;

	register int current_char = 0;

	/* Checking one character at a time until the end of a line is found */
	while(true)
	{
		current_char = fgetc(input_fp);

		if (current_char == EOF)
		{
			/* We have reached the end of the file */
			more_rows = false;

			break;

		} else if (current_char == line_term_char)
		{
			/* We have reached the end of the row */
			current_pos++;

			break;

		} else {

			current_pos++;
		}
	}

	/* Let's try to peek one character ahead to see if we are at the end of the file */
	if (more_rows)
	{
		current_char = fgetc(input_fp);

		more_rows = (current_char == EOF) ? false : true;
	}

	/* Find out how long this row is */
	const size_t length_of_row = current_pos - original_pos;

	if (length_of_row > 0)
	{
        *buffer_len = (unsigned int)(length_of_row * sizeof(char)+1);

		*buffer = (char *) realloc(*buffer, *buffer_len);

		memset(*buffer, 0, *buffer_len);

		/* Reset the internal pointer to the original position */
		fseek(input_fp, original_pos, SEEK_SET);

		/* Copy the contents of the line into the buffer */
		fread(*buffer, 1, length_of_row, input_fp);
	}
}
```

## ServerLibrary\Util\csv_parser\csv_parser.hpp
```hpp
/**
 * csv_parser Header File
 *
 * This object is used to parse text documents that are delimited by some
 * type of character. Some of the common ones use spaces, tabs, commas and semi-colons.
 *
 * This is a list of common characters encountered by this program
 *
 * This list was prepared from the data from http://www.asciitable.com
 *
 * @li DEC is how it would be represented in decimal form (base 10)
 * @li HEX is how it would be represented in hexadecimal format (base 16)
 *
 * @li	DEC	HEX		Character Name
 * @li	0	0x00	null
 * @li	9	0x09	horizontal tab
 * @li	10	0x0A	line feed, new line
 * @li	13	0x0D	carriage return
 * @li	27	0x1B	escape
 * @li	32	0x20	space
 * @li	33	0x21	double quote
 * @li	39	0x27	single quote
 * @li	44	0x2C	comma
 * @li	92	0x5C	backslash
 *
 * @author Israel Ekpo <israel.ekpo@israelekpo.com>
 */

#ifndef CSV_PARSER_HPP_INCLUDED

#define CSV_PARSER_HPP_INCLUDED

#define LIBCSV_PARSER_MAJOR_VERSION 1

#define LIBCSV_PARSER_MINOR_VERSION 0

#define LIBCSV_PARSER_PATCH_VERSION 0

#define LIBCSV_PARSER_VERSION_NUMBER 10000

/* C++ header files */
#include <string>
#include <vector>

/* C header files */
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

/**
 * @typedef csv_row
 *
 * Data structure used to represent a record.
 *
 * This is an alias for vector <string>
 */
typedef vector <string> csv_row;

/**
 * @typedef csv_row_ptr
 *
 * Pointer to a csv_row object
 *
 * Expands to vector <string> *
 */
typedef csv_row * csv_row_ptr;

/**
 * @typedef enclosure_type_t
 *
 * This enum type is used to set the mode in which the CSV file is parsed.
 *
 * @li ENCLOSURE_NONE 		(1) means the CSV file does not use any enclosure characters for the fields
 * @li ENCLOSURE_REQUIRED 	(2) means the CSV file requires enclosure characters for all the fields
 * @li ENCLOSURE_OPTIONAL 	(3) means the use of enclosure characters for the fields is optional
 *
 * The ENCLOSURE_TYPE_BEGIN and ENCLOSURE_TYPE_END members of this enum definition are never to be used.
 */
typedef enum
{
	ENCLOSURE_TYPE_BEGIN = 0,
	ENCLOSURE_NONE       = 1,
	ENCLOSURE_REQUIRED   = 2,
	ENCLOSURE_OPTIONAL   = 3,
	ENCLOSURE_TYPE_END

} enclosure_type_t;

/**
 * @def CSV_PARSER_FREE_BUFFER_PTR(ptr)
 *
 * Used to deallocate buffer pointers
 *
 * It deallocates the pointer only if it is not null
 */
#define CSV_PARSER_FREE_BUFFER_PTR(ptr)	\
if (ptr != NULL)						\
{										\
	free(ptr);							\
										\
	ptr = NULL;							\
}

/**
 * @def CSV_PARSER_FREE_FILE_PTR(fptr)
 *
 * Used to close open file handles
 *
 * It closes the file only if it is not null
 */
#define CSV_PARSER_FREE_FILE_PTR(fptr)	\
if (fptr != NULL)						\
{										\
	fclose(fptr);						\
										\
	fptr = NULL;						\
}

/**
 * @class csv_parser
 *
 * The csv_parser object
 *
 * Used to parse text files to extract records and fields.
 *
 * We are making the following assumptions :
 *
 * @li The record terminator is only one character in length.
 * @li The field terminator is only one character in length.
 * @li The fields are enclosed by single characters, if any.
 *
 * @li The parser can handle documents where fields are always enclosed, not enclosed at all or optionally enclosed.
 * @li When fields are strictly all enclosed, there is an assumption that any enclosure characters within the field are escaped by placing a backslash in front of the enclosure character.
 *
 * The CSV files can be parsed in 3 modes.
 * @li (a) No enclosures
 * @li (b) Fields always enclosed.
 * @li (c) Fields optionally enclosed.
 *
 * For option (c) when the enclosure character is optional, if an enclosure character is spotted at either the beginning
 * or the end of the string, it is assumed that the field is enclosed.
 *
 * The csv_parser::init() method can accept a character array as the path to the CSV file.
 * Since it is overloaded, it can also accept a FILE pointer to a stream that is already open for reading.
 *
 * The set_enclosed_char() method accepts the field enclosure character as the first parameter and the enclosure mode as the second parameter which
 * controls how the text file is going to be parsed.
 *
 * @see csv_parser::set_enclosed_char()
 * @see enclosure_type_t
 *
 * @todo Add ability to parse files where fields/columns are terminated by strings instead of just one char.
 * @todo Add ability to set strings where lines start by. Currently lines do not have any starting char or string.
 * @todo Add ability to set strings where line end by. Currently lines can only end with a single char.
 * @todo Add ability to accept other escape characters besides the backslash character 0x5C.
 * @todo More support for improperly formatted CSV data files.
 *
 * @author Israel Ekpo <israel.ekpo@israelekpo.com>
 */
class csv_parser
{

public :

	/**
	 * Class constructor
	 *
	 * This is the default constructor.
	 *
	 * All the internal attributes are initialized here
	 *
	 * @li The enclosure character is initialized to NULL 0x00.
	 * @li The escape character is initialized to the backslash character 0x5C.
	 * @li The field delimiter character is initialized to a comma 0x2C.
	 * @li The record delimiter character is initialized to a new line character 0x0A.
	 *
	 * @li The lengths of all the above-mentioned fields are initialized to 0,1,1 and 1 respectively.
	 * @li The number of records to ignore is set to zero.
	 * @li The more_rows internal attribute is set to false.
	 * @li The pointer to the CSV input file is initialized to NULL
	 * @li The pointer to the buffer for the file name is also initialized to NULL
	 */
	csv_parser() : enclosed_char(0x00), 	escaped_char(0x5C),
				   field_term_char(0x2C),  	line_term_char(0x0A),
				   enclosed_length(0U),    	escaped_length(1U),
				   field_term_length(1U),  	line_term_length(1U),
				   ignore_num_lines(0U),   	record_count(0U),
				   input_fp(NULL),		   	input_filename(NULL),
				   enclosure_type(ENCLOSURE_NONE),
				   more_rows(false)
				   { }

	/**
	 * Class destructor
	 *
	 * In the class destructor the file pointer to the input CSV file is closed and
	 * the buffer to the input file name is also deallocated.
	 *
	 * @see csv_parser::input_fp
	 * @see csv_parser::input_filename
	 */
	~csv_parser()
	{
		CSV_PARSER_FREE_FILE_PTR(input_fp);

		CSV_PARSER_FREE_BUFFER_PTR(input_filename);
	}

	/**
	 * Initializes the current object
	 *
	 * This init method accepts a pointer to the CSV file that has been opened for reading
	 *
	 * It also resets the file pointer to the beginning of the stream
	 *
	 * @overload bool init(FILE * input_file_pointer)
	 * @param[in] input_file_pointer
	 * @return bool Returns true on success and false on error.
	 */
	bool init(FILE * input_file_pointer);

	/**
	 * Initializes the current object
	 *
	 * @li This init method accepts a character array as the path to the csv file.
	 * @li It sets the value of the csv_parser::input_filename property.
	 * @li Then it creates a pointer to the csv_parser::input_fp property.
	 *
	 * @overload bool init(const char * input_filename)
	 * @param[in] input_filename
	 * @return bool Returns true on success and false on error.
	 */
	bool init(const char * input_filename);

	/**
	 * Defines the Field Enclosure character used in the Text File
	 *
	 * Setting this to NULL means that the enclosure character is optional.
	 *
	 * If the enclosure is optional, there could be fields that are enclosed, and fields that are not enclosed within the same line/record.
	 *
	 * @param[in] fields_enclosed_by The character used to enclose the fields.
	 * @param[in] enclosure_mode How the CSV file should be parsed.
	 * @return void
	 */
	void set_enclosed_char(char fields_enclosed_by, enclosure_type_t enclosure_mode);

	/**
	 * Defines the Field Delimiter character used in the text file
	 *
	 * @param[in] fields_terminated_by
	 * @return void
	 */
	void set_field_term_char(char fields_terminated_by);

	/**
	 * Defines the Record Terminator character used in the text file
	 *
	 * @param[in] lines_terminated_by
	 * @return void
	 */
	void set_line_term_char(char lines_terminated_by);

	/**
	 * Returns whether there is still more data
	 *
	 * This method returns a boolean value indicating whether or not there are
	 * still more records to be extracted in the current file being parsed.
	 *
	 * Call this method to see if there are more rows to retrieve before invoking csv_parser::get_row()
	 *
	 * @see csv_parser::get_row()
	 * @see csv_parser::more_rows
	 *
	 * @return bool Returns true if there are still more rows and false if there is not.
	 */
	bool has_more_rows(void)
	{
		return more_rows;
	}

	/**
	 * Defines the number of records to discard
	 *
	 * The number of records specified will be discarded during the parsing process.
	 *
	 * @see csv_parser::_skip_lines()
	 * @see csv_parser::get_row()
	 * @see csv_parser::has_more_rows()
	 *
	 * @param[in] lines_to_skip How many records should be skipped
	 * @return void
	 */
	void set_skip_lines(unsigned int lines_to_skip)
	{
		ignore_num_lines = lines_to_skip;
	}

	/**
	 * Return the current row from the CSV file
	 *
	 * The row is returned as a vector of string objects.
	 *
	 * This method should be called only if csv_parser::has_more_rows() is true
	 *
	 * @see csv_parser::has_more_rows()
	 * @see csv_parser::get_record_count()
	 * @see csv_parser::reset_record_count()
	 * @see csv_parser::more_rows
	 *
	 * @return csv_row A vector type containing an array of strings
	 */
	csv_row get_row(void);

	/**
	 * Returns the number of times the csv_parser::get_row() method has been invoked
	 *
	 * @see csv_parser::reset_record_count()
	 * @return unsigned int The number of times the csv_parser::get_row() method has been invoked.
	 */
	unsigned int get_record_count(void)
	{
		return record_count;
	}

	/**
	 * Resets the record_count internal attribute to zero
	 *
	 * This may be used if the object is reused multiple times.
	 *
	 * @see csv_parser::record_count
	 * @see csv_parser::get_record_count()
	 * @return void
	 */
	void reset_record_count(void)
	{
		record_count = 0U;
	}

private :

	/**
	 * Ignores N records in the CSV file
	 *
	 * Where N is the value of the csv_parser::ignore_num_lines internal property.
	 *
	 * The number of lines skipped can be defined by csv_parser::set_skip_lines()
	 *
	 * @see csv_parser::set_skip_lines()
	 *
	 * @return void
	 */
	void _skip_lines(void);

	/**
	 * Reads a Single Line
	 *
	 * Reads a single record into the buffer passed by reference to the method
	 *
	 * @param[in,out] buffer A pointer to a character array for the current line.
	 * @param[out] buffer_len A pointer to an integer storing the length of the buffer.
	 * @return void
	 */
	void _read_single_line(char ** buffer, unsigned int * buffer_len);

	/**
	 * Extracts the fields without enclosures
	 *
	 * This is used when the enclosure character is not set
	 * @param[out] row The vector of strings
	 * @param[in] line The character array buffer containing the current record/line
	 * @param[in] line_length The length of the buffer
	 */
	void _get_fields_without_enclosure(csv_row_ptr row, const char * line, const unsigned int * line_length);

	/**
	 * Extracts the fields with enclosures
	 *
	 * This is used when the enclosure character is set.
	 *
	 * @param[out] row The vector of strings
	 * @param[in] line The character array buffer containing the current record/line
	 * @param[in] line_length The length of the buffer
	 */
	void _get_fields_with_enclosure(csv_row_ptr row, const char * line, const unsigned int * line_length);

	/**
	 * Extracts the fields when enclosure is optional
	 *
	 * This is used when the enclosure character is optional
	 *
	 * Hence, there could be fields that use it, and fields that don't.
	 *
	 * @param[out] row The vector of strings
	 * @param[in] line The character array buffer containing the current record/line
	 * @param[in] line_length The length of the buffer
	 */
	void _get_fields_with_optional_enclosure(csv_row_ptr row, const char * line, const unsigned int * line_length);

protected :

	/**
	 * The enclosure character
	 *
	 * If present or used for a field it is assumed that both ends of the fields are wrapped.
	 *
	 * This is that single character used in the document to wrap the fields.
	 *
	 * @see csv_parser::_get_fields_without_enclosure()
	 * @see csv_parser::_get_fields_with_enclosure()
	 * @see csv_parser::_get_fields_with_optional_enclosure()
	 *
	 * @var enclosed_char
	 */
	char enclosed_char;

	/**
	 * The escape character
	 *
	 * For now the only valid escape character allowed is the backslash character 0x5C
	 *
	 * This is only important when the enclosure character is required or optional.
	 *
	 * This is the backslash character used to escape enclosure characters found within the fields.
	 *
	 * @see csv_parser::_get_fields_with_enclosure()
	 * @see csv_parser::_get_fields_with_optional_enclosure()
	 * @todo Update the code to accept other escape characters besides the backslash
	 *
	 * @var escaped_char
	 */
	char escaped_char;

	/**
	 * The field terminator
	 *
	 * This is the single character used to mark the end of a column in the text file.
	 *
	 * Common characters used include the comma, tab, and semi-colons.
	 *
	 * This is the single character used to separate fields within a record.
	 *
	 * @var field_term_char
	 */
	char field_term_char;

	/**
	 * The record terminator
	 *
	 * This is the single character used to mark the end of a record in the text file.
	 *
	 * The most popular one is the new line character however it is possible to use others as well.
	 *
	 * This is the single character used to mark the end of a record
	 *
	 * @see csv_parser::get_row()
	 *
	 * @var line_term_char
	 */
	char line_term_char;

	/**
	 * Enclosure length
	 *
	 * This is the length of the enclosure character
	 *
	 * @see csv_parser::csv_parser()
	 * @see csv_parser::set_enclosed_char()
	 *
	 * @var enclosed_length
	 */
	unsigned int enclosed_length;

	/**
	 * The length of the escape character
	 *
	 * Right now this is really not being used.
	 *
	 * It may be used in future versions of the object.
	 *
	 * @todo Update the code to accept other escape characters besides the backslash
	 *
	 * @var escaped_length
	 */
	unsigned int escaped_length;

	/**
	 * Length of the field terminator
	 *
	 * For now this is not being used. It will be used in future versions of the object.
	 *
	 * @var field_term_length
	 */
	unsigned int field_term_length;

	/**
	 * Length of the record terminator
	 *
	 * For now this is not being used. It will be used in future versions of the object.
	 *
	 * @var line_term_length
	 */
	unsigned int line_term_length;

	/**
	 * Number of records to discard
	 *
	 * This variable controls how many records in the file are skipped before parsing begins.
	 *
	 * @see csv_parser::_skip_lines()
	 * @see csv_parser::set_skip_lines()
	 *
	 * @var ignore_num_lines
	 */
	unsigned int ignore_num_lines;

	/**
	 * Number of times the get_row() method has been called
	 *
	 * @see csv_parser::get_row()
	 * @var record_count
	 */
	unsigned int record_count;

	/**
	 * The CSV File Pointer
	 *
	 * This is the pointer to the CSV file
	 *
	 * @var input_fp
	 */
	FILE * input_fp;

	/**
	 * Buffer to input file name
	 *
	 * This buffer is used to store the name of the file that is being parsed
	 *
	 * @var input_filename
	 */
	char * input_filename;

	/**
	 * Mode in which the CSV file will be parsed
	 *
	 * The various values are explained below
	 *
	 * @li ENCLOSURE_NONE 		(1) means the CSV file does not use any enclosure characters for the fields
	 * @li ENCLOSURE_REQUIRED 	(2) means the CSV file requires enclosure characters for all the fields
	 * @li ENCLOSURE_OPTIONAL 	(3) means the use of enclosure characters for the fields is optional
	 *
	 * @see csv_parser::get_row()
	 * @see csv_parser::_read_single_line()
	 * @see csv_parser::_get_fields_without_enclosure()
	 * @see csv_parser::_get_fields_with_enclosure()
	 * @see csv_parser::_get_fields_with_optional_enclosure()
	 *
	 * @var enclosure_type
	 */
	enclosure_type_t enclosure_type;

	/**
	 * There are still more records to parse
	 *
	 * This boolean property is an internal indicator of whether there are still records in the
	 * file to be parsed.
	 *
	 * @see csv_parser::has_more_rows()
	 * @var more_rows
	 */
	bool more_rows;

}; /* class csv_parser */

#endif /* CSV_PARSER_HPP_INCLUDED */
```

## ServerLibrary\Util\GameObject.h
```h
#pragma once
#include "stdafx.h"

class Object
{
	wstr_t			allocFile_;
	int				allocLine_;
};

class NameObject
{
	wstr_t name_;
public:
	wstr_t& name() 
	{
		return name_;
	}

	void setName(wstr_t name)
	{
		name_ = name;
	}
};

class Work
{
public:
	virtual void tick() = 0;
	virtual void wakeup() {};
	virtual void suspend() {};
	virtual void stop() {};
	virtual void start() {};
};

class GameObject : public NameObject, public Work
{
	POINT		position_;
	float		direction_;

public:
	virtual ~GameObject() 
	{
		this->free();
	}
	virtual void initialize() {};
	virtual void free() {};
};
```

## ServerLibrary\Util\Lock.cpp
```cpp
#include "stdafx.h"
#include "Lock.h"
#include "Thread.h"

#ifdef _DEBUG
#define STERN_MODE
#endif

const int INVALID_LINE = -1;

Lock::Lock(WCHAR *name)
{
	lockId_ = LockManager::getInstance().generalId();
	name_ = name;

	lockingFile_.clear();
	lockingLine_ = INVALID_LINE;
}

Lock::~Lock()
{
	name_.clear();
}

const WCHAR* Lock::name() 
{
	return name_.c_str();
}

size_t Lock::lockId()
{
	return lockId_;
}

lock_t& Lock::mutex()
{
	return mutex_;
}

void Lock::lock(LPCWSTR fileName, int lineNo)
{
	mutex_.lock();

	lockingFile_ = fileName;
	lockingLine_ = lineNo;
}

void Lock::unlock()
{
	mutex_.unlock();

	lockingFile_.clear();
	lockingLine_ = INVALID_LINE;
}

void Lock::setThreadId(threadId_t id)
{
	threadId_ = id;
}

threadId_t Lock::threadId()
{
	return threadId_;
}
//-------------------------------------------------------//

LockSafeScope::LockSafeScope(Lock *lock, LPCWSTR fileName, int lineNo)
{
	if (lock == nullptr) {
		return;
	}
	if (_shutdown == true) {
		return;
	}

	lock_ = lock;
	Lock *deadLock = LockManager::getInstance().checkDeadLock(lock_);
	if (deadLock != nullptr) {
#ifdef STERN_MODE
		SErrLog(L"! [%s]lock and [%s]lock is dead detecting!", deadLock->name(), lock->name());
#else
		std::lock(lock_->mutex(), deadLock->mutex());
		SLog(L"!!! [%s]lock and [%s]lock is dead detecting!", deadLock->name(), lock->name());
#endif
		return;
	}

	lock_->lock(fileName, lineNo);
	lock->setThreadId(GET_CURRENT_THREAD_ID());
}

LockSafeScope::~LockSafeScope()
{
	if (!lock_) {
		return;
	}
	if (_shutdown == true) {
		return;
	}
	lock_->unlock();
	//lock_->setThreadId(nullptr);
}

//-------------------------------------------------------//
LockManager::LockManager()
{
	idSeed_ = 0;
}


Lock* LockManager::searchLockCycle(Lock *newLock)
{

	Thread *thread = ThreadManager::getInstance().at(GET_CURRENT_THREAD_ID());
	if (!thread) {
		return nullptr;
	}
	std::vector<Lock *> trace;		// 데드락 탐지시, 걸린 락 stact 추척
	trace.push_back(newLock);

	Lock *deadLock = nullptr;
	while (true) {
		Lock *threadLock = thread->lock();
		if (threadLock == nullptr) {
			break;
		}
		if (threadLock->lockId() == trace[0]->lockId()) {
			deadLock = threadLock;
			break;
		}
		trace.push_back(threadLock);
		thread = ThreadManager::getInstance().at(threadLock->threadId());
		if (!thread) {
			break;
		}
	}
	trace.empty();
	return deadLock;
}

Lock* LockManager::checkDeadLock(Lock *newLock)
{
	Lock *deadLock = this->searchLockCycle(newLock);
	if (deadLock) {
		return deadLock;
	}

	return nullptr;
}

size_t LockManager::generalId()
{
	size_t id = idSeed_++;
	return id;
}
```

## ServerLibrary\Util\Lock.h
```h
#pragma once
#include "stdafx.h"

class Lock
{
private:
	lock_t          mutex_;
	wstr_t			name_;
	size_t          lockId_;
	threadId_t		threadId_;

	wstr_t			lockingFile_;
	int				lockingLine_;

public:
	Lock(WCHAR* name);
	virtual ~Lock();

	const WCHAR* name();
	size_t lockId();

	lock_t& mutex();
	void lock(LPCWSTR fileName, int lineNo);
	void unlock();

	void setThreadId(threadId_t id);
	threadId_t threadId();
};

class LockSafeScope
{
	Lock          *lock_;
public:
	LockSafeScope(Lock *lock, LPCWSTR fileName, int lineNo);
	~LockSafeScope();
};

#define SAFE_LOCK(lock)     LockSafeScope __lockSafe(&lock, _W(__FILE__), __LINE__);

// 데드락 탐지를 위함
class LockManager : public Singleton < LockManager >
{
	size_t       idSeed_;

public:
	LockManager();

	Lock* searchLockCycle(Lock *newLock);
	Lock* checkDeadLock(Lock *lock);

	size_t generalId();
};
```

## ServerLibrary\Util\Logger.cpp
```cpp
#include "stdafx.h"
#include "Logger.h"

LogPrintf::LogPrintf()
{
    printf("* Log create : printf log mode\n");
}

void LogPrintf::log(WCHAR *logStr)
{
    printf("%ws", logStr);
}


LogFile::LogFile(xml_t *config)
{
	xmlNode_t *root = config->FirstChildElement("App")->FirstChildElement("Log");
	xmlNode_t *elem = root->FirstChildElement("Path");

	array<WCHAR, _MAX_PATH> logFilePath;
	StrConvA2W((char *)elem->GetText(), logFilePath.data(), logFilePath.max_size());
	printf("* Log create : [%ws]file log mode\n", logFilePath.data());
	this->initialize(logFilePath.data());
}

LogFile::~LogFile()
{
    fs_.close();
    fs_.clear();

    std::size_t found = fileName_.find(L".log");
    if (found == wstr_t::npos){
        return;
    }


    wstr_t closeFileName = fileName_.substr(0, found);
    closeFileName += CLOCK.nowTime(L"_%Y%m%d-%H%M%S.log");
    _wrename(fileName_.c_str(), closeFileName.c_str());
}

void LogFile::initialize(WCHAR *logFileName)
{
    fileName_ = logFileName;
    fs_.open(logFileName, std::ios::out | std::ios::trunc);
    if (fs_.bad()) {
        printf("! logfile error, file open fail.\n");
        assert(false);
    }
}

void LogFile::log(WCHAR *logStr)
{
    printf("%ws", logStr);

    fs_ << logStr;
    fs_.flush();
}


LogWriter::LogWriter()
{
    base_ = nullptr;
}

LogWriter::~LogWriter()
{
    prefix_.clear();

	SAFE_DELETE(base_);
};

void LogWriter::setLogger(LogBase *base, const WCHAR *logPrefix)
{
    prefix_.clear();     
    prefix_ = logPrefix;

    if (base_) {
        LogBase *old = base_;
        base_ = nullptr;
        old->unInitialize();
        
        SAFE_DELETE(old);
    }

    base_ = base;
    base_->initialize();
}

LogBase *LogWriter::logger()
{
    return base_;
}

void LogWriter::log(WCHAR *fmt, ...)
{
	va_list args;
	va_start(args, fmt);

	this->log(fmt, args);

	va_end(args);
}

void LogWriter::log(WCHAR *fmt, va_list args)
{
	wstr_t logMessage = CLOCK.nowTimeWithMilliSec();
	threadId_t threadId = GET_CURRENT_THREAD_ID();

	logMessage += L"\t";


	Thread *thread = ThreadManager::getInstance().at(threadId);
	if (thread) {
		logMessage += thread->name();
	}
	else {
		logMessage += prefix_;
	}

	array<WCHAR, SIZE_1024> logStr;

	vswprintf_s(logStr.data(), logStr.size(), fmt, args);

	logMessage += logStr.data();
	logMessage += L"\n";
    base_->log((WCHAR *)logMessage.c_str());
}

SystemLog::SystemLog()
{
	xml_t config;
	if (!loadConfig(&config)) {
		printf("!!! have not config file\n");
		exit(0);
		return;
	}
	this->initialize(&config);
}

SystemLog::~SystemLog()
{
}

void SystemLog::initialize(xml_t *config)
{
	xmlNode_t *root = config->FirstChildElement("App")->FirstChildElement("Log");
	if (!root) {
		printf("@ not exist log setting");
		LogBase *base = new LogPrintf();
		logWrite_.setLogger(base, L"testServer");
		return;
	}
	xmlNode_t *elem = root->FirstChildElement("Path");

	array<WCHAR, SIZE_256> tmp;
	elem = root->FirstChildElement("Prefix");
	StrConvA2W((char *)elem->GetText(), tmp.data(), tmp.max_size());
	wstr_t prefix = tmp.data();

	LogBase *base;
	elem = root->FirstChildElement("Type");
	const char *type = (char *)elem->GetText();
	if (!strcmp(type, "WithFile")) {
		base = new LogFile(config);
	}
	else {
		base = new LogPrintf();
	}

	logWrite_.setLogger(base, prefix.c_str());
}

void SystemLog::log(WCHAR *fmt, ...)
{
	va_list args;
	va_start(args, fmt);
    logWrite_.log(fmt, args);
	va_end(args);
}
```

## ServerLibrary\Util\Logger.h
```h
#pragma once
#include "stdafx.h"
#include <fstream>
#include "Singleton.h"
#include "Type.h"

#define SLog(arg, ...)				SystemLog::getInstance().log(arg, __VA_ARGS__);
#define SErrLog(arg, ...)			SystemLog::getInstance().log(arg, __VA_ARGS__); ::ExitProcess(0);


class LogBase
{
public:
    LogBase(){}
    virtual ~LogBase(){}
    virtual void initialize() {}
    virtual void unInitialize() {}
    virtual void log(WCHAR *logStr) = 0;
};

class LogPrintf : public LogBase
{
public:
    LogPrintf();
    void log(WCHAR *logStr);
};

class LogFile : public LogBase
{
    std::wfstream   fs_;
    wstr_t			fileName_;
public:
    LogFile(xml_t *config);
    virtual ~LogFile();

    void initialize(){}
    void initialize(WCHAR *logFileName);
    void log(WCHAR *logStr);
};
// 로그 쓰는 주체
class LogWriter
{
private:
    LogBase			*base_;
    wstr_t			prefix_;
public:
    LogWriter();
    virtual ~LogWriter();

    void setLogger(LogBase *base, const WCHAR *logPrefix);
    LogBase *logger();

    void log(WCHAR *fmt, ...);
	void log(WCHAR *fmt, va_list args);
};
typedef LogWriter* LogWriterPtr;

// 어플 시스템 로그
class SystemLog : public Singleton<SystemLog>
{
private:
    LogWriter   logWrite_;
public:
	SystemLog();
    virtual ~SystemLog();
	
	void initialize(xml_t *config);
	void log(WCHAR *fmt, ...);
};
```

## ServerLibrary\Util\Memory_LowFragmentationHeap.h
```h
#pragma once
#include "stdafx.h"

class LowFragmentationHeap
{
public:
	LowFragmentationHeap()
	{
		static bool init = false;
		if (init) {
			return;
		}
		init = true;

		ULONG HeapFragValue = 2;
		HANDLE hHeaps[100];
		DWORD dwHeapCount = GetProcessHeaps(100, hHeaps);

		for (DWORD i = 0; i < dwHeapCount; i++) {
			HeapSetInformation(hHeaps[i],
				HeapCompatibilityInformation,
				&HeapFragValue,
				sizeof(HeapFragValue));

		}
		printf("* Low-fragmentation Heap setting\n");
	}
};

static LowFragmentationHeap lfh;
```

## ServerLibrary\Util\MemoryLeak.h
```h
#pragma once
#include "stdafx.h"

#ifndef _DEBUG
#define USE_VISUAL_LEAK_DETECTOR
#endif

#ifdef USE_VISUAL_LEAK_DETECTOR
#include <vld.h>

#else 


#define _CRTDBG_MAP_ALLOC
#include "crtdbg.h"

#if 0 //실제 내부는 아래와 같이 선언되어 있다.
#ifdef  _CRTDBG_MAP_ALLOC

#define   malloc(s)
_malloc_dbg(s, _NORMAL_BLOCK, __FILE__, __LINE__)
#define   calloc(c, s)
_calloc_dbg(c, s, _NORMAL_BLOCK, __FILE__, __LINE__)
#define   realloc(p, s)
_realloc_dbg(p, s, _NORMAL_BLOCK, __FILE__, __LINE__)
#define   _expand(p, s)
_expand_dbg(p, s, _NORMAL_BLOCK, __FILE__, __LINE__)
#define   free(p)
_free_dbg(p, _NORMAL_BLOCK)
#define   _msize(p)         _msize_dbg(p, _NORMAL_BLOCK)

#endif  /* _CRTDBG_MAP_ALLOC */
#endif

class MemoryLeckDetct
{
public:
    MemoryLeckDetct()
    {
        _CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF);
        // Send all reports to STDOUT
        _CrtSetReportMode(_CRT_WARN, _CRTDBG_MODE_FILE);
        _CrtSetReportFile(_CRT_WARN, _CRTDBG_FILE_STDOUT);
        _CrtSetReportMode(_CRT_ERROR, _CRTDBG_MODE_FILE);
        _CrtSetReportFile(_CRT_ERROR, _CRTDBG_FILE_STDOUT);
        _CrtSetReportMode(_CRT_ASSERT, _CRTDBG_MODE_FILE);
        _CrtSetReportFile(_CRT_ASSERT, _CRTDBG_FILE_STDOUT);


    }

    ~MemoryLeckDetct()
    {
        //서버 종료시 메모리 체크해줍니다.
        _ASSERTE(_CrtCheckMemory());
    }
};

//static MemoryLeckDetct leck;
#endif //USE_VISUAL_LEAK_DETECTOR
```

## ServerLibrary\Util\Minidump.cpp
```cpp
#include "stdafx.h"
#include "MiniDump.h"

MiniDump::MiniDump()
{
	::SetUnhandledExceptionFilter(execptionFilter);
	printf("* Dump filter setting complte!\n");
}

LONG WINAPI MiniDump::execptionFilter(struct _EXCEPTION_POINTERS *exceptionInfo)
{
    shutdownServer();

    _CrtMemDumpAllObjectsSince(NULL);

    HMODULE dumpDll = nullptr;
    dumpDll = ::LoadLibraryA("DBGHELP.DLL");
    if (!dumpDll) {
		printf("! DBGHelp.dll not loaded\n");
		return 0;
    }

    wstr_t dumpPatch;
    dumpPatch += NOW_STRING(L"D%Y-%m-%dT%H-%M-%S");
    dumpPatch += L".dmp";

    HANDLE file = ::CreateFile(dumpPatch.c_str(), GENERIC_WRITE, FILE_SHARE_WRITE, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    if (file == INVALID_HANDLE_VALUE) {
		printf("! dump file not making\n");
        return 0;
    }

    _MINIDUMP_EXCEPTION_INFORMATION info;
	info.ThreadId = ::GetCurrentThreadId();
    info.ExceptionPointers = exceptionInfo;
    info.ClientPointers = NULL;

    WRITEDUMP dumpFunc = (WRITEDUMP)::GetProcAddress(dumpDll, "MiniDumpWriteDump");
    if (dumpFunc(GetCurrentProcess(), GetCurrentProcessId(), file, MiniDumpNormal, &info, NULL, NULL) == FALSE) {
		printf("! dump file saving error\n");
        return 0;
    }
    ::CloseHandle(file);

    return EXCEPTION_CONTINUE_SEARCH;
}

static MiniDump minidump;
```

## ServerLibrary\Util\Minidump.h
```h
#pragma once
#include "stdafx.h"
#include "dbghelp.h"

//dump 함수 포인터
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
```

## ServerLibrary\Util\Monitoring.h
```h
#pragma once
#include "stdafx.h"
#include "psapi.h"

class Monitoring : public Singleton<Monitoring>
{
	ULARGE_INTEGER lastCPU, lastSysCPU, lastUserCPU;
	int numProcessors;
	HANDLE self;

public:
	Monitoring() 
	{
		SYSTEM_INFO sysInfo;
		FILETIME ftime, fsys, fuser;

		GetSystemInfo(&sysInfo);
		numProcessors = sysInfo.dwNumberOfProcessors;

		GetSystemTimeAsFileTime(&ftime);
		memcpy(&lastCPU, &ftime, sizeof(FILETIME));

		self = GetCurrentProcess();
		GetProcessTimes(self, &ftime, &ftime, &fsys, &fuser);
		memcpy(&lastSysCPU, &fsys, sizeof(FILETIME));
		memcpy(&lastUserCPU, &fuser, sizeof(FILETIME));
	}

	double processCpuUsage() 
	{
		FILETIME ftime, fsys, fuser;
		ULARGE_INTEGER now, sys, user;
		double percent;

		GetSystemTimeAsFileTime(&ftime);
		memcpy(&now, &ftime, sizeof(FILETIME));

		GetProcessTimes(self, &ftime, &ftime, &fsys, &fuser);
		memcpy(&sys, &fsys, sizeof(FILETIME));
		memcpy(&user, &fuser, sizeof(FILETIME));
		percent = (double)((sys.QuadPart - lastSysCPU.QuadPart) + (user.QuadPart - lastUserCPU.QuadPart));
		percent /= (now.QuadPart - lastCPU.QuadPart);
		percent /= numProcessors;
		percent = percent * 100;
		return fixInRange(0, percent, 100);
	}

	SIZE_T processMemUsage()
	{
		PROCESS_MEMORY_COUNTERS pmc;
		GetProcessMemoryInfo(GetCurrentProcess(), &pmc, sizeof(pmc));
		return (size_t) pmc.WorkingSetSize;
	}

	SIZE_T physyicMemUsage()
	{
		MEMORYSTATUSEX memInfo;
		memInfo.dwLength = sizeof(MEMORYSTATUSEX);
		GlobalMemoryStatusEx(&memInfo);

		return (size_t) memInfo.ullTotalPhys - memInfo.ullAvailPhys;
	}
};
```

## ServerLibrary\Util\ProgramValidation.h
```h
#pragma once

// 만약 바이너리가 유출 되었을때를 대비한 안전장치 (서버 검증 장치)
#include "stdafx.h"
#include <locale>
#include <iostream>
#include <sstream>
#include <time.h>

class ProgramValidation
{
//	void checkSMTP()
//	{
//		SOCKET smtpSocket;
//		if (!connectSMTP(&smtpSocket)) {
//			SLog(L"! The smtp server is not loaded.");
//#ifndef _DEBUG
//			exit(1);
//#endif //_DEBUG
//		}
//	}

	class ProgramExpire
	{
		tick_t serverBirthTick_;

		void checkExpire()
		{
			tick_t expireTick = serverBirthTick_ + DAY_TO_TICK(30);
			tick_t now = CLOCK.systemTick();
			if (!isInRange(serverBirthTick_, now, expireTick)) {
				//sendMail("serverAlert@server.com",
				//	"serverProgramer@server.com",
				//	"[EXPIRE] 서버 유효성 체크 실패",
				//	"IP주소, port 번호등...");
#ifndef _DEBUG
				exit(1);
#endif //_DEBUG
			}
		}

		void setBirthTick()
		{
			//문자열 시간을 tick_t화 하기
			locale loc;
			basic_stringstream<char> birthDate;
			ios_base::iostate st = 0;
			struct tm t;
			memset(&t, 0, sizeof(struct tm));

			birthDate << __DATE__;		
			birthDate.imbue(loc);
			basic_istream<char>::_Iter i = use_facet
				<time_get <char> >
				(loc).get_date(basic_istream<char>::_Iter(birthDate.rdbuf()),
				basic_istream<char>::_Iter(0), birthDate, st, &t);

			if (st & ios_base::failbit) {
				cout << "time_get::get_time(" << birthDate.rdbuf()->str() << ") FAILED on char: " << *i << endl;
				ASSERT(FALSE);
			}
			array<WCHAR, SIZE_64> dataTime;
			snwprintf(dataTime, L"%4d-%2d-%2d %d:%d:%d", t.tm_year + 1900, t.tm_mon + 1, t.tm_mday, 0, 0, 0);
			serverBirthTick_ = CLOCK.strToTick(dataTime.data());
		}

	public:
		ProgramExpire()
		{
			this->setBirthTick();
			this->checkExpire();
		}
	};
	

public:
	ProgramValidation()
	{
		ProgramExpire checkExpire;

	}
};

static ProgramValidation programValidation;
```

## ServerLibrary\Util\Singleton.h
```h
#pragma once
#include "stdafx.h"

template <class T>
class Singleton
{
protected:
    Singleton() {}
    ~Singleton() {}

public:
    Singleton(const Singleton&);
    Singleton& operator = (const Singleton &);

    static T& getInstance()
    {
        static T instance;
        return instance;
    }
};
```

## ServerLibrary\Util\Table.h
```h
#pragma once
#include "stdafx.h"
#include <unordered_map>
#include <map>
#include <unordered_set>
#include <set>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <array>
#include <algorithm>
#include <functional>

typedef std::function<void(void *)> EachFunction;
typedef std::function<void(void *, void *)> PairFunction;

#if 0
template <typename KEY, typename VALUE>
class hash_map
{
    typedef std::hash_map<KEY, VALUE>			MAP;

    typedef typename MAP::iterator              ITER;
    typedef typename MAP::const_iterator        CITER;

    MAP     map_;
public:
    MAP&    map()           { return map_; }

    void    clear()         { map_.clear(); }
    size_t  size()          { return map_.size(); }
    bool    empty()         { return map_.empty(); }
    ITER    begin()         { return map_.begin(); }
    ITER    end()           { return map_.end(); }

    VALUE   front()
    {
        if (this->empty()) {
            return (VALUE) nullptr;
        }
        return this->begin()->second();
    }

    VALUE   back()
    {
        if (this->empty()) {
            return (VALUE) nullptr;
        }
        auto iter = this->end();
        --iter;
        return iter->second;
    }

    void    push(KEY key, VALUE value)
    {
		std::pair<KEY, VALUE> node(key, value);
		map_.insert(node);
    }

    VALUE    pop(KEY key)
    {
        auto iter = map_.find(key);
        if (iter == map_.end()) {
            return (VALUE) nullptr;
        }
        VALUE value = iter->second;
        map_.erase(iter);
        return value;
    }

    VALUE   get(KEY key)
    {
		if (this->empty()) {
			return (VALUE) nullptr;
		}
        auto iter = map_.find(key);
        return (iter == this->end()) ? (VALUE) nullptr : iter->second;
    }

    VALUE   next(KEY key, KEY &key2)
    {
        if (this->empty()) {
            return (VALUE) nullptr;
        }
        auto iter = map_.upper_bound(key);
        if (iter == this->end()) {
            return (VALUE) nullptr;
        }
        key2 = iter->first;
        return iter->second;
    }

    void    clearObjects(EachFunction func)
    {
		for (auto iter : map_) {
            if (func) {
                func(iter.second);
                continue;
            }
			SAFE_DELETE(iter.second);
        }
        this->clear();
    }

	void	clearObjects()
	{
		for (auto iter : map_) {
			SAFE_DELETE(iter.second);
        }
        this->clear();
	}

	void    doEach(EachFunction func)
	{
        if (!func) {
            return;
        }
		for (auto iter : map_) {
			func(iter.second);
		}
    }

    void    doPair(PairFunction func)
    {
        if (!func) {
            return;
        }
		for (auto iter : map_) {
			func(iter.second);
        }
    }
};

//-----------------------------------------------------------------//
//리스트 재 정의
//-----------------------------------------------------------------//
template <typename VALUE>
class List
{
public:
    typedef std::list<VALUE>					    LIST;
    typedef typename std::list<VALUE>::iterator	    ITER;
    typedef typename std::list<VALUE>::reverse_iterator 	RITER;

private:
    LIST    	list_;
    DWORD		currentPos_;
    VALUE			*instance_;

public:
    List() {
        currentPos_ = 0;
        instance_ = nullptr;
    }

    //기본 조작
    inline ITER		begin()	    			{ return list_.begin(); }
    inline ITER		end()					{ return list_.end(); }
    inline RITER	rbegin()				{ return list_.rbegin(); }
    inline RITER	rend()					{ return list_.rend(); }

    inline bool		next(ITER &pos, VALUE*& ptr)
    {
        ptr = nullptr;
        if (this->end() == pos)	{
            return false;
        }

        ptr = &(*pos);
        ++pos;
        return true;
    }

    inline ITER		erase(ITER &pos)	
    {
        if (this->end() == pos)	{
            return pos;
        }
        return list_.erase(pos);
    }
    inline void		remove(VALUE data)			{ list_.remove(data); }

    inline void		pushFront(VALUE &data)		{ list_.push_front(data); }
    inline void		pushBack(VALUE &data)		{ list_.push_back(data); }
    inline void		pushBackCopy(VALUE t)		{ PushBack(t); }

    inline VALUE&		front()					{ return list_.front(); }
    inline VALUE&		back()					{ return list_.back(); }

    inline void		popFront()				{ list_.pop_front(); }
    inline void		popBack()				{ list_.pop_back(); }
    inline bool		pop(VALUE &data)
    {
        ITER iter = this->find(data);
        if (iter != this->end()) {
            this->erase(iter);
            return true;
        }
        return false;
    }
    inline bool		rpop(VALUE &data)
    {
		RITER iter = this->rbegin();
		for (; iter != this->rend(); ++iter) {
			if (*iter = data) {
				this->erase((++iter).base());
                return true;
            }
        }
        
        return false;
    }

    inline void		clean(EachFunction func)
    {
        auto iter = this->begin();
        for (; iter != this->end(); ++iter) {
            if (func) {
                func(*iter);
            } else {
                SAFE_DELETE(*iter);
            }
        }
        this->clear();
    }
    inline void		clear()					{ list_.clear(); }

    inline size_t	size()	const			{ return list_.size(); }
    inline bool		empty()	const			{ return (bool)list_.empty(); }

    void	doEach(EachFunction func)
    {
        if (!func) {
            return;
        }
		for (auto iter : list_) {
			func(iter);
        }
    }
    void    doPair(PairFunction func)
    {
        if (!func) {
            return;
        }
		for (auto iter : list_) {
			func(iter);
        }
    }

    //-----------------------------------------------------------------//
    // 알고리즘
    VALUE	find(VALUE &aVal)
	{
		auto iter = std::find(this->begin(), this->end(), aVal); 
		if (iter == this->end()) {
			return (VALUE) nullptr;
		}
		return (VALUE)*iter;
	}
    LIST	&listData()					    { return list_; }
};
#endif
```

## ServerLibrary\Util\Task.cpp
```cpp
#include "stdafx.h"
#include "Task.h"

TaskNode::TaskNode(Work *workObject, int freqSec, int durationSec)
{
	workObject_ = workObject;
	freqSec_ = freqSec;
	durationSec_ = durationSec;
	this->nextTick();
}

TaskNode::~TaskNode()
{
	SAFE_DELETE(workObject_);
}

void TaskNode::nextTick()
{
	nextTick_ = NOW_TICK() + (tick_t)freqSec_;
}

bool TaskNode::expired()
{
	if (workObject_ == nullptr) {
		return true;
	}
	if (durationSec_ != TICK_INFINTY) {
		if (durationSec_ < NOW_TICK()) {
			return true;
		}
	}
	return false;
}

void TaskNode::tick()
{
	if (nextTick_ < NOW_TICK()) {
		workObject_->tick();
		this->nextTick();
	}
}

Task::Task(int id) 
{
	id_ = id;
}

Task::~Task()
{
	for (auto node : taskList_) {
		SAFE_DELETE(node);
	}
}

void Task::add(TaskNode *taskNode)
{
	taskList_.push_back(taskNode);
}

void Task::remove(TaskNode *taskNode)
{
	taskList_.remove(taskNode);
}

void Task::process()
{
	while (!_shutdown) {
		std::vector<TaskNode *> deleteNodes;
		for (auto taskNode : taskList_) {
			if (taskNode->expired()) {
				deleteNodes.push_back(taskNode);
				continue;
			}
			taskNode->tick();
		}

		for (auto node : deleteNodes) {
			this->remove(node);
		}
		CONTEXT_SWITCH;
	}
}

void Task::run()
{
	thread_ = MAKE_THREAD(Task, process);
}

TaskManager::TaskManager()
{
	xml_t config;
	if (!loadConfig(&config)) {
		return;
	}
	this->initialize(&config);
}

void TaskManager::initialize(xml_t *config)
{
	xmlNode_t *root = config->FirstChildElement("App")->FirstChildElement("Task");
	if (!root) {
		SLog(L"@ not exist task setting");
		return;
	}
	xmlNode_t *elem = root->FirstChildElement("ThreadCount");
	sscanf_s(elem->GetText(), "%d", &threadCount_);

	for (int i = 0; i < threadCount_; ++i) {
		Task *task = new Task(i);
		taskPool_.push_back(task);
		task->run();
	}
	SLog(L"* task thread, [%d] maked", threadCount_);
}

TaskManager::~TaskManager()
{
	for (auto task : taskPool_) {
		SAFE_DELETE(task);
	}
}

void TaskManager::add(Work *workObject, int freqSec, int durationSec)
{
	const int MINIMAL_THREAD_COUNT = 1;
	if (threadCount_ < MINIMAL_THREAD_COUNT) {
		return;
	}
	static int nodeCount = 0;
	
	TaskNode *node = new TaskNode(workObject, freqSec, durationSec);
	int index = nodeCount % threadCount_;
	Task *task = taskPool_[index];
	task->add(node);

	++nodeCount;
}
```

## ServerLibrary\Util\Task.h
```h
#pragma once
#include "stdafx.h"

#define TICK_INFINTY		0

class Work;
class TaskNode
{
	Work		*workObject_;
	int			freqSec_;
	int			durationSec_;

	tick_t		nextTick_;
public:
	TaskNode(Work *workObject, int freqSec, int durationSec);
	~TaskNode();

	void nextTick();
	bool expired();

	void tick();
};

class Task
{
	std::list<TaskNode *> taskList_;
	Thread		*thread_;
	int			id_;

public:
	Task(int id);
	~Task();
	void add(TaskNode *taskNode);
	void remove(TaskNode *taskNode);

	void process();
	void run();
};

class TaskManager : public Singleton <TaskManager>
{
	int                     threadCount_;
	std::vector<Task *>     taskPool_;

public:
	TaskManager();
	virtual ~TaskManager();

	void initialize(xml_t *config);

	void add(Work *workObject, int freqSec, int durationSec);
};
```

## ServerLibrary\Util\Thread.cpp
```cpp
#include "stdafx.h"
#include "Thread.h"
#include "Lock.h"

Thread::Thread(thread_t *thread, wstr_t name)
{
	name_ = name;
	thread_ = thread;
	id_ = thread_->get_id();

	ThreadManager::getInstance().put(this);
}

Thread::~Thread()
{
	thread_->join();
	SAFE_DELETE(thread_);
	SAFE_DELETE(lock_);
}

threadId_t Thread::id()
{
	return id_;
}

wstr_t &Thread::name()
{
	return name_;
}

void Thread::setLock(Lock *lock)
{
	lock_ = lock;
}

Lock* Thread::lock()
{
	return lock_;
}

ThreadManager::~ThreadManager()
{
	for (auto thread : threadPool_){
		SAFE_DELETE(thread.second);
	}
}

void ThreadManager::put(Thread *thread)
{
	std::pair<threadId_t, Thread *> node(thread->id(), thread);
	threadPool_.insert(node);
	SLog(L"* create thread : id[0x%X] name[%s], pool size[%d]", thread->id(), thread->name().c_str(), threadPool_.size());
}

void ThreadManager::remove(threadId_t id)
{
	auto iter = threadPool_.find(id);
	if (iter == threadPool_.end()) {
		return;
	}
	auto thread = iter->second;
	threadPool_.erase(iter);
}

Thread* ThreadManager::at(threadId_t id)
{
	if (threadPool_.empty()) {
		return nullptr;
	}
	auto iter = threadPool_.find(id);
	if (iter == threadPool_.end()) {
		return nullptr;
	}
	auto thread = iter->second;
	return thread;
}
```

## ServerLibrary\Util\Thread.h
```h
#pragma once
#include "stdafx.h"

#define MAKE_THREAD(className, process)	(new Thread(new thread_t(&className##::##process, this), L#className))
#define GET_CURRENT_THREAD_ID		std::this_thread::get_id
class Lock;
typedef std::function<void(void *)> ThreadFunction;

class Thread
{
	threadId_t				id_;
	wstr_t					name_;
	thread_t				*thread_;
	Lock					*lock_;			//지금 걸린 락
	
public:
	Thread(thread_t *thread, wstr_t name);
	~Thread();	

	threadId_t id();
	wstr_t &name();

	void setLock(Lock *lock);
	Lock *lock();
};

//#define THREAD_POOL_HASHMAP
class ThreadManager : public Singleton < ThreadManager >
{
#ifdef THREAD_POOL_HASHMAP
	hash_map <threadId_t, Thread*> threadPool_;
#else //THREAD_POOL_HASHMAP
	map <threadId_t, Thread *> threadPool_;
#endif //THREAD_POOL_HASHMAP

public:
	~ThreadManager();

	void put(Thread *thread);
	void remove(threadId_t id);
	Thread *at(threadId_t id);
};
```

## ServerLibrary\Util\ThreadJobQueue.h
```h
#pragma once
#include "stdafx.h"
#include <queue>
#include <stdexcept>   

template <typename T>
class ThreadJobQueue
{
private:
    enum {
        WRITE_QUEUE,
        READ_QUEUE,
        MAX_QUEUE,
    };
    std::queue<T>		queue_[MAX_QUEUE];

    std::queue<T>		*writeQueue_;	
    std::queue<T>		*readQueue_;	

    Lock		        lock_;

public:
    ThreadJobQueue(WCHAR* name)
        : lock_(name)
    {
        writeQueue_ = &queue_[WRITE_QUEUE];
        readQueue_ = &queue_[READ_QUEUE];
    }

	~ThreadJobQueue()
	{
		readQueue_->empty();
		writeQueue_->empty();
	}

    inline void push(const T &t)
    {
        SAFE_LOCK(lock_);
        writeQueue_->push(t);
    }

	inline bool pop(T &t)
	{
		SAFE_LOCK(lock_);
		size_t size = this->size();
		if (size == 0) {
			return false;
		}
		if (readQueue_->empty()) {
			this->swap();
		}
		t = readQueue_->front();
		readQueue_->pop();
		return true;
	}

    inline void swap()
    {
        SAFE_LOCK(lock_);
        if (writeQueue_ == &queue_[WRITE_QUEUE]) {
            writeQueue_ = &queue_[READ_QUEUE];
            readQueue_ = &queue_[WRITE_QUEUE];
        } else {
            writeQueue_ = &queue_[WRITE_QUEUE];
            readQueue_ = &queue_[READ_QUEUE];
        }
    }

    inline bool isEmpty()   { return readQueue_->empty(); }
    inline size_t size()
    {
        SAFE_LOCK(lock_);
		size_t size = (size_t)(queue_[WRITE_QUEUE].size() + queue_[READ_QUEUE].size()); 
		return size;
    }
};
```

## ServerLibrary\Util\tinyXml\tinystr.cpp
```cpp
/*
www.sourceforge.net/projects/tinyxml

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any
damages arising from the use of this software.

Permission is granted to anyone to use this software for any
purpose, including commercial applications, and to alter it and
redistribute it freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must
not claim that you wrote the original software. If you use this
software in a product, an acknowledgment in the product documentation
would be appreciated but is not required.

2. Altered source versions must be plainly marked as such, and
must not be misrepresented as being the original software.

3. This notice may not be removed or altered from any source
distribution.
*/
#include "stdafx.h"

#ifndef TIXML_USE_STL

#include "tinystr.h"

// Error value for find primitive
const TiXmlString::size_type TiXmlString::npos = static_cast< TiXmlString::size_type >(-1);


// Null rep.
TiXmlString::Rep TiXmlString::nullrep_ = { 0, 0, { '\0' } };


void TiXmlString::reserve (size_type cap)
{
	if (cap > capacity())
	{
		TiXmlString tmp;
		tmp.init(length(), cap);
		memcpy(tmp.start(), data(), length());
		swap(tmp);
	}
}


TiXmlString& TiXmlString::assign(const char* str, size_type len)
{
	size_type cap = capacity();
	if (len > cap || cap > 3*(len + 8))
	{
		TiXmlString tmp;
		tmp.init(len);
		memcpy(tmp.start(), str, len);
		swap(tmp);
	}
	else
	{
		memmove(start(), str, len);
		set_size(len);
	}
	return *this;
}


TiXmlString& TiXmlString::append(const char* str, size_type len)
{
	size_type newsize = length() + len;
	if (newsize > capacity())
	{
		reserve (newsize + capacity());
	}
	memmove(finish(), str, len);
	set_size(newsize);
	return *this;
}


TiXmlString operator + (const TiXmlString & a, const TiXmlString & b)
{
	TiXmlString tmp;
	tmp.reserve(a.length() + b.length());
	tmp += a;
	tmp += b;
	return tmp;
}

TiXmlString operator + (const TiXmlString & a, const char* b)
{
	TiXmlString tmp;
	TiXmlString::size_type b_len = static_cast<TiXmlString::size_type>( strlen(b) );
	tmp.reserve(a.length() + b_len);
	tmp += a;
	tmp.append(b, b_len);
	return tmp;
}

TiXmlString operator + (const char* a, const TiXmlString & b)
{
	TiXmlString tmp;
	TiXmlString::size_type a_len = static_cast<TiXmlString::size_type>( strlen(a) );
	tmp.reserve(a_len + b.length());
	tmp.append(a, a_len);
	tmp += b;
	return tmp;
}


#endif	// TIXML_USE_STL
```

## ServerLibrary\Util\tinyXml\tinystr.h
```h
/*
www.sourceforge.net/projects/tinyxml

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any
damages arising from the use of this software.

Permission is granted to anyone to use this software for any
purpose, including commercial applications, and to alter it and
redistribute it freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must
not claim that you wrote the original software. If you use this
software in a product, an acknowledgment in the product documentation
would be appreciated but is not required.

2. Altered source versions must be plainly marked as such, and
must not be misrepresented as being the original software.

3. This notice may not be removed or altered from any source
distribution.
*/

#include "stdafx.h"
#ifndef TIXML_USE_STL

#ifndef TIXML_STRING_INCLUDED
#define TIXML_STRING_INCLUDED

#include <assert.h>
#include <string.h>

/*	The support for explicit isn't that universal, and it isn't really
	required - it is used to check that the TiXmlString class isn't incorrectly
	used. Be nice to old compilers and macro it here:
*/
#if defined(_MSC_VER) && (_MSC_VER >= 1200 )
	// Microsoft visual studio, version 6 and higher.
	#define TIXML_EXPLICIT explicit
#elif defined(__GNUC__) && (__GNUC__ >= 3 )
	// GCC version 3 and higher.s
	#define TIXML_EXPLICIT explicit
#else
	#define TIXML_EXPLICIT
#endif


/*
   TiXmlString is an emulation of a subset of the std::string template.
   Its purpose is to allow compiling TinyXML on compilers with no or poor STL support.
   Only the member functions relevant to the TinyXML project have been implemented.
   The buffer allocation is made by a simplistic power of 2 like mechanism : if we increase
   a string and there's no more room, we allocate a buffer twice as big as we need.
*/
class TiXmlString
{
  public :
	// The size type used
  	typedef size_t size_type;

	// Error value for find primitive
	static const size_type npos; // = -1;


	// TiXmlString empty constructor
	TiXmlString () : rep_(&nullrep_)
	{
	}

	// TiXmlString copy constructor
	TiXmlString ( const TiXmlString & copy) : rep_(0)
	{
		init(copy.length());
		memcpy(start(), copy.data(), length());
	}

	// TiXmlString constructor, based on a string
	TIXML_EXPLICIT TiXmlString ( const char * copy) : rep_(0)
	{
		init( static_cast<size_type>( strlen(copy) ));
		memcpy(start(), copy, length());
	}

	// TiXmlString constructor, based on a string
	TIXML_EXPLICIT TiXmlString ( const char * str, size_type len) : rep_(0)
	{
		init(len);
		memcpy(start(), str, len);
	}

	// TiXmlString destructor
	~TiXmlString ()
	{
		quit();
	}

	TiXmlString& operator = (const char * copy)
	{
		return assign( copy, (size_type)strlen(copy));
	}

	TiXmlString& operator = (const TiXmlString & copy)
	{
		return assign(copy.start(), copy.length());
	}


	// += operator. Maps to append
	TiXmlString& operator += (const char * suffix)
	{
		return append(suffix, static_cast<size_type>( strlen(suffix) ));
	}

	// += operator. Maps to append
	TiXmlString& operator += (char single)
	{
		return append(&single, 1);
	}

	// += operator. Maps to append
	TiXmlString& operator += (const TiXmlString & suffix)
	{
		return append(suffix.data(), suffix.length());
	}


	// Convert a TiXmlString into a null-terminated char *
	const char * c_str () const { return rep_->str; }

	// Convert a TiXmlString into a char * (need not be null terminated).
	const char * data () const { return rep_->str; }

	// Return the length of a TiXmlString
	size_type length () const { return rep_->size; }

	// Alias for length()
	size_type size () const { return rep_->size; }

	// Checks if a TiXmlString is empty
	bool empty () const { return rep_->size == 0; }

	// Return capacity of string
	size_type capacity () const { return rep_->capacity; }


	// single char extraction
	const char& at (size_type index) const
	{
		assert( index < length() );
		return rep_->str[ index ];
	}

	// [] operator
	char& operator [] (size_type index) const
	{
		assert( index < length() );
		return rep_->str[ index ];
	}

	// find a char in a string. Return TiXmlString::npos if not found
	size_type find (char lookup) const
	{
		return find(lookup, 0);
	}

	// find a char in a string from an offset. Return TiXmlString::npos if not found
	size_type find (char tofind, size_type offset) const
	{
		if (offset >= length()) return npos;

		for (const char* p = c_str() + offset; *p != '\0'; ++p)
		{
		   if (*p == tofind) return static_cast< size_type >( p - c_str() );
		}
		return npos;
	}

	void clear ()
	{
		//Lee:
		//The original was just too strange, though correct:
		//	TiXmlString().swap(*this);
		//Instead use the quit & re-init:
		quit();
		init(0,0);
	}

	/*	Function to reserve a big amount of data when we know we'll need it. Be aware that this
		function DOES NOT clear the content of the TiXmlString if any exists.
	*/
	void reserve (size_type cap);

	TiXmlString& assign (const char* str, size_type len);

	TiXmlString& append (const char* str, size_type len);

	void swap (TiXmlString& other)
	{
		Rep* r = rep_;
		rep_ = other.rep_;
		other.rep_ = r;
	}

  private:

	void init(size_type sz) { init(sz, sz); }
	void set_size(size_type sz) { rep_->str[ rep_->size = sz ] = '\0'; }
	char* start() const { return rep_->str; }
	char* finish() const { return rep_->str + rep_->size; }

	struct Rep
	{
		size_type size, capacity;
		char str[1];
	};

	void init(size_type sz, size_type cap)
	{
		if (cap)
		{
			// Lee: the original form:
			//	rep_ = static_cast<Rep*>(operator new(sizeof(Rep) + cap));
			// doesn't work in some cases of new being overloaded. Switching
			// to the normal allocation, although use an 'int' for systems
			// that are overly picky about structure alignment.
			const size_type bytesNeeded = sizeof(Rep) + cap;
			const size_type intsNeeded = ( bytesNeeded + sizeof(int) - 1 ) / sizeof( int ); 
			rep_ = reinterpret_cast<Rep*>( new int[ intsNeeded ] );

			rep_->str[ rep_->size = sz ] = '\0';
			rep_->capacity = cap;
		}
		else
		{
			rep_ = &nullrep_;
		}
	}

	void quit()
	{
		if (rep_ != &nullrep_)
		{
			// The rep_ is really an array of ints. (see the allocator, above).
			// Cast it back before delete, so the compiler won't incorrectly call destructors.
			delete [] ( reinterpret_cast<int*>( rep_ ) );
		}
	}

	Rep * rep_;
	static Rep nullrep_;

} ;


inline bool operator == (const TiXmlString & a, const TiXmlString & b)
{
	return    ( a.length() == b.length() )				// optimization on some platforms
	       && ( strcmp(a.c_str(), b.c_str()) == 0 );	// actual compare
}
inline bool operator < (const TiXmlString & a, const TiXmlString & b)
{
	return strcmp(a.c_str(), b.c_str()) < 0;
}

inline bool operator != (const TiXmlString & a, const TiXmlString & b) { return !(a == b); }
inline bool operator >  (const TiXmlString & a, const TiXmlString & b) { return b < a; }
inline bool operator <= (const TiXmlString & a, const TiXmlString & b) { return !(b < a); }
inline bool operator >= (const TiXmlString & a, const TiXmlString & b) { return !(a < b); }

inline bool operator == (const TiXmlString & a, const char* b) { return strcmp(a.c_str(), b) == 0; }
inline bool operator == (const char* a, const TiXmlString & b) { return b == a; }
inline bool operator != (const TiXmlString & a, const char* b) { return !(a == b); }
inline bool operator != (const char* a, const TiXmlString & b) { return !(b == a); }

TiXmlString operator + (const TiXmlString & a, const TiXmlString & b);
TiXmlString operator + (const TiXmlString & a, const char* b);
TiXmlString operator + (const char* a, const TiXmlString & b);


/*
   TiXmlOutStream is an emulation of std::ostream. It is based on TiXmlString.
   Only the operators that we need for TinyXML have been developped.
*/
class TiXmlOutStream : public TiXmlString
{
public :

	// TiXmlOutStream << operator.
	TiXmlOutStream & operator << (const TiXmlString & in)
	{
		*this += in;
		return *this;
	}

	// TiXmlOutStream << operator.
	TiXmlOutStream & operator << (const char * in)
	{
		*this += in;
		return *this;
	}

} ;

#endif	// TIXML_STRING_INCLUDED
#endif	// TIXML_USE_STL
```

## ServerLibrary\Util\tinyXml\tinyxml.cpp
```cpp
/*
www.sourceforge.net/projects/tinyxml
Original code by Lee Thomason (www.grinninglizard.com)

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any
damages arising from the use of this software.

Permission is granted to anyone to use this software for any
purpose, including commercial applications, and to alter it and
redistribute it freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must
not claim that you wrote the original software. If you use this
software in a product, an acknowledgment in the product documentation
would be appreciated but is not required.

2. Altered source versions must be plainly marked as such, and
must not be misrepresented as being the original software.

3. This notice may not be removed or altered from any source
distribution.
*/
#include "stdafx.h"
#include <ctype.h>

#ifdef TIXML_USE_STL
#include <sstream>
#include <iostream>
#endif

#include "tinyxml.h"

FILE* TiXmlFOpen( const char* filename, const char* mode );

bool TiXmlBase::condenseWhiteSpace = true;

// Microsoft compiler security
FILE* TiXmlFOpen( const char* filename, const char* mode )
{
	#if defined(_MSC_VER) && (_MSC_VER >= 1400 )
		FILE* fp = 0;
		errno_t err = fopen_s( &fp, filename, mode );
		if ( !err && fp )
			return fp;
		return 0;
	#else
		return fopen( filename, mode );
	#endif
}

void TiXmlBase::EncodeString( const TIXML_STRING& str, TIXML_STRING* outString )
{
	int i=0;

	while( i<(int)str.length() )
	{
		unsigned char c = (unsigned char) str[i];

		if (    c == '&' 
		     && i < ( (int)str.length() - 2 )
			 && str[i+1] == '#'
			 && str[i+2] == 'x' )
		{
			// Hexadecimal character reference.
			// Pass through unchanged.
			// &#xA9;	-- copyright symbol, for example.
			//
			// The -1 is a bug fix from Rob Laveaux. It keeps
			// an overflow from happening if there is no ';'.
			// There are actually 2 ways to exit this loop -
			// while fails (error case) and break (semicolon found).
			// However, there is no mechanism (currently) for
			// this function to return an error.
			while ( i<(int)str.length()-1 )
			{
				outString->append( str.c_str() + i, 1 );
				++i;
				if ( str[i] == ';' )
					break;
			}
		}
		else if ( c == '&' )
		{
			outString->append( entity[0].str, entity[0].strLength );
			++i;
		}
		else if ( c == '<' )
		{
			outString->append( entity[1].str, entity[1].strLength );
			++i;
		}
		else if ( c == '>' )
		{
			outString->append( entity[2].str, entity[2].strLength );
			++i;
		}
		else if ( c == '\"' )
		{
			outString->append( entity[3].str, entity[3].strLength );
			++i;
		}
		else if ( c == '\'' )
		{
			outString->append( entity[4].str, entity[4].strLength );
			++i;
		}
		else if ( c < 32 )
		{
			// Easy pass at non-alpha/numeric/symbol
			// Below 32 is symbolic.
			char buf[ 32 ];
			
			#if defined(TIXML_SNPRINTF)		
				TIXML_SNPRINTF( buf, sizeof(buf), "&#x%02X;", (unsigned) ( c & 0xff ) );
			#else
				sprintf( buf, "&#x%02X;", (unsigned) ( c & 0xff ) );
			#endif		

			//*ME:	warning C4267: convert 'size_t' to 'int'
			//*ME:	Int-Cast to make compiler happy ...
			outString->append( buf, (int)strlen( buf ) );
			++i;
		}
		else
		{
			//char realc = (char) c;
			//outString->append( &realc, 1 );
			*outString += (char) c;	// somewhat more efficient function call.
			++i;
		}
	}
}


TiXmlNode::TiXmlNode( NodeType _type ) : TiXmlBase()
{
	parent = 0;
	type = _type;
	firstChild = 0;
	lastChild = 0;
	prev = 0;
	next = 0;
}


TiXmlNode::~TiXmlNode()
{
	TiXmlNode* node = firstChild;
	TiXmlNode* temp = 0;

	while ( node )
	{
		temp = node;
		node = node->next;
		delete temp;
	}	
}


void TiXmlNode::CopyTo( TiXmlNode* target ) const
{
	target->SetValue (value.c_str() );
	target->userData = userData; 
	target->location = location;
}


void TiXmlNode::Clear()
{
	TiXmlNode* node = firstChild;
	TiXmlNode* temp = 0;

	while ( node )
	{
		temp = node;
		node = node->next;
		delete temp;
	}	

	firstChild = 0;
	lastChild = 0;
}


TiXmlNode* TiXmlNode::LinkEndChild( TiXmlNode* node )
{
	assert( node->parent == 0 || node->parent == this );
	assert( node->GetDocument() == 0 || node->GetDocument() == this->GetDocument() );

	if ( node->Type() == TiXmlNode::TINYXML_DOCUMENT )
	{
		delete node;
		if ( GetDocument() ) 
			GetDocument()->SetError( TIXML_ERROR_DOCUMENT_TOP_ONLY, 0, 0, TIXML_ENCODING_UNKNOWN );
		return 0;
	}

	node->parent = this;

	node->prev = lastChild;
	node->next = 0;

	if ( lastChild )
		lastChild->next = node;
	else
		firstChild = node;			// it was an empty list.

	lastChild = node;
	return node;
}


TiXmlNode* TiXmlNode::InsertEndChild( const TiXmlNode& addThis )
{
	if ( addThis.Type() == TiXmlNode::TINYXML_DOCUMENT )
	{
		if ( GetDocument() ) 
			GetDocument()->SetError( TIXML_ERROR_DOCUMENT_TOP_ONLY, 0, 0, TIXML_ENCODING_UNKNOWN );
		return 0;
	}
	TiXmlNode* node = addThis.Clone();
	if ( !node )
		return 0;

	return LinkEndChild( node );
}


TiXmlNode* TiXmlNode::InsertBeforeChild( TiXmlNode* beforeThis, const TiXmlNode& addThis )
{	
	if ( !beforeThis || beforeThis->parent != this ) {
		return 0;
	}
	if ( addThis.Type() == TiXmlNode::TINYXML_DOCUMENT )
	{
		if ( GetDocument() ) 
			GetDocument()->SetError( TIXML_ERROR_DOCUMENT_TOP_ONLY, 0, 0, TIXML_ENCODING_UNKNOWN );
		return 0;
	}

	TiXmlNode* node = addThis.Clone();
	if ( !node )
		return 0;
	node->parent = this;

	node->next = beforeThis;
	node->prev = beforeThis->prev;
	if ( beforeThis->prev )
	{
		beforeThis->prev->next = node;
	}
	else
	{
		assert( firstChild == beforeThis );
		firstChild = node;
	}
	beforeThis->prev = node;
	return node;
}


TiXmlNode* TiXmlNode::InsertAfterChild( TiXmlNode* afterThis, const TiXmlNode& addThis )
{
	if ( !afterThis || afterThis->parent != this ) {
		return 0;
	}
	if ( addThis.Type() == TiXmlNode::TINYXML_DOCUMENT )
	{
		if ( GetDocument() ) 
			GetDocument()->SetError( TIXML_ERROR_DOCUMENT_TOP_ONLY, 0, 0, TIXML_ENCODING_UNKNOWN );
		return 0;
	}

	TiXmlNode* node = addThis.Clone();
	if ( !node )
		return 0;
	node->parent = this;

	node->prev = afterThis;
	node->next = afterThis->next;
	if ( afterThis->next )
	{
		afterThis->next->prev = node;
	}
	else
	{
		assert( lastChild == afterThis );
		lastChild = node;
	}
	afterThis->next = node;
	return node;
}


TiXmlNode* TiXmlNode::ReplaceChild( TiXmlNode* replaceThis, const TiXmlNode& withThis )
{
	if ( !replaceThis )
		return 0;

	if ( replaceThis->parent != this )
		return 0;

	if ( withThis.ToDocument() ) {
		// A document can never be a child.	Thanks to Noam.
		TiXmlDocument* document = GetDocument();
		if ( document ) 
			document->SetError( TIXML_ERROR_DOCUMENT_TOP_ONLY, 0, 0, TIXML_ENCODING_UNKNOWN );
		return 0;
	}

	TiXmlNode* node = withThis.Clone();
	if ( !node )
		return 0;

	node->next = replaceThis->next;
	node->prev = replaceThis->prev;

	if ( replaceThis->next )
		replaceThis->next->prev = node;
	else
		lastChild = node;

	if ( replaceThis->prev )
		replaceThis->prev->next = node;
	else
		firstChild = node;

	delete replaceThis;
	node->parent = this;
	return node;
}


bool TiXmlNode::RemoveChild( TiXmlNode* removeThis )
{
	if ( !removeThis ) {
		return false;
	}

	if ( removeThis->parent != this )
	{	
		assert( 0 );
		return false;
	}

	if ( removeThis->next )
		removeThis->next->prev = removeThis->prev;
	else
		lastChild = removeThis->prev;

	if ( removeThis->prev )
		removeThis->prev->next = removeThis->next;
	else
		firstChild = removeThis->next;

	delete removeThis;
	return true;
}

const TiXmlNode* TiXmlNode::FirstChild( const char * _value ) const
{
	const TiXmlNode* node;
	for ( node = firstChild; node; node = node->next )
	{
		if ( strcmp( node->Value(), _value ) == 0 )
			return node;
	}
	return 0;
}


const TiXmlNode* TiXmlNode::LastChild( const char * _value ) const
{
	const TiXmlNode* node;
	for ( node = lastChild; node; node = node->prev )
	{
		if ( strcmp( node->Value(), _value ) == 0 )
			return node;
	}
	return 0;
}


const TiXmlNode* TiXmlNode::IterateChildren( const TiXmlNode* previous ) const
{
	if ( !previous )
	{
		return FirstChild();
	}
	else
	{
		assert( previous->parent == this );
		return previous->NextSibling();
	}
}


const TiXmlNode* TiXmlNode::IterateChildren( const char * val, const TiXmlNode* previous ) const
{
	if ( !previous )
	{
		return FirstChild( val );
	}
	else
	{
		assert( previous->parent == this );
		return previous->NextSibling( val );
	}
}


const TiXmlNode* TiXmlNode::NextSibling( const char * _value ) const 
{
	const TiXmlNode* node;
	for ( node = next; node; node = node->next )
	{
		if ( strcmp( node->Value(), _value ) == 0 )
			return node;
	}
	return 0;
}


const TiXmlNode* TiXmlNode::PreviousSibling( const char * _value ) const
{
	const TiXmlNode* node;
	for ( node = prev; node; node = node->prev )
	{
		if ( strcmp( node->Value(), _value ) == 0 )
			return node;
	}
	return 0;
}


void TiXmlElement::RemoveAttribute( const char * name )
{
    #ifdef TIXML_USE_STL
	TIXML_STRING str( name );
	TiXmlAttribute* node = attributeSet.Find( str );
	#else
	TiXmlAttribute* node = attributeSet.Find( name );
	#endif
	if ( node )
	{
		attributeSet.Remove( node );
		delete node;
	}
}

const TiXmlElement* TiXmlNode::FirstChildElement() const
{
	const TiXmlNode* node;

	for (	node = FirstChild();
			node;
			node = node->NextSibling() )
	{
		if ( node->ToElement() )
			return node->ToElement();
	}
	return 0;
}


const TiXmlElement* TiXmlNode::FirstChildElement( const char * _value ) const
{
	const TiXmlNode* node;

	for (	node = FirstChild( _value );
			node;
			node = node->NextSibling( _value ) )
	{
		if ( node->ToElement() )
			return node->ToElement();
	}
	return 0;
}


const TiXmlElement* TiXmlNode::NextSiblingElement() const
{
	const TiXmlNode* node;

	for (	node = NextSibling();
			node;
			node = node->NextSibling() )
	{
		if ( node->ToElement() )
			return node->ToElement();
	}
	return 0;
}


const TiXmlElement* TiXmlNode::NextSiblingElement( const char * _value ) const
{
	const TiXmlNode* node;

	for (	node = NextSibling( _value );
			node;
			node = node->NextSibling( _value ) )
	{
		if ( node->ToElement() )
			return node->ToElement();
	}
	return 0;
}


const TiXmlDocument* TiXmlNode::GetDocument() const
{
	const TiXmlNode* node;

	for( node = this; node; node = node->parent )
	{
		if ( node->ToDocument() )
			return node->ToDocument();
	}
	return 0;
}


TiXmlElement::TiXmlElement (const char * _value)
	: TiXmlNode( TiXmlNode::TINYXML_ELEMENT )
{
	firstChild = lastChild = 0;
	value = _value;
}


#ifdef TIXML_USE_STL
TiXmlElement::TiXmlElement( const std::string& _value ) 
	: TiXmlNode( TiXmlNode::TINYXML_ELEMENT )
{
	firstChild = lastChild = 0;
	value = _value;
}
#endif


TiXmlElement::TiXmlElement( const TiXmlElement& copy)
	: TiXmlNode( TiXmlNode::TINYXML_ELEMENT )
{
	firstChild = lastChild = 0;
	copy.CopyTo( this );	
}


TiXmlElement& TiXmlElement::operator=( const TiXmlElement& base )
{
	ClearThis();
	base.CopyTo( this );
	return *this;
}


TiXmlElement::~TiXmlElement()
{
	ClearThis();
}


void TiXmlElement::ClearThis()
{
	Clear();
	while( attributeSet.First() )
	{
		TiXmlAttribute* node = attributeSet.First();
		attributeSet.Remove( node );
		delete node;
	}
}


const char* TiXmlElement::Attribute( const char* name ) const
{
	const TiXmlAttribute* node = attributeSet.Find( name );
	if ( node )
		return node->Value();
	return 0;
}


#ifdef TIXML_USE_STL
const std::string* TiXmlElement::Attribute( const std::string& name ) const
{
	const TiXmlAttribute* attrib = attributeSet.Find( name );
	if ( attrib )
		return &attrib->ValueStr();
	return 0;
}
#endif


const char* TiXmlElement::Attribute( const char* name, int* i ) const
{
	const TiXmlAttribute* attrib = attributeSet.Find( name );
	const char* result = 0;

	if ( attrib ) {
		result = attrib->Value();
		if ( i ) {
			attrib->QueryIntValue( i );
		}
	}
	return result;
}


#ifdef TIXML_USE_STL
const std::string* TiXmlElement::Attribute( const std::string& name, int* i ) const
{
	const TiXmlAttribute* attrib = attributeSet.Find( name );
	const std::string* result = 0;

	if ( attrib ) {
		result = &attrib->ValueStr();
		if ( i ) {
			attrib->QueryIntValue( i );
		}
	}
	return result;
}
#endif


const char* TiXmlElement::Attribute( const char* name, double* d ) const
{
	const TiXmlAttribute* attrib = attributeSet.Find( name );
	const char* result = 0;

	if ( attrib ) {
		result = attrib->Value();
		if ( d ) {
			attrib->QueryDoubleValue( d );
		}
	}
	return result;
}


#ifdef TIXML_USE_STL
const std::string* TiXmlElement::Attribute( const std::string& name, double* d ) const
{
	const TiXmlAttribute* attrib = attributeSet.Find( name );
	const std::string* result = 0;

	if ( attrib ) {
		result = &attrib->ValueStr();
		if ( d ) {
			attrib->QueryDoubleValue( d );
		}
	}
	return result;
}
#endif


int TiXmlElement::QueryIntAttribute( const char* name, int* ival ) const
{
	const TiXmlAttribute* attrib = attributeSet.Find( name );
	if ( !attrib )
		return TIXML_NO_ATTRIBUTE;
	return attrib->QueryIntValue( ival );
}


int TiXmlElement::QueryUnsignedAttribute( const char* name, unsigned* value ) const
{
	const TiXmlAttribute* node = attributeSet.Find( name );
	if ( !node )
		return TIXML_NO_ATTRIBUTE;

	int ival = 0;
	int result = node->QueryIntValue( &ival );
	*value = (unsigned)ival;
	return result;
}


int TiXmlElement::QueryBoolAttribute( const char* name, bool* bval ) const
{
	const TiXmlAttribute* node = attributeSet.Find( name );
	if ( !node )
		return TIXML_NO_ATTRIBUTE;
	
	int result = TIXML_WRONG_TYPE;
	if (    StringEqual( node->Value(), "true", true, TIXML_ENCODING_UNKNOWN ) 
		 || StringEqual( node->Value(), "yes", true, TIXML_ENCODING_UNKNOWN ) 
		 || StringEqual( node->Value(), "1", true, TIXML_ENCODING_UNKNOWN ) ) 
	{
		*bval = true;
		result = TIXML_SUCCESS;
	}
	else if (    StringEqual( node->Value(), "false", true, TIXML_ENCODING_UNKNOWN ) 
			  || StringEqual( node->Value(), "no", true, TIXML_ENCODING_UNKNOWN ) 
			  || StringEqual( node->Value(), "0", true, TIXML_ENCODING_UNKNOWN ) ) 
	{
		*bval = false;
		result = TIXML_SUCCESS;
	}
	return result;
}



#ifdef TIXML_USE_STL
int TiXmlElement::QueryIntAttribute( const std::string& name, int* ival ) const
{
	const TiXmlAttribute* attrib = attributeSet.Find( name );
	if ( !attrib )
		return TIXML_NO_ATTRIBUTE;
	return attrib->QueryIntValue( ival );
}
#endif


int TiXmlElement::QueryDoubleAttribute( const char* name, double* dval ) const
{
	const TiXmlAttribute* attrib = attributeSet.Find( name );
	if ( !attrib )
		return TIXML_NO_ATTRIBUTE;
	return attrib->QueryDoubleValue( dval );
}


#ifdef TIXML_USE_STL
int TiXmlElement::QueryDoubleAttribute( const std::string& name, double* dval ) const
{
	const TiXmlAttribute* attrib = attributeSet.Find( name );
	if ( !attrib )
		return TIXML_NO_ATTRIBUTE;
	return attrib->QueryDoubleValue( dval );
}
#endif


void TiXmlElement::SetAttribute( const char * name, int val )
{	
	TiXmlAttribute* attrib = attributeSet.FindOrCreate( name );
	if ( attrib ) {
		attrib->SetIntValue( val );
	}
}


#ifdef TIXML_USE_STL
void TiXmlElement::SetAttribute( const std::string& name, int val )
{	
	TiXmlAttribute* attrib = attributeSet.FindOrCreate( name );
	if ( attrib ) {
		attrib->SetIntValue( val );
	}
}
#endif


void TiXmlElement::SetDoubleAttribute( const char * name, double val )
{	
	TiXmlAttribute* attrib = attributeSet.FindOrCreate( name );
	if ( attrib ) {
		attrib->SetDoubleValue( val );
	}
}


#ifdef TIXML_USE_STL
void TiXmlElement::SetDoubleAttribute( const std::string& name, double val )
{	
	TiXmlAttribute* attrib = attributeSet.FindOrCreate( name );
	if ( attrib ) {
		attrib->SetDoubleValue( val );
	}
}
#endif 


void TiXmlElement::SetAttribute( const char * cname, const char * cvalue )
{
	TiXmlAttribute* attrib = attributeSet.FindOrCreate( cname );
	if ( attrib ) {
		attrib->SetValue( cvalue );
	}
}


#ifdef TIXML_USE_STL
void TiXmlElement::SetAttribute( const std::string& _name, const std::string& _value )
{
	TiXmlAttribute* attrib = attributeSet.FindOrCreate( _name );
	if ( attrib ) {
		attrib->SetValue( _value );
	}
}
#endif


void TiXmlElement::Print( FILE* cfile, int depth ) const
{
	int i;
	assert( cfile );
	for ( i=0; i<depth; i++ ) {
		fprintf( cfile, "    " );
	}

	fprintf( cfile, "<%s", value.c_str() );

	const TiXmlAttribute* attrib;
	for ( attrib = attributeSet.First(); attrib; attrib = attrib->Next() )
	{
		fprintf( cfile, " " );
		attrib->Print( cfile, depth );
	}

	// There are 3 different formatting approaches:
	// 1) An element without children is printed as a <foo /> node
	// 2) An element with only a text child is printed as <foo> text </foo>
	// 3) An element with children is printed on multiple lines.
	TiXmlNode* node;
	if ( !firstChild )
	{
		fprintf( cfile, " />" );
	}
	else if ( firstChild == lastChild && firstChild->ToText() )
	{
		fprintf( cfile, ">" );
		firstChild->Print( cfile, depth + 1 );
		fprintf( cfile, "</%s>", value.c_str() );
	}
	else
	{
		fprintf( cfile, ">" );

		for ( node = firstChild; node; node=node->NextSibling() )
		{
			if ( !node->ToText() )
			{
				fprintf( cfile, "\n" );
			}
			node->Print( cfile, depth+1 );
		}
		fprintf( cfile, "\n" );
		for( i=0; i<depth; ++i ) {
			fprintf( cfile, "    " );
		}
		fprintf( cfile, "</%s>", value.c_str() );
	}
}


void TiXmlElement::CopyTo( TiXmlElement* target ) const
{
	// superclass:
	TiXmlNode::CopyTo( target );

	// Element class: 
	// Clone the attributes, then clone the children.
	const TiXmlAttribute* attribute = 0;
	for(	attribute = attributeSet.First();
	attribute;
	attribute = attribute->Next() )
	{
		target->SetAttribute( attribute->Name(), attribute->Value() );
	}

	TiXmlNode* node = 0;
	for ( node = firstChild; node; node = node->NextSibling() )
	{
		target->LinkEndChild( node->Clone() );
	}
}

bool TiXmlElement::Accept( TiXmlVisitor* visitor ) const
{
	if ( visitor->VisitEnter( *this, attributeSet.First() ) ) 
	{
		for ( const TiXmlNode* node=FirstChild(); node; node=node->NextSibling() )
		{
			if ( !node->Accept( visitor ) )
				break;
		}
	}
	return visitor->VisitExit( *this );
}


TiXmlNode* TiXmlElement::Clone() const
{
	TiXmlElement* clone = new TiXmlElement( Value() );
	if ( !clone )
		return 0;

	CopyTo( clone );
	return clone;
}


const char* TiXmlElement::GetText() const
{
	const TiXmlNode* child = this->FirstChild();
	if ( child ) {
		const TiXmlText* childText = child->ToText();
		if ( childText ) {
			return childText->Value();
		}
	}
	return 0;
}


TiXmlDocument::TiXmlDocument() : TiXmlNode( TiXmlNode::TINYXML_DOCUMENT )
{
	tabsize = 4;
	useMicrosoftBOM = false;
	ClearError();
}

TiXmlDocument::TiXmlDocument( const char * documentName ) : TiXmlNode( TiXmlNode::TINYXML_DOCUMENT )
{
	tabsize = 4;
	useMicrosoftBOM = false;
	value = documentName;
	ClearError();
}


#ifdef TIXML_USE_STL
TiXmlDocument::TiXmlDocument( const std::string& documentName ) : TiXmlNode( TiXmlNode::TINYXML_DOCUMENT )
{
	tabsize = 4;
	useMicrosoftBOM = false;
    value = documentName;
	ClearError();
}
#endif


TiXmlDocument::TiXmlDocument( const TiXmlDocument& copy ) : TiXmlNode( TiXmlNode::TINYXML_DOCUMENT )
{
	copy.CopyTo( this );
}


TiXmlDocument& TiXmlDocument::operator=( const TiXmlDocument& copy )
{
	Clear();
	copy.CopyTo( this );
	return *this;
}


bool TiXmlDocument::LoadFile( TiXmlEncoding encoding )
{
	return LoadFile( Value(), encoding );
}


bool TiXmlDocument::SaveFile() const
{
	return SaveFile( Value() );
}

bool TiXmlDocument::LoadFile( const char* _filename, TiXmlEncoding encoding )
{
	TIXML_STRING filename( _filename );
	value = filename;

	// reading in binary mode so that tinyxml can normalize the EOL
	FILE* file = TiXmlFOpen( value.c_str (), "rb" );	

	if ( file )
	{
		bool result = LoadFile( file, encoding );
		fclose( file );
		return result;
	}
	else
	{
		SetError( TIXML_ERROR_OPENING_FILE, 0, 0, TIXML_ENCODING_UNKNOWN );
		return false;
	}
}

bool TiXmlDocument::LoadFile( FILE* file, TiXmlEncoding encoding )
{
	if ( !file ) 
	{
		SetError( TIXML_ERROR_OPENING_FILE, 0, 0, TIXML_ENCODING_UNKNOWN );
		return false;
	}

	// Delete the existing data:
	Clear();
	location.Clear();

	// Get the file size, so we can pre-allocate the string. HUGE speed impact.
	long length = 0;
	fseek( file, 0, SEEK_END );
	length = ftell( file );
	fseek( file, 0, SEEK_SET );

	// Strange case, but good to handle up front.
	if ( length <= 0 )
	{
		SetError( TIXML_ERROR_DOCUMENT_EMPTY, 0, 0, TIXML_ENCODING_UNKNOWN );
		return false;
	}

	// Subtle bug here. TinyXml did use fgets. But from the XML spec:
	// 2.11 End-of-Line Handling
	// <snip>
	// <quote>
	// ...the XML processor MUST behave as if it normalized all line breaks in external 
	// parsed entities (including the document entity) on input, before parsing, by translating 
	// both the two-character sequence #xD #xA and any #xD that is not followed by #xA to 
	// a single #xA character.
	// </quote>
	//
	// It is not clear fgets does that, and certainly isn't clear it works cross platform. 
	// Generally, you expect fgets to translate from the convention of the OS to the c/unix
	// convention, and not work generally.

	/*
	while( fgets( buf, sizeof(buf), file ) )
	{
		data += buf;
	}
	*/

	char* buf = new char[ length+1 ];
	buf[0] = 0;

	if ( fread( buf, length, 1, file ) != 1 ) {
		delete [] buf;
		SetError( TIXML_ERROR_OPENING_FILE, 0, 0, TIXML_ENCODING_UNKNOWN );
		return false;
	}

	// Process the buffer in place to normalize new lines. (See comment above.)
	// Copies from the 'p' to 'q' pointer, where p can advance faster if
	// a newline-carriage return is hit.
	//
	// Wikipedia:
	// Systems based on ASCII or a compatible character set use either LF  (Line feed, '\n', 0x0A, 10 in decimal) or 
	// CR (Carriage return, '\r', 0x0D, 13 in decimal) individually, or CR followed by LF (CR+LF, 0x0D 0x0A)...
	//		* LF:    Multics, Unix and Unix-like systems (GNU/Linux, AIX, Xenix, Mac OS X, FreeBSD, etc.), BeOS, Amiga, RISC OS, and others
    //		* CR+LF: DEC RT-11 and most other early non-Unix, non-IBM OSes, CP/M, MP/M, DOS, OS/2, Microsoft Windows, Symbian OS
    //		* CR:    Commodore 8-bit machines, Apple II family, Mac OS up to version 9 and OS-9

	const char* p = buf;	// the read head
	char* q = buf;			// the write head
	const char CR = 0x0d;
	const char LF = 0x0a;

	buf[length] = 0;
	while( *p ) {
		assert( p < (buf+length) );
		assert( q <= (buf+length) );
		assert( q <= p );

		if ( *p == CR ) {
			*q++ = LF;
			p++;
			if ( *p == LF ) {		// check for CR+LF (and skip LF)
				p++;
			}
		}
		else {
			*q++ = *p++;
		}
	}
	assert( q <= (buf+length) );
	*q = 0;

	Parse( buf, 0, encoding );

	delete [] buf;
	return !Error();
}


bool TiXmlDocument::SaveFile( const char * filename ) const
{
	// The old c stuff lives on...
	FILE* fp = TiXmlFOpen( filename, "w" );
	if ( fp )
	{
		bool result = SaveFile( fp );
		fclose( fp );
		return result;
	}
	return false;
}


bool TiXmlDocument::SaveFile( FILE* fp ) const
{
	if ( useMicrosoftBOM ) 
	{
		const unsigned char TIXML_UTF_LEAD_0 = 0xefU;
		const unsigned char TIXML_UTF_LEAD_1 = 0xbbU;
		const unsigned char TIXML_UTF_LEAD_2 = 0xbfU;

		fputc( TIXML_UTF_LEAD_0, fp );
		fputc( TIXML_UTF_LEAD_1, fp );
		fputc( TIXML_UTF_LEAD_2, fp );
	}
	Print( fp, 0 );
	return (ferror(fp) == 0);
}


void TiXmlDocument::CopyTo( TiXmlDocument* target ) const
{
	TiXmlNode::CopyTo( target );

	target->error = error;
	target->errorId = errorId;
	target->errorDesc = errorDesc;
	target->tabsize = tabsize;
	target->errorLocation = errorLocation;
	target->useMicrosoftBOM = useMicrosoftBOM;

	TiXmlNode* node = 0;
	for ( node = firstChild; node; node = node->NextSibling() )
	{
		target->LinkEndChild( node->Clone() );
	}	
}


TiXmlNode* TiXmlDocument::Clone() const
{
	TiXmlDocument* clone = new TiXmlDocument();
	if ( !clone )
		return 0;

	CopyTo( clone );
	return clone;
}


void TiXmlDocument::Print( FILE* cfile, int depth ) const
{
	assert( cfile );
	for ( const TiXmlNode* node=FirstChild(); node; node=node->NextSibling() )
	{
		node->Print( cfile, depth );
		fprintf( cfile, "\n" );
	}
}


bool TiXmlDocument::Accept( TiXmlVisitor* visitor ) const
{
	if ( visitor->VisitEnter( *this ) )
	{
		for ( const TiXmlNode* node=FirstChild(); node; node=node->NextSibling() )
		{
			if ( !node->Accept( visitor ) )
				break;
		}
	}
	return visitor->VisitExit( *this );
}


const TiXmlAttribute* TiXmlAttribute::Next() const
{
	// We are using knowledge of the sentinel. The sentinel
	// have a value or name.
	if ( next->value.empty() && next->name.empty() )
		return 0;
	return next;
}

/*
TiXmlAttribute* TiXmlAttribute::Next()
{
	// We are using knowledge of the sentinel. The sentinel
	// have a value or name.
	if ( next->value.empty() && next->name.empty() )
		return 0;
	return next;
}
*/

const TiXmlAttribute* TiXmlAttribute::Previous() const
{
	// We are using knowledge of the sentinel. The sentinel
	// have a value or name.
	if ( prev->value.empty() && prev->name.empty() )
		return 0;
	return prev;
}

/*
TiXmlAttribute* TiXmlAttribute::Previous()
{
	// We are using knowledge of the sentinel. The sentinel
	// have a value or name.
	if ( prev->value.empty() && prev->name.empty() )
		return 0;
	return prev;
}
*/

void TiXmlAttribute::Print( FILE* cfile, int /*depth*/, TIXML_STRING* str ) const
{
	TIXML_STRING n, v;

	EncodeString( name, &n );
	EncodeString( value, &v );

	if (value.find ('\"') == TIXML_STRING::npos) {
		if ( cfile ) {
			fprintf (cfile, "%s=\"%s\"", n.c_str(), v.c_str() );
		}
		if ( str ) {
			(*str) += n; (*str) += "=\""; (*str) += v; (*str) += "\"";
		}
	}
	else {
		if ( cfile ) {
			fprintf (cfile, "%s='%s'", n.c_str(), v.c_str() );
		}
		if ( str ) {
			(*str) += n; (*str) += "='"; (*str) += v; (*str) += "'";
		}
	}
}


int TiXmlAttribute::QueryIntValue( int* ival ) const
{
	if ( TIXML_SSCANF( value.c_str(), "%d", ival ) == 1 )
		return TIXML_SUCCESS;
	return TIXML_WRONG_TYPE;
}

int TiXmlAttribute::QueryDoubleValue( double* dval ) const
{
	if ( TIXML_SSCANF( value.c_str(), "%lf", dval ) == 1 )
		return TIXML_SUCCESS;
	return TIXML_WRONG_TYPE;
}

void TiXmlAttribute::SetIntValue( int _value )
{
	char buf [64];
	#if defined(TIXML_SNPRINTF)		
		TIXML_SNPRINTF(buf, sizeof(buf), "%d", _value);
	#else
		sprintf (buf, "%d", _value);
	#endif
	SetValue (buf);
}

void TiXmlAttribute::SetDoubleValue( double _value )
{
	char buf [256];
	#if defined(TIXML_SNPRINTF)		
		TIXML_SNPRINTF( buf, sizeof(buf), "%g", _value);
	#else
		sprintf (buf, "%g", _value);
	#endif
	SetValue (buf);
}

int TiXmlAttribute::IntValue() const
{
	return atoi (value.c_str ());
}

double  TiXmlAttribute::DoubleValue() const
{
	return atof (value.c_str ());
}


TiXmlComment::TiXmlComment( const TiXmlComment& copy ) : TiXmlNode( TiXmlNode::TINYXML_COMMENT )
{
	copy.CopyTo( this );
}


TiXmlComment& TiXmlComment::operator=( const TiXmlComment& base )
{
	Clear();
	base.CopyTo( this );
	return *this;
}


void TiXmlComment::Print( FILE* cfile, int depth ) const
{
	assert( cfile );
	for ( int i=0; i<depth; i++ )
	{
		fprintf( cfile,  "    " );
	}
	fprintf( cfile, "<!--%s-->", value.c_str() );
}


void TiXmlComment::CopyTo( TiXmlComment* target ) const
{
	TiXmlNode::CopyTo( target );
}


bool TiXmlComment::Accept( TiXmlVisitor* visitor ) const
{
	return visitor->Visit( *this );
}


TiXmlNode* TiXmlComment::Clone() const
{
	TiXmlComment* clone = new TiXmlComment();

	if ( !clone )
		return 0;

	CopyTo( clone );
	return clone;
}


void TiXmlText::Print( FILE* cfile, int depth ) const
{
	assert( cfile );
	if ( cdata )
	{
		int i;
		fprintf( cfile, "\n" );
		for ( i=0; i<depth; i++ ) {
			fprintf( cfile, "    " );
		}
		fprintf( cfile, "<![CDATA[%s]]>\n", value.c_str() );	// unformatted output
	}
	else
	{
		TIXML_STRING buffer;
		EncodeString( value, &buffer );
		fprintf( cfile, "%s", buffer.c_str() );
	}
}


void TiXmlText::CopyTo( TiXmlText* target ) const
{
	TiXmlNode::CopyTo( target );
	target->cdata = cdata;
}


bool TiXmlText::Accept( TiXmlVisitor* visitor ) const
{
	return visitor->Visit( *this );
}


TiXmlNode* TiXmlText::Clone() const
{	
	TiXmlText* clone = 0;
	clone = new TiXmlText( "" );

	if ( !clone )
		return 0;

	CopyTo( clone );
	return clone;
}


TiXmlDeclaration::TiXmlDeclaration( const char * _version,
									const char * _encoding,
									const char * _standalone )
	: TiXmlNode( TiXmlNode::TINYXML_DECLARATION )
{
	version = _version;
	encoding = _encoding;
	standalone = _standalone;
}


#ifdef TIXML_USE_STL
TiXmlDeclaration::TiXmlDeclaration(	const std::string& _version,
									const std::string& _encoding,
									const std::string& _standalone )
	: TiXmlNode( TiXmlNode::TINYXML_DECLARATION )
{
	version = _version;
	encoding = _encoding;
	standalone = _standalone;
}
#endif


TiXmlDeclaration::TiXmlDeclaration( const TiXmlDeclaration& copy )
	: TiXmlNode( TiXmlNode::TINYXML_DECLARATION )
{
	copy.CopyTo( this );	
}


TiXmlDeclaration& TiXmlDeclaration::operator=( const TiXmlDeclaration& copy )
{
	Clear();
	copy.CopyTo( this );
	return *this;
}


void TiXmlDeclaration::Print( FILE* cfile, int /*depth*/, TIXML_STRING* str ) const
{
	if ( cfile ) fprintf( cfile, "<?xml " );
	if ( str )	 (*str) += "<?xml ";

	if ( !version.empty() ) {
		if ( cfile ) fprintf (cfile, "version=\"%s\" ", version.c_str ());
		if ( str ) { (*str) += "version=\""; (*str) += version; (*str) += "\" "; }
	}
	if ( !encoding.empty() ) {
		if ( cfile ) fprintf (cfile, "encoding=\"%s\" ", encoding.c_str ());
		if ( str ) { (*str) += "encoding=\""; (*str) += encoding; (*str) += "\" "; }
	}
	if ( !standalone.empty() ) {
		if ( cfile ) fprintf (cfile, "standalone=\"%s\" ", standalone.c_str ());
		if ( str ) { (*str) += "standalone=\""; (*str) += standalone; (*str) += "\" "; }
	}
	if ( cfile ) fprintf( cfile, "?>" );
	if ( str )	 (*str) += "?>";
}


void TiXmlDeclaration::CopyTo( TiXmlDeclaration* target ) const
{
	TiXmlNode::CopyTo( target );

	target->version = version;
	target->encoding = encoding;
	target->standalone = standalone;
}


bool TiXmlDeclaration::Accept( TiXmlVisitor* visitor ) const
{
	return visitor->Visit( *this );
}


TiXmlNode* TiXmlDeclaration::Clone() const
{	
	TiXmlDeclaration* clone = new TiXmlDeclaration();

	if ( !clone )
		return 0;

	CopyTo( clone );
	return clone;
}


void TiXmlUnknown::Print( FILE* cfile, int depth ) const
{
	for ( int i=0; i<depth; i++ )
		fprintf( cfile, "    " );
	fprintf( cfile, "<%s>", value.c_str() );
}


void TiXmlUnknown::CopyTo( TiXmlUnknown* target ) const
{
	TiXmlNode::CopyTo( target );
}


bool TiXmlUnknown::Accept( TiXmlVisitor* visitor ) const
{
	return visitor->Visit( *this );
}


TiXmlNode* TiXmlUnknown::Clone() const
{
	TiXmlUnknown* clone = new TiXmlUnknown();

	if ( !clone )
		return 0;

	CopyTo( clone );
	return clone;
}


TiXmlAttributeSet::TiXmlAttributeSet()
{
	sentinel.next = &sentinel;
	sentinel.prev = &sentinel;
}


TiXmlAttributeSet::~TiXmlAttributeSet()
{
	assert( sentinel.next == &sentinel );
	assert( sentinel.prev == &sentinel );
}


void TiXmlAttributeSet::Add( TiXmlAttribute* addMe )
{
    #ifdef TIXML_USE_STL
	assert( !Find( TIXML_STRING( addMe->Name() ) ) );	// Shouldn't be multiply adding to the set.
	#else
	assert( !Find( addMe->Name() ) );	// Shouldn't be multiply adding to the set.
	#endif

	addMe->next = &sentinel;
	addMe->prev = sentinel.prev;

	sentinel.prev->next = addMe;
	sentinel.prev      = addMe;
}

void TiXmlAttributeSet::Remove( TiXmlAttribute* removeMe )
{
	TiXmlAttribute* node;

	for( node = sentinel.next; node != &sentinel; node = node->next )
	{
		if ( node == removeMe )
		{
			node->prev->next = node->next;
			node->next->prev = node->prev;
			node->next = 0;
			node->prev = 0;
			return;
		}
	}
	assert( 0 );		// we tried to remove a non-linked attribute.
}


#ifdef TIXML_USE_STL
TiXmlAttribute* TiXmlAttributeSet::Find( const std::string& name ) const
{
	for( TiXmlAttribute* node = sentinel.next; node != &sentinel; node = node->next )
	{
		if ( node->name == name )
			return node;
	}
	return 0;
}

TiXmlAttribute* TiXmlAttributeSet::FindOrCreate( const std::string& _name )
{
	TiXmlAttribute* attrib = Find( _name );
	if ( !attrib ) {
		attrib = new TiXmlAttribute();
		Add( attrib );
		attrib->SetName( _name );
	}
	return attrib;
}
#endif


TiXmlAttribute* TiXmlAttributeSet::Find( const char* name ) const
{
	for( TiXmlAttribute* node = sentinel.next; node != &sentinel; node = node->next )
	{
		if ( strcmp( node->name.c_str(), name ) == 0 )
			return node;
	}
	return 0;
}


TiXmlAttribute* TiXmlAttributeSet::FindOrCreate( const char* _name )
{
	TiXmlAttribute* attrib = Find( _name );
	if ( !attrib ) {
		attrib = new TiXmlAttribute();
		Add( attrib );
		attrib->SetName( _name );
	}
	return attrib;
}


#ifdef TIXML_USE_STL	
std::istream& operator>> (std::istream & in, TiXmlNode & base)
{
	TIXML_STRING tag;
	tag.reserve( 8 * 1000 );
	base.StreamIn( &in, &tag );

	base.Parse( tag.c_str(), 0, TIXML_DEFAULT_ENCODING );
	return in;
}
#endif


#ifdef TIXML_USE_STL	
std::ostream& operator<< (std::ostream & out, const TiXmlNode & base)
{
	TiXmlPrinter printer;
	printer.SetStreamPrinting();
	base.Accept( &printer );
	out << printer.Str();

	return out;
}


std::string& operator<< (std::string& out, const TiXmlNode& base )
{
	TiXmlPrinter printer;
	printer.SetStreamPrinting();
	base.Accept( &printer );
	out.append( printer.Str() );

	return out;
}
#endif


TiXmlHandle TiXmlHandle::FirstChild() const
{
	if ( node )
	{
		TiXmlNode* child = node->FirstChild();
		if ( child )
			return TiXmlHandle( child );
	}
	return TiXmlHandle( 0 );
}


TiXmlHandle TiXmlHandle::FirstChild( const char * value ) const
{
	if ( node )
	{
		TiXmlNode* child = node->FirstChild( value );
		if ( child )
			return TiXmlHandle( child );
	}
	return TiXmlHandle( 0 );
}


TiXmlHandle TiXmlHandle::FirstChildElement() const
{
	if ( node )
	{
		TiXmlElement* child = node->FirstChildElement();
		if ( child )
			return TiXmlHandle( child );
	}
	return TiXmlHandle( 0 );
}


TiXmlHandle TiXmlHandle::FirstChildElement( const char * value ) const
{
	if ( node )
	{
		TiXmlElement* child = node->FirstChildElement( value );
		if ( child )
			return TiXmlHandle( child );
	}
	return TiXmlHandle( 0 );
}


TiXmlHandle TiXmlHandle::Child( int count ) const
{
	if ( node )
	{
		int i;
		TiXmlNode* child = node->FirstChild();
		for (	i=0;
				child && i<count;
				child = child->NextSibling(), ++i )
		{
			// nothing
		}
		if ( child )
			return TiXmlHandle( child );
	}
	return TiXmlHandle( 0 );
}


TiXmlHandle TiXmlHandle::Child( const char* value, int count ) const
{
	if ( node )
	{
		int i;
		TiXmlNode* child = node->FirstChild( value );
		for (	i=0;
				child && i<count;
				child = child->NextSibling( value ), ++i )
		{
			// nothing
		}
		if ( child )
			return TiXmlHandle( child );
	}
	return TiXmlHandle( 0 );
}


TiXmlHandle TiXmlHandle::ChildElement( int count ) const
{
	if ( node )
	{
		int i;
		TiXmlElement* child = node->FirstChildElement();
		for (	i=0;
				child && i<count;
				child = child->NextSiblingElement(), ++i )
		{
			// nothing
		}
		if ( child )
			return TiXmlHandle( child );
	}
	return TiXmlHandle( 0 );
}


TiXmlHandle TiXmlHandle::ChildElement( const char* value, int count ) const
{
	if ( node )
	{
		int i;
		TiXmlElement* child = node->FirstChildElement( value );
		for (	i=0;
				child && i<count;
				child = child->NextSiblingElement( value ), ++i )
		{
			// nothing
		}
		if ( child )
			return TiXmlHandle( child );
	}
	return TiXmlHandle( 0 );
}


bool TiXmlPrinter::VisitEnter( const TiXmlDocument& )
{
	return true;
}

bool TiXmlPrinter::VisitExit( const TiXmlDocument& )
{
	return true;
}

bool TiXmlPrinter::VisitEnter( const TiXmlElement& element, const TiXmlAttribute* firstAttribute )
{
	DoIndent();
	buffer += "<";
	buffer += element.Value();

	for( const TiXmlAttribute* attrib = firstAttribute; attrib; attrib = attrib->Next() )
	{
		buffer += " ";
		attrib->Print( 0, 0, &buffer );
	}

	if ( !element.FirstChild() ) 
	{
		buffer += " />";
		DoLineBreak();
	}
	else 
	{
		buffer += ">";
		if (    element.FirstChild()->ToText()
			  && element.LastChild() == element.FirstChild()
			  && element.FirstChild()->ToText()->CDATA() == false )
		{
			simpleTextPrint = true;
			// no DoLineBreak()!
		}
		else
		{
			DoLineBreak();
		}
	}
	++depth;	
	return true;
}


bool TiXmlPrinter::VisitExit( const TiXmlElement& element )
{
	--depth;
	if ( !element.FirstChild() ) 
	{
		// nothing.
	}
	else 
	{
		if ( simpleTextPrint )
		{
			simpleTextPrint = false;
		}
		else
		{
			DoIndent();
		}
		buffer += "</";
		buffer += element.Value();
		buffer += ">";
		DoLineBreak();
	}
	return true;
}


bool TiXmlPrinter::Visit( const TiXmlText& text )
{
	if ( text.CDATA() )
	{
		DoIndent();
		buffer += "<![CDATA[";
		buffer += text.Value();
		buffer += "]]>";
		DoLineBreak();
	}
	else if ( simpleTextPrint )
	{
		TIXML_STRING str;
		TiXmlBase::EncodeString( text.ValueTStr(), &str );
		buffer += str;
	}
	else
	{
		DoIndent();
		TIXML_STRING str;
		TiXmlBase::EncodeString( text.ValueTStr(), &str );
		buffer += str;
		DoLineBreak();
	}
	return true;
}


bool TiXmlPrinter::Visit( const TiXmlDeclaration& declaration )
{
	DoIndent();
	declaration.Print( 0, 0, &buffer );
	DoLineBreak();
	return true;
}


bool TiXmlPrinter::Visit( const TiXmlComment& comment )
{
	DoIndent();
	buffer += "<!--";
	buffer += comment.Value();
	buffer += "-->";
	DoLineBreak();
	return true;
}


bool TiXmlPrinter::Visit( const TiXmlUnknown& unknown )
{
	DoIndent();
	buffer += "<";
	buffer += unknown.Value();
	buffer += ">";
	DoLineBreak();
	return true;
}
```

## ServerLibrary\Util\tinyXml\tinyxml.h
```h
/*
www.sourceforge.net/projects/tinyxml
Original code by Lee Thomason (www.grinninglizard.com)

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any
damages arising from the use of this software.

Permission is granted to anyone to use this software for any
purpose, including commercial applications, and to alter it and
redistribute it freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must
not claim that you wrote the original software. If you use this
software in a product, an acknowledgment in the product documentation
would be appreciated but is not required.

2. Altered source versions must be plainly marked as such, and
must not be misrepresented as being the original software.

3. This notice may not be removed or altered from any source
distribution.
*/

#include "stdafx.h"
#ifndef TINYXML_INCLUDED
#define TINYXML_INCLUDED

#ifdef _MSC_VER
#pragma warning( push )
#pragma warning( disable : 4530 )
#pragma warning( disable : 4786 )
#endif

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

// Help out windows:
#if defined( _DEBUG ) && !defined( DEBUG )
#define DEBUG
#endif

#ifdef TIXML_USE_STL
	#include <string>
 	#include <iostream>
	#include <sstream>
	#define TIXML_STRING		std::string
#else
	#include "tinystr.h"
	#define TIXML_STRING		TiXmlString
#endif

// Deprecated library function hell. Compilers want to use the
// new safe versions. This probably doesn't fully address the problem,
// but it gets closer. There are too many compilers for me to fully
// test. If you get compilation troubles, undefine TIXML_SAFE
#define TIXML_SAFE

#ifdef TIXML_SAFE
	#if defined(_MSC_VER) && (_MSC_VER >= 1400 )
		// Microsoft visual studio, version 2005 and higher.
		#define TIXML_SNPRINTF _snprintf_s
		#define TIXML_SSCANF   sscanf_s
	#elif defined(_MSC_VER) && (_MSC_VER >= 1200 )
		// Microsoft visual studio, version 6 and higher.
		//#pragma message( "Using _sn* functions." )
		#define TIXML_SNPRINTF _snprintf
		#define TIXML_SSCANF   sscanf
	#elif defined(__GNUC__) && (__GNUC__ >= 3 )
		// GCC version 3 and higher.s
		//#warning( "Using sn* functions." )
		#define TIXML_SNPRINTF snprintf
		#define TIXML_SSCANF   sscanf
	#else
		#define TIXML_SNPRINTF snprintf
		#define TIXML_SSCANF   sscanf
	#endif
#endif	

class TiXmlDocument;
class TiXmlElement;
class TiXmlComment;
class TiXmlUnknown;
class TiXmlAttribute;
class TiXmlText;
class TiXmlDeclaration;
class TiXmlParsingData;

const int TIXML_MAJOR_VERSION = 2;
const int TIXML_MINOR_VERSION = 6;
const int TIXML_PATCH_VERSION = 2;

/*	Internal structure for tracking location of items 
	in the XML file.
*/
struct TiXmlCursor
{
	TiXmlCursor()		{ Clear(); }
	void Clear()		{ row = col = -1; }

	int row;	// 0 based.
	int col;	// 0 based.
};


/**
	Implements the interface to the "Visitor pattern" (see the Accept() method.)
	If you call the Accept() method, it requires being passed a TiXmlVisitor
	class to handle callbacks. For nodes that contain other nodes (Document, Element)
	you will get called with a VisitEnter/VisitExit pair. Nodes that are always leaves
	are simply called with Visit().

	If you return 'true' from a Visit method, recursive parsing will continue. If you return
	false, <b>no children of this node or its sibilings</b> will be Visited.

	All flavors of Visit methods have a default implementation that returns 'true' (continue 
	visiting). You need to only override methods that are interesting to you.

	Generally Accept() is called on the TiXmlDocument, although all nodes suppert Visiting.

	You should never change the document from a callback.

	@sa TiXmlNode::Accept()
*/
class TiXmlVisitor
{
public:
	virtual ~TiXmlVisitor() {}

	/// Visit a document.
	virtual bool VisitEnter( const TiXmlDocument& /*doc*/ )			{ return true; }
	/// Visit a document.
	virtual bool VisitExit( const TiXmlDocument& /*doc*/ )			{ return true; }

	/// Visit an element.
	virtual bool VisitEnter( const TiXmlElement& /*element*/, const TiXmlAttribute* /*firstAttribute*/ )	{ return true; }
	/// Visit an element.
	virtual bool VisitExit( const TiXmlElement& /*element*/ )		{ return true; }

	/// Visit a declaration
	virtual bool Visit( const TiXmlDeclaration& /*declaration*/ )	{ return true; }
	/// Visit a text node
	virtual bool Visit( const TiXmlText& /*text*/ )					{ return true; }
	/// Visit a comment node
	virtual bool Visit( const TiXmlComment& /*comment*/ )			{ return true; }
	/// Visit an unknown node
	virtual bool Visit( const TiXmlUnknown& /*unknown*/ )			{ return true; }
};

// Only used by Attribute::Query functions
enum 
{ 
	TIXML_SUCCESS,
	TIXML_NO_ATTRIBUTE,
	TIXML_WRONG_TYPE
};


// Used by the parsing routines.
enum TiXmlEncoding
{
	TIXML_ENCODING_UNKNOWN,
	TIXML_ENCODING_UTF8,
	TIXML_ENCODING_LEGACY
};

const TiXmlEncoding TIXML_DEFAULT_ENCODING = TIXML_ENCODING_UNKNOWN;

/** TiXmlBase is a base class for every class in TinyXml.
	It does little except to establish that TinyXml classes
	can be printed and provide some utility functions.

	In XML, the document and elements can contain
	other elements and other types of nodes.

	@verbatim
	A Document can contain:	Element	(container or leaf)
							Comment (leaf)
							Unknown (leaf)
							Declaration( leaf )

	An Element can contain:	Element (container or leaf)
							Text	(leaf)
							Attributes (not on tree)
							Comment (leaf)
							Unknown (leaf)

	A Decleration contains: Attributes (not on tree)
	@endverbatim
*/
class TiXmlBase
{
	friend class TiXmlNode;
	friend class TiXmlElement;
	friend class TiXmlDocument;

public:
	TiXmlBase()	:	userData(0)		{}
	virtual ~TiXmlBase()			{}

	/**	All TinyXml classes can print themselves to a filestream
		or the string class (TiXmlString in non-STL mode, std::string
		in STL mode.) Either or both cfile and str can be null.
		
		This is a formatted print, and will insert 
		tabs and newlines.
		
		(For an unformatted stream, use the << operator.)
	*/
	virtual void Print( FILE* cfile, int depth ) const = 0;

	/**	The world does not agree on whether white space should be kept or
		not. In order to make everyone happy, these global, static functions
		are provided to set whether or not TinyXml will condense all white space
		into a single space or not. The default is to condense. Note changing this
		value is not thread safe.
	*/
	static void SetCondenseWhiteSpace( bool condense )		{ condenseWhiteSpace = condense; }

	/// Return the current white space setting.
	static bool IsWhiteSpaceCondensed()						{ return condenseWhiteSpace; }

	/** Return the position, in the original source file, of this node or attribute.
		The row and column are 1-based. (That is the first row and first column is
		1,1). If the returns values are 0 or less, then the parser does not have
		a row and column value.

		Generally, the row and column value will be set when the TiXmlDocument::Load(),
		TiXmlDocument::LoadFile(), or any TiXmlNode::Parse() is called. It will NOT be set
		when the DOM was created from operator>>.

		The values reflect the initial load. Once the DOM is modified programmatically
		(by adding or changing nodes and attributes) the new values will NOT update to
		reflect changes in the document.

		There is a minor performance cost to computing the row and column. Computation
		can be disabled if TiXmlDocument::SetTabSize() is called with 0 as the value.

		@sa TiXmlDocument::SetTabSize()
	*/
	int Row() const			{ return location.row + 1; }
	int Column() const		{ return location.col + 1; }	///< See Row()

	void  SetUserData( void* user )			{ userData = user; }	///< Set a pointer to arbitrary user data.
	void* GetUserData()						{ return userData; }	///< Get a pointer to arbitrary user data.
	const void* GetUserData() const 		{ return userData; }	///< Get a pointer to arbitrary user data.

	// Table that returs, for a given lead byte, the total number of bytes
	// in the UTF-8 sequence.
	static const int utf8ByteTable[256];

	virtual const char* Parse(	const char* p, 
								TiXmlParsingData* data, 
								TiXmlEncoding encoding /*= TIXML_ENCODING_UNKNOWN */ ) = 0;

	/** Expands entities in a string. Note this should not contian the tag's '<', '>', etc, 
		or they will be transformed into entities!
	*/
	static void EncodeString( const TIXML_STRING& str, TIXML_STRING* out );

	enum
	{
		TIXML_NO_ERROR = 0,
		TIXML_ERROR,
		TIXML_ERROR_OPENING_FILE,
		TIXML_ERROR_PARSING_ELEMENT,
		TIXML_ERROR_FAILED_TO_READ_ELEMENT_NAME,
		TIXML_ERROR_READING_ELEMENT_VALUE,
		TIXML_ERROR_READING_ATTRIBUTES,
		TIXML_ERROR_PARSING_EMPTY,
		TIXML_ERROR_READING_END_TAG,
		TIXML_ERROR_PARSING_UNKNOWN,
		TIXML_ERROR_PARSING_COMMENT,
		TIXML_ERROR_PARSING_DECLARATION,
		TIXML_ERROR_DOCUMENT_EMPTY,
		TIXML_ERROR_EMBEDDED_NULL,
		TIXML_ERROR_PARSING_CDATA,
		TIXML_ERROR_DOCUMENT_TOP_ONLY,

		TIXML_ERROR_STRING_COUNT
	};

protected:

	static const char* SkipWhiteSpace( const char*, TiXmlEncoding encoding );

	inline static bool IsWhiteSpace( char c )		
	{ 
		return ( isspace( (unsigned char) c ) || c == '\n' || c == '\r' ); 
	}
	inline static bool IsWhiteSpace( int c )
	{
		if ( c < 256 )
			return IsWhiteSpace( (char) c );
		return false;	// Again, only truly correct for English/Latin...but usually works.
	}

	#ifdef TIXML_USE_STL
	static bool	StreamWhiteSpace( std::istream * in, TIXML_STRING * tag );
	static bool StreamTo( std::istream * in, int character, TIXML_STRING * tag );
	#endif

	/*	Reads an XML name into the string provided. Returns
		a pointer just past the last character of the name,
		or 0 if the function has an error.
	*/
	static const char* ReadName( const char* p, TIXML_STRING* name, TiXmlEncoding encoding );

	/*	Reads text. Returns a pointer past the given end tag.
		Wickedly complex options, but it keeps the (sensitive) code in one place.
	*/
	static const char* ReadText(	const char* in,				// where to start
									TIXML_STRING* text,			// the string read
									bool ignoreWhiteSpace,		// whether to keep the white space
									const char* endTag,			// what ends this text
									bool ignoreCase,			// whether to ignore case in the end tag
									TiXmlEncoding encoding );	// the current encoding

	// If an entity has been found, transform it into a character.
	static const char* GetEntity( const char* in, char* value, int* length, TiXmlEncoding encoding );

	// Get a character, while interpreting entities.
	// The length can be from 0 to 4 bytes.
	inline static const char* GetChar( const char* p, char* _value, int* length, TiXmlEncoding encoding )
	{
		assert( p );
		if ( encoding == TIXML_ENCODING_UTF8 )
		{
			*length = utf8ByteTable[ *((const unsigned char*)p) ];
			assert( *length >= 0 && *length < 5 );
		}
		else
		{
			*length = 1;
		}

		if ( *length == 1 )
		{
			if ( *p == '&' )
				return GetEntity( p, _value, length, encoding );
			*_value = *p;
			return p+1;
		}
		else if ( *length )
		{
			//strncpy( _value, p, *length );	// lots of compilers don't like this function (unsafe),
												// and the null terminator isn't needed
			for( int i=0; p[i] && i<*length; ++i ) {
				_value[i] = p[i];
			}
			return p + (*length);
		}
		else
		{
			// Not valid text.
			return 0;
		}
	}

	// Return true if the next characters in the stream are any of the endTag sequences.
	// Ignore case only works for english, and should only be relied on when comparing
	// to English words: StringEqual( p, "version", true ) is fine.
	static bool StringEqual(	const char* p,
								const char* endTag,
								bool ignoreCase,
								TiXmlEncoding encoding );

	static const char* errorString[ TIXML_ERROR_STRING_COUNT ];

	TiXmlCursor location;

    /// Field containing a generic user pointer
	void*			userData;
	
	// None of these methods are reliable for any language except English.
	// Good for approximation, not great for accuracy.
	static int IsAlpha( unsigned char anyByte, TiXmlEncoding encoding );
	static int IsAlphaNum( unsigned char anyByte, TiXmlEncoding encoding );
	inline static int ToLower( int v, TiXmlEncoding encoding )
	{
		if ( encoding == TIXML_ENCODING_UTF8 )
		{
			if ( v < 128 ) return tolower( v );
			return v;
		}
		else
		{
			return tolower( v );
		}
	}
	static void ConvertUTF32ToUTF8( unsigned long input, char* output, int* length );

private:
	TiXmlBase( const TiXmlBase& );				// not implemented.
	void operator=( const TiXmlBase& base );	// not allowed.

	struct Entity
	{
		const char*     str;
		unsigned int	strLength;
		char		    chr;
	};
	enum
	{
		NUM_ENTITY = 5,
		MAX_ENTITY_LENGTH = 6

	};
	static Entity entity[ NUM_ENTITY ];
	static bool condenseWhiteSpace;
};


/** The parent class for everything in the Document Object Model.
	(Except for attributes).
	Nodes have siblings, a parent, and children. A node can be
	in a document, or stand on its own. The type of a TiXmlNode
	can be queried, and it can be cast to its more defined type.
*/
class TiXmlNode : public TiXmlBase
{
	friend class TiXmlDocument;
	friend class TiXmlElement;

public:
	#ifdef TIXML_USE_STL	

	    /** An input stream operator, for every class. Tolerant of newlines and
		    formatting, but doesn't expect them.
	    */
	    friend std::istream& operator >> (std::istream& in, TiXmlNode& base);

	    /** An output stream operator, for every class. Note that this outputs
		    without any newlines or formatting, as opposed to Print(), which
		    includes tabs and new lines.

		    The operator<< and operator>> are not completely symmetric. Writing
		    a node to a stream is very well defined. You'll get a nice stream
		    of output, without any extra whitespace or newlines.
		    
		    But reading is not as well defined. (As it always is.) If you create
		    a TiXmlElement (for example) and read that from an input stream,
		    the text needs to define an element or junk will result. This is
		    true of all input streams, but it's worth keeping in mind.

		    A TiXmlDocument will read nodes until it reads a root element, and
			all the children of that root element.
	    */	
	    friend std::ostream& operator<< (std::ostream& out, const TiXmlNode& base);

		/// Appends the XML node or attribute to a std::string.
		friend std::string& operator<< (std::string& out, const TiXmlNode& base );

	#endif

	/** The types of XML nodes supported by TinyXml. (All the
			unsupported types are picked up by UNKNOWN.)
	*/
	enum NodeType
	{
		TINYXML_DOCUMENT,
		TINYXML_ELEMENT,
		TINYXML_COMMENT,
		TINYXML_UNKNOWN,
		TINYXML_TEXT,
		TINYXML_DECLARATION,
		TINYXML_TYPECOUNT
	};

	virtual ~TiXmlNode();

	/** The meaning of 'value' changes for the specific type of
		TiXmlNode.
		@verbatim
		Document:	filename of the xml file
		Element:	name of the element
		Comment:	the comment text
		Unknown:	the tag contents
		Text:		the text string
		@endverbatim

		The subclasses will wrap this function.
	*/
	const char *Value() const { return value.c_str (); }

    #ifdef TIXML_USE_STL
	/** Return Value() as a std::string. If you only use STL,
	    this is more efficient than calling Value().
		Only available in STL mode.
	*/
	const std::string& ValueStr() const { return value; }
	#endif

	const TIXML_STRING& ValueTStr() const { return value; }

	/** Changes the value of the node. Defined as:
		@verbatim
		Document:	filename of the xml file
		Element:	name of the element
		Comment:	the comment text
		Unknown:	the tag contents
		Text:		the text string
		@endverbatim
	*/
	void SetValue(const char * _value) { value = _value;}

    #ifdef TIXML_USE_STL
	/// STL std::string form.
	void SetValue( const std::string& _value )	{ value = _value; }
	#endif

	/// Delete all the children of this node. Does not affect 'this'.
	void Clear();

	/// One step up the DOM.
	TiXmlNode* Parent()							{ return parent; }
	const TiXmlNode* Parent() const				{ return parent; }

	const TiXmlNode* FirstChild()	const		{ return firstChild; }	///< The first child of this node. Will be null if there are no children.
	TiXmlNode* FirstChild()						{ return firstChild; }
	const TiXmlNode* FirstChild( const char * value ) const;			///< The first child of this node with the matching 'value'. Will be null if none found.
	/// The first child of this node with the matching 'value'. Will be null if none found.
	TiXmlNode* FirstChild( const char * _value ) {
		// Call through to the const version - safe since nothing is changed. Exiting syntax: cast this to a const (always safe)
		// call the method, cast the return back to non-const.
		return const_cast< TiXmlNode* > ((const_cast< const TiXmlNode* >(this))->FirstChild( _value ));
	}
	const TiXmlNode* LastChild() const	{ return lastChild; }		/// The last child of this node. Will be null if there are no children.
	TiXmlNode* LastChild()	{ return lastChild; }
	
	const TiXmlNode* LastChild( const char * value ) const;			/// The last child of this node matching 'value'. Will be null if there are no children.
	TiXmlNode* LastChild( const char * _value ) {
		return const_cast< TiXmlNode* > ((const_cast< const TiXmlNode* >(this))->LastChild( _value ));
	}

    #ifdef TIXML_USE_STL
	const TiXmlNode* FirstChild( const std::string& _value ) const	{	return FirstChild (_value.c_str ());	}	///< STL std::string form.
	TiXmlNode* FirstChild( const std::string& _value )				{	return FirstChild (_value.c_str ());	}	///< STL std::string form.
	const TiXmlNode* LastChild( const std::string& _value ) const	{	return LastChild (_value.c_str ());	}	///< STL std::string form.
	TiXmlNode* LastChild( const std::string& _value )				{	return LastChild (_value.c_str ());	}	///< STL std::string form.
	#endif

	/** An alternate way to walk the children of a node.
		One way to iterate over nodes is:
		@verbatim
			for( child = parent->FirstChild(); child; child = child->NextSibling() )
		@endverbatim

		IterateChildren does the same thing with the syntax:
		@verbatim
			child = 0;
			while( child = parent->IterateChildren( child ) )
		@endverbatim

		IterateChildren takes the previous child as input and finds
		the next one. If the previous child is null, it returns the
		first. IterateChildren will return null when done.
	*/
	const TiXmlNode* IterateChildren( const TiXmlNode* previous ) const;
	TiXmlNode* IterateChildren( const TiXmlNode* previous ) {
		return const_cast< TiXmlNode* >( (const_cast< const TiXmlNode* >(this))->IterateChildren( previous ) );
	}

	/// This flavor of IterateChildren searches for children with a particular 'value'
	const TiXmlNode* IterateChildren( const char * value, const TiXmlNode* previous ) const;
	TiXmlNode* IterateChildren( const char * _value, const TiXmlNode* previous ) {
		return const_cast< TiXmlNode* >( (const_cast< const TiXmlNode* >(this))->IterateChildren( _value, previous ) );
	}

    #ifdef TIXML_USE_STL
	const TiXmlNode* IterateChildren( const std::string& _value, const TiXmlNode* previous ) const	{	return IterateChildren (_value.c_str (), previous);	}	///< STL std::string form.
	TiXmlNode* IterateChildren( const std::string& _value, const TiXmlNode* previous ) {	return IterateChildren (_value.c_str (), previous);	}	///< STL std::string form.
	#endif

	/** Add a new node related to this. Adds a child past the LastChild.
		Returns a pointer to the new object or NULL if an error occured.
	*/
	TiXmlNode* InsertEndChild( const TiXmlNode& addThis );


	/** Add a new node related to this. Adds a child past the LastChild.

		NOTE: the node to be added is passed by pointer, and will be
		henceforth owned (and deleted) by tinyXml. This method is efficient
		and avoids an extra copy, but should be used with care as it
		uses a different memory model than the other insert functions.

		@sa InsertEndChild
	*/
	TiXmlNode* LinkEndChild( TiXmlNode* addThis );

	/** Add a new node related to this. Adds a child before the specified child.
		Returns a pointer to the new object or NULL if an error occured.
	*/
	TiXmlNode* InsertBeforeChild( TiXmlNode* beforeThis, const TiXmlNode& addThis );

	/** Add a new node related to this. Adds a child after the specified child.
		Returns a pointer to the new object or NULL if an error occured.
	*/
	TiXmlNode* InsertAfterChild(  TiXmlNode* afterThis, const TiXmlNode& addThis );

	/** Replace a child of this node.
		Returns a pointer to the new object or NULL if an error occured.
	*/
	TiXmlNode* ReplaceChild( TiXmlNode* replaceThis, const TiXmlNode& withThis );

	/// Delete a child of this node.
	bool RemoveChild( TiXmlNode* removeThis );

	/// Navigate to a sibling node.
	const TiXmlNode* PreviousSibling() const			{ return prev; }
	TiXmlNode* PreviousSibling()						{ return prev; }

	/// Navigate to a sibling node.
	const TiXmlNode* PreviousSibling( const char * ) const;
	TiXmlNode* PreviousSibling( const char *_prev ) {
		return const_cast< TiXmlNode* >( (const_cast< const TiXmlNode* >(this))->PreviousSibling( _prev ) );
	}

    #ifdef TIXML_USE_STL
	const TiXmlNode* PreviousSibling( const std::string& _value ) const	{	return PreviousSibling (_value.c_str ());	}	///< STL std::string form.
	TiXmlNode* PreviousSibling( const std::string& _value ) 			{	return PreviousSibling (_value.c_str ());	}	///< STL std::string form.
	const TiXmlNode* NextSibling( const std::string& _value) const		{	return NextSibling (_value.c_str ());	}	///< STL std::string form.
	TiXmlNode* NextSibling( const std::string& _value) 					{	return NextSibling (_value.c_str ());	}	///< STL std::string form.
	#endif

	/// Navigate to a sibling node.
	const TiXmlNode* NextSibling() const				{ return next; }
	TiXmlNode* NextSibling()							{ return next; }

	/// Navigate to a sibling node with the given 'value'.
	const TiXmlNode* NextSibling( const char * ) const;
	TiXmlNode* NextSibling( const char* _next ) {
		return const_cast< TiXmlNode* >( (const_cast< const TiXmlNode* >(this))->NextSibling( _next ) );
	}

	/** Convenience function to get through elements.
		Calls NextSibling and ToElement. Will skip all non-Element
		nodes. Returns 0 if there is not another element.
	*/
	const TiXmlElement* NextSiblingElement() const;
	TiXmlElement* NextSiblingElement() {
		return const_cast< TiXmlElement* >( (const_cast< const TiXmlNode* >(this))->NextSiblingElement() );
	}

	/** Convenience function to get through elements.
		Calls NextSibling and ToElement. Will skip all non-Element
		nodes. Returns 0 if there is not another element.
	*/
	const TiXmlElement* NextSiblingElement( const char * ) const;
	TiXmlElement* NextSiblingElement( const char *_next ) {
		return const_cast< TiXmlElement* >( (const_cast< const TiXmlNode* >(this))->NextSiblingElement( _next ) );
	}

    #ifdef TIXML_USE_STL
	const TiXmlElement* NextSiblingElement( const std::string& _value) const	{	return NextSiblingElement (_value.c_str ());	}	///< STL std::string form.
	TiXmlElement* NextSiblingElement( const std::string& _value)				{	return NextSiblingElement (_value.c_str ());	}	///< STL std::string form.
	#endif

	/// Convenience function to get through elements.
	const TiXmlElement* FirstChildElement()	const;
	TiXmlElement* FirstChildElement() {
		return const_cast< TiXmlElement* >( (const_cast< const TiXmlNode* >(this))->FirstChildElement() );
	}

	/// Convenience function to get through elements.
	const TiXmlElement* FirstChildElement( const char * _value ) const;
	TiXmlElement* FirstChildElement( const char * _value ) {
		return const_cast< TiXmlElement* >( (const_cast< const TiXmlNode* >(this))->FirstChildElement( _value ) );
	}

    #ifdef TIXML_USE_STL
	const TiXmlElement* FirstChildElement( const std::string& _value ) const	{	return FirstChildElement (_value.c_str ());	}	///< STL std::string form.
	TiXmlElement* FirstChildElement( const std::string& _value )				{	return FirstChildElement (_value.c_str ());	}	///< STL std::string form.
	#endif

	/** Query the type (as an enumerated value, above) of this node.
		The possible types are: TINYXML_DOCUMENT, TINYXML_ELEMENT, TINYXML_COMMENT,
								TINYXML_UNKNOWN, TINYXML_TEXT, and TINYXML_DECLARATION.
	*/
	int Type() const	{ return type; }

	/** Return a pointer to the Document this node lives in.
		Returns null if not in a document.
	*/
	const TiXmlDocument* GetDocument() const;
	TiXmlDocument* GetDocument() {
		return const_cast< TiXmlDocument* >( (const_cast< const TiXmlNode* >(this))->GetDocument() );
	}

	/// Returns true if this node has no children.
	bool NoChildren() const						{ return !firstChild; }

	virtual const TiXmlDocument*    ToDocument()    const { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type.
	virtual const TiXmlElement*     ToElement()     const { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type.
	virtual const TiXmlComment*     ToComment()     const { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type.
	virtual const TiXmlUnknown*     ToUnknown()     const { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type.
	virtual const TiXmlText*        ToText()        const { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type.
	virtual const TiXmlDeclaration* ToDeclaration() const { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type.

	virtual TiXmlDocument*          ToDocument()    { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type.
	virtual TiXmlElement*           ToElement()	    { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type.
	virtual TiXmlComment*           ToComment()     { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type.
	virtual TiXmlUnknown*           ToUnknown()	    { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type.
	virtual TiXmlText*	            ToText()        { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type.
	virtual TiXmlDeclaration*       ToDeclaration() { return 0; } ///< Cast to a more defined type. Will return null if not of the requested type.

	/** Create an exact duplicate of this node and return it. The memory must be deleted
		by the caller. 
	*/
	virtual TiXmlNode* Clone() const = 0;

	/** Accept a hierchical visit the nodes in the TinyXML DOM. Every node in the 
		XML tree will be conditionally visited and the host will be called back
		via the TiXmlVisitor interface.

		This is essentially a SAX interface for TinyXML. (Note however it doesn't re-parse
		the XML for the callbacks, so the performance of TinyXML is unchanged by using this
		interface versus any other.)

		The interface has been based on ideas from:

		- http://www.saxproject.org/
		- http://c2.com/cgi/wiki?HierarchicalVisitorPattern 

		Which are both good references for "visiting".

		An example of using Accept():
		@verbatim
		TiXmlPrinter printer;
		tinyxmlDoc.Accept( &printer );
		const char* xmlcstr = printer.CStr();
		@endverbatim
	*/
	virtual bool Accept( TiXmlVisitor* visitor ) const = 0;

protected:
	TiXmlNode( NodeType _type );

	// Copy to the allocated object. Shared functionality between Clone, Copy constructor,
	// and the assignment operator.
	void CopyTo( TiXmlNode* target ) const;

	#ifdef TIXML_USE_STL
	    // The real work of the input operator.
	virtual void StreamIn( std::istream* in, TIXML_STRING* tag ) = 0;
	#endif

	// Figure out what is at *p, and parse it. Returns null if it is not an xml node.
	TiXmlNode* Identify( const char* start, TiXmlEncoding encoding );

	TiXmlNode*		parent;
	NodeType		type;

	TiXmlNode*		firstChild;
	TiXmlNode*		lastChild;

	TIXML_STRING	value;

	TiXmlNode*		prev;
	TiXmlNode*		next;

private:
	TiXmlNode( const TiXmlNode& );				// not implemented.
	void operator=( const TiXmlNode& base );	// not allowed.
};


/** An attribute is a name-value pair. Elements have an arbitrary
	number of attributes, each with a unique name.

	@note The attributes are not TiXmlNodes, since they are not
		  part of the tinyXML document object model. There are other
		  suggested ways to look at this problem.
*/
class TiXmlAttribute : public TiXmlBase
{
	friend class TiXmlAttributeSet;

public:
	/// Construct an empty attribute.
	TiXmlAttribute() : TiXmlBase()
	{
		document = 0;
		prev = next = 0;
	}

	#ifdef TIXML_USE_STL
	/// std::string constructor.
	TiXmlAttribute( const std::string& _name, const std::string& _value )
	{
		name = _name;
		value = _value;
		document = 0;
		prev = next = 0;
	}
	#endif

	/// Construct an attribute with a name and value.
	TiXmlAttribute( const char * _name, const char * _value )
	{
		name = _name;
		value = _value;
		document = 0;
		prev = next = 0;
	}

	const char*		Name()  const		{ return name.c_str(); }		///< Return the name of this attribute.
	const char*		Value() const		{ return value.c_str(); }		///< Return the value of this attribute.
	#ifdef TIXML_USE_STL
	const std::string& ValueStr() const	{ return value; }				///< Return the value of this attribute.
	#endif
	int				IntValue() const;									///< Return the value of this attribute, converted to an integer.
	double			DoubleValue() const;								///< Return the value of this attribute, converted to a double.

	// Get the tinyxml string representation
	const TIXML_STRING& NameTStr() const { return name; }

	/** QueryIntValue examines the value string. It is an alternative to the
		IntValue() method with richer error checking.
		If the value is an integer, it is stored in 'value' and 
		the call returns TIXML_SUCCESS. If it is not
		an integer, it returns TIXML_WRONG_TYPE.

		A specialized but useful call. Note that for success it returns 0,
		which is the opposite of almost all other TinyXml calls.
	*/
	int QueryIntValue( int* _value ) const;
	/// QueryDoubleValue examines the value string. See QueryIntValue().
	int QueryDoubleValue( double* _value ) const;

	void SetName( const char* _name )	{ name = _name; }				///< Set the name of this attribute.
	void SetValue( const char* _value )	{ value = _value; }				///< Set the value.

	void SetIntValue( int _value );										///< Set the value from an integer.
	void SetDoubleValue( double _value );								///< Set the value from a double.

    #ifdef TIXML_USE_STL
	/// STL std::string form.
	void SetName( const std::string& _name )	{ name = _name; }	
	/// STL std::string form.	
	void SetValue( const std::string& _value )	{ value = _value; }
	#endif

	/// Get the next sibling attribute in the DOM. Returns null at end.
	const TiXmlAttribute* Next() const;
	TiXmlAttribute* Next() {
		return const_cast< TiXmlAttribute* >( (const_cast< const TiXmlAttribute* >(this))->Next() ); 
	}

	/// Get the previous sibling attribute in the DOM. Returns null at beginning.
	const TiXmlAttribute* Previous() const;
	TiXmlAttribute* Previous() {
		return const_cast< TiXmlAttribute* >( (const_cast< const TiXmlAttribute* >(this))->Previous() ); 
	}

	bool operator==( const TiXmlAttribute& rhs ) const { return rhs.name == name; }
	bool operator<( const TiXmlAttribute& rhs )	 const { return name < rhs.name; }
	bool operator>( const TiXmlAttribute& rhs )  const { return name > rhs.name; }

	/*	Attribute parsing starts: first letter of the name
						 returns: the next char after the value end quote
	*/
	virtual const char* Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding );

	// Prints this Attribute to a FILE stream.
	virtual void Print( FILE* cfile, int depth ) const {
		Print( cfile, depth, 0 );
	}
	void Print( FILE* cfile, int depth, TIXML_STRING* str ) const;

	// [internal use]
	// Set the document pointer so the attribute can report errors.
	void SetDocument( TiXmlDocument* doc )	{ document = doc; }

private:
	TiXmlAttribute( const TiXmlAttribute& );				// not implemented.
	void operator=( const TiXmlAttribute& base );	// not allowed.

	TiXmlDocument*	document;	// A pointer back to a document, for error reporting.
	TIXML_STRING name;
	TIXML_STRING value;
	TiXmlAttribute*	prev;
	TiXmlAttribute*	next;
};


/*	A class used to manage a group of attributes.
	It is only used internally, both by the ELEMENT and the DECLARATION.
	
	The set can be changed transparent to the Element and Declaration
	classes that use it, but NOT transparent to the Attribute
	which has to implement a next() and previous() method. Which makes
	it a bit problematic and prevents the use of STL.

	This version is implemented with circular lists because:
		- I like circular lists
		- it demonstrates some independence from the (typical) doubly linked list.
*/
class TiXmlAttributeSet
{
public:
	TiXmlAttributeSet();
	~TiXmlAttributeSet();

	void Add( TiXmlAttribute* attribute );
	void Remove( TiXmlAttribute* attribute );

	const TiXmlAttribute* First()	const	{ return ( sentinel.next == &sentinel ) ? 0 : sentinel.next; }
	TiXmlAttribute* First()					{ return ( sentinel.next == &sentinel ) ? 0 : sentinel.next; }
	const TiXmlAttribute* Last() const		{ return ( sentinel.prev == &sentinel ) ? 0 : sentinel.prev; }
	TiXmlAttribute* Last()					{ return ( sentinel.prev == &sentinel ) ? 0 : sentinel.prev; }

	TiXmlAttribute*	Find( const char* _name ) const;
	TiXmlAttribute* FindOrCreate( const char* _name );

#	ifdef TIXML_USE_STL
	TiXmlAttribute*	Find( const std::string& _name ) const;
	TiXmlAttribute* FindOrCreate( const std::string& _name );
#	endif


private:
	//*ME:	Because of hidden/disabled copy-construktor in TiXmlAttribute (sentinel-element),
	//*ME:	this class must be also use a hidden/disabled copy-constructor !!!
	TiXmlAttributeSet( const TiXmlAttributeSet& );	// not allowed
	void operator=( const TiXmlAttributeSet& );	// not allowed (as TiXmlAttribute)

	TiXmlAttribute sentinel;
};


/** The element is a container class. It has a value, the element name,
	and can contain other elements, text, comments, and unknowns.
	Elements also contain an arbitrary number of attributes.
*/
class TiXmlElement : public TiXmlNode
{
public:
	/// Construct an element.
	TiXmlElement (const char * in_value);

	#ifdef TIXML_USE_STL
	/// std::string constructor.
	TiXmlElement( const std::string& _value );
	#endif

	TiXmlElement( const TiXmlElement& );

	TiXmlElement& operator=( const TiXmlElement& base );

	virtual ~TiXmlElement();

	/** Given an attribute name, Attribute() returns the value
		for the attribute of that name, or null if none exists.
	*/
	const char* Attribute( const char* name ) const;

	/** Given an attribute name, Attribute() returns the value
		for the attribute of that name, or null if none exists.
		If the attribute exists and can be converted to an integer,
		the integer value will be put in the return 'i', if 'i'
		is non-null.
	*/
	const char* Attribute( const char* name, int* i ) const;

	/** Given an attribute name, Attribute() returns the value
		for the attribute of that name, or null if none exists.
		If the attribute exists and can be converted to an double,
		the double value will be put in the return 'd', if 'd'
		is non-null.
	*/
	const char* Attribute( const char* name, double* d ) const;

	/** QueryIntAttribute examines the attribute - it is an alternative to the
		Attribute() method with richer error checking.
		If the attribute is an integer, it is stored in 'value' and 
		the call returns TIXML_SUCCESS. If it is not
		an integer, it returns TIXML_WRONG_TYPE. If the attribute
		does not exist, then TIXML_NO_ATTRIBUTE is returned.
	*/	
	int QueryIntAttribute( const char* name, int* _value ) const;
	/// QueryUnsignedAttribute examines the attribute - see QueryIntAttribute().
	int QueryUnsignedAttribute( const char* name, unsigned* _value ) const;
	/** QueryBoolAttribute examines the attribute - see QueryIntAttribute(). 
		Note that '1', 'true', or 'yes' are considered true, while '0', 'false'
		and 'no' are considered false.
	*/
	int QueryBoolAttribute( const char* name, bool* _value ) const;
	/// QueryDoubleAttribute examines the attribute - see QueryIntAttribute().
	int QueryDoubleAttribute( const char* name, double* _value ) const;
	/// QueryFloatAttribute examines the attribute - see QueryIntAttribute().
	int QueryFloatAttribute( const char* name, float* _value ) const {
		double d;
		int result = QueryDoubleAttribute( name, &d );
		if ( result == TIXML_SUCCESS ) {
			*_value = (float)d;
		}
		return result;
	}

    #ifdef TIXML_USE_STL
	/// QueryStringAttribute examines the attribute - see QueryIntAttribute().
	int QueryStringAttribute( const char* name, std::string* _value ) const {
		const char* cstr = Attribute( name );
		if ( cstr ) {
			*_value = std::string( cstr );
			return TIXML_SUCCESS;
		}
		return TIXML_NO_ATTRIBUTE;
	}

	/** Template form of the attribute query which will try to read the
		attribute into the specified type. Very easy, very powerful, but
		be careful to make sure to call this with the correct type.
		
		NOTE: This method doesn't work correctly for 'string' types that contain spaces.

		@return TIXML_SUCCESS, TIXML_WRONG_TYPE, or TIXML_NO_ATTRIBUTE
	*/
	template< typename T > int QueryValueAttribute( const std::string& name, T* outValue ) const
	{
		const TiXmlAttribute* node = attributeSet.Find( name );
		if ( !node )
			return TIXML_NO_ATTRIBUTE;

		std::stringstream sstream( node->ValueStr() );
		sstream >> *outValue;
		if ( !sstream.fail() )
			return TIXML_SUCCESS;
		return TIXML_WRONG_TYPE;
	}

	int QueryValueAttribute( const std::string& name, std::string* outValue ) const
	{
		const TiXmlAttribute* node = attributeSet.Find( name );
		if ( !node )
			return TIXML_NO_ATTRIBUTE;
		*outValue = node->ValueStr();
		return TIXML_SUCCESS;
	}
	#endif

	/** Sets an attribute of name to a given value. The attribute
		will be created if it does not exist, or changed if it does.
	*/
	void SetAttribute( const char* name, const char * _value );

    #ifdef TIXML_USE_STL
	const std::string* Attribute( const std::string& name ) const;
	const std::string* Attribute( const std::string& name, int* i ) const;
	const std::string* Attribute( const std::string& name, double* d ) const;
	int QueryIntAttribute( const std::string& name, int* _value ) const;
	int QueryDoubleAttribute( const std::string& name, double* _value ) const;

	/// STL std::string form.
	void SetAttribute( const std::string& name, const std::string& _value );
	///< STL std::string form.
	void SetAttribute( const std::string& name, int _value );
	///< STL std::string form.
	void SetDoubleAttribute( const std::string& name, double value );
	#endif

	/** Sets an attribute of name to a given value. The attribute
		will be created if it does not exist, or changed if it does.
	*/
	void SetAttribute( const char * name, int value );

	/** Sets an attribute of name to a given value. The attribute
		will be created if it does not exist, or changed if it does.
	*/
	void SetDoubleAttribute( const char * name, double value );

	/** Deletes an attribute with the given name.
	*/
	void RemoveAttribute( const char * name );
    #ifdef TIXML_USE_STL
	void RemoveAttribute( const std::string& name )	{	RemoveAttribute (name.c_str ());	}	///< STL std::string form.
	#endif

	const TiXmlAttribute* FirstAttribute() const	{ return attributeSet.First(); }		///< Access the first attribute in this element.
	TiXmlAttribute* FirstAttribute() 				{ return attributeSet.First(); }
	const TiXmlAttribute* LastAttribute()	const 	{ return attributeSet.Last(); }		///< Access the last attribute in this element.
	TiXmlAttribute* LastAttribute()					{ return attributeSet.Last(); }

	/** Convenience function for easy access to the text inside an element. Although easy
		and concise, GetText() is limited compared to getting the TiXmlText child
		and accessing it directly.
	
		If the first child of 'this' is a TiXmlText, the GetText()
		returns the character string of the Text node, else null is returned.

		This is a convenient method for getting the text of simple contained text:
		@verbatim
		<foo>This is text</foo>
		const char* str = fooElement->GetText();
		@endverbatim

		'str' will be a pointer to "This is text". 
		
		Note that this function can be misleading. If the element foo was created from
		this XML:
		@verbatim
		<foo><b>This is text</b></foo> 
		@endverbatim

		then the value of str would be null. The first child node isn't a text node, it is
		another element. From this XML:
		@verbatim
		<foo>This is <b>text</b></foo> 
		@endverbatim
		GetText() will return "This is ".

		WARNING: GetText() accesses a child node - don't become confused with the 
				 similarly named TiXmlHandle::Text() and TiXmlNode::ToText() which are 
				 safe type casts on the referenced node.
	*/
	const char* GetText() const;

	/// Creates a new Element and returns it - the returned element is a copy.
	virtual TiXmlNode* Clone() const;
	// Print the Element to a FILE stream.
	virtual void Print( FILE* cfile, int depth ) const;

	/*	Attribtue parsing starts: next char past '<'
						 returns: next char past '>'
	*/
	virtual const char* Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding );

	virtual const TiXmlElement*     ToElement()     const { return this; } ///< Cast to a more defined type. Will return null not of the requested type.
	virtual TiXmlElement*           ToElement()	          { return this; } ///< Cast to a more defined type. Will return null not of the requested type.

	/** Walk the XML tree visiting this node and all of its children. 
	*/
	virtual bool Accept( TiXmlVisitor* visitor ) const;

protected:

	void CopyTo( TiXmlElement* target ) const;
	void ClearThis();	// like clear, but initializes 'this' object as well

	// Used to be public [internal use]
	#ifdef TIXML_USE_STL
	virtual void StreamIn( std::istream * in, TIXML_STRING * tag );
	#endif
	/*	[internal use]
		Reads the "value" of the element -- another element, or text.
		This should terminate with the current end tag.
	*/
	const char* ReadValue( const char* in, TiXmlParsingData* prevData, TiXmlEncoding encoding );

private:
	TiXmlAttributeSet attributeSet;
};


/**	An XML comment.
*/
class TiXmlComment : public TiXmlNode
{
public:
	/// Constructs an empty comment.
	TiXmlComment() : TiXmlNode( TiXmlNode::TINYXML_COMMENT ) {}
	/// Construct a comment from text.
	TiXmlComment( const char* _value ) : TiXmlNode( TiXmlNode::TINYXML_COMMENT ) {
		SetValue( _value );
	}
	TiXmlComment( const TiXmlComment& );
	TiXmlComment& operator=( const TiXmlComment& base );

	virtual ~TiXmlComment()	{}

	/// Returns a copy of this Comment.
	virtual TiXmlNode* Clone() const;
	// Write this Comment to a FILE stream.
	virtual void Print( FILE* cfile, int depth ) const;

	/*	Attribtue parsing starts: at the ! of the !--
						 returns: next char past '>'
	*/
	virtual const char* Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding );

	virtual const TiXmlComment*  ToComment() const	{ return this; } ///< Cast to a more defined type. Will return null not of the requested type.
	virtual		  TiXmlComment*  ToComment()		{ return this; } ///< Cast to a more defined type. Will return null not of the requested type.

	/** Walk the XML tree visiting this node and all of its children. 
	*/
	virtual bool Accept( TiXmlVisitor* visitor ) const;

protected:
	void CopyTo( TiXmlComment* target ) const;

	// used to be public
	#ifdef TIXML_USE_STL
	virtual void StreamIn( std::istream * in, TIXML_STRING * tag );
	#endif
//	virtual void StreamOut( TIXML_OSTREAM * out ) const;

private:

};


/** XML text. A text node can have 2 ways to output the next. "normal" output 
	and CDATA. It will default to the mode it was parsed from the XML file and
	you generally want to leave it alone, but you can change the output mode with 
	SetCDATA() and query it with CDATA().
*/
class TiXmlText : public TiXmlNode
{
	friend class TiXmlElement;
public:
	/** Constructor for text element. By default, it is treated as 
		normal, encoded text. If you want it be output as a CDATA text
		element, set the parameter _cdata to 'true'
	*/
	TiXmlText (const char * initValue ) : TiXmlNode (TiXmlNode::TINYXML_TEXT)
	{
		SetValue( initValue );
		cdata = false;
	}
	virtual ~TiXmlText() {}

	#ifdef TIXML_USE_STL
	/// Constructor.
	TiXmlText( const std::string& initValue ) : TiXmlNode (TiXmlNode::TINYXML_TEXT)
	{
		SetValue( initValue );
		cdata = false;
	}
	#endif

	TiXmlText( const TiXmlText& copy ) : TiXmlNode( TiXmlNode::TINYXML_TEXT )	{ copy.CopyTo( this ); }
	TiXmlText& operator=( const TiXmlText& base )							 	{ base.CopyTo( this ); return *this; }

	// Write this text object to a FILE stream.
	virtual void Print( FILE* cfile, int depth ) const;

	/// Queries whether this represents text using a CDATA section.
	bool CDATA() const				{ return cdata; }
	/// Turns on or off a CDATA representation of text.
	void SetCDATA( bool _cdata )	{ cdata = _cdata; }

	virtual const char* Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding );

	virtual const TiXmlText* ToText() const { return this; } ///< Cast to a more defined type. Will return null not of the requested type.
	virtual TiXmlText*       ToText()       { return this; } ///< Cast to a more defined type. Will return null not of the requested type.

	/** Walk the XML tree visiting this node and all of its children. 
	*/
	virtual bool Accept( TiXmlVisitor* content ) const;

protected :
	///  [internal use] Creates a new Element and returns it.
	virtual TiXmlNode* Clone() const;
	void CopyTo( TiXmlText* target ) const;

	bool Blank() const;	// returns true if all white space and new lines
	// [internal use]
	#ifdef TIXML_USE_STL
	virtual void StreamIn( std::istream * in, TIXML_STRING * tag );
	#endif

private:
	bool cdata;			// true if this should be input and output as a CDATA style text element
};


/** In correct XML the declaration is the first entry in the file.
	@verbatim
		<?xml version="1.0" standalone="yes"?>
	@endverbatim

	TinyXml will happily read or write files without a declaration,
	however. There are 3 possible attributes to the declaration:
	version, encoding, and standalone.

	Note: In this version of the code, the attributes are
	handled as special cases, not generic attributes, simply
	because there can only be at most 3 and they are always the same.
*/
class TiXmlDeclaration : public TiXmlNode
{
public:
	/// Construct an empty declaration.
	TiXmlDeclaration()   : TiXmlNode( TiXmlNode::TINYXML_DECLARATION ) {}

#ifdef TIXML_USE_STL
	/// Constructor.
	TiXmlDeclaration(	const std::string& _version,
						const std::string& _encoding,
						const std::string& _standalone );
#endif

	/// Construct.
	TiXmlDeclaration(	const char* _version,
						const char* _encoding,
						const char* _standalone );

	TiXmlDeclaration( const TiXmlDeclaration& copy );
	TiXmlDeclaration& operator=( const TiXmlDeclaration& copy );

	virtual ~TiXmlDeclaration()	{}

	/// Version. Will return an empty string if none was found.
	const char *Version() const			{ return version.c_str (); }
	/// Encoding. Will return an empty string if none was found.
	const char *Encoding() const		{ return encoding.c_str (); }
	/// Is this a standalone document?
	const char *Standalone() const		{ return standalone.c_str (); }

	/// Creates a copy of this Declaration and returns it.
	virtual TiXmlNode* Clone() const;
	// Print this declaration to a FILE stream.
	virtual void Print( FILE* cfile, int depth, TIXML_STRING* str ) const;
	virtual void Print( FILE* cfile, int depth ) const {
		Print( cfile, depth, 0 );
	}

	virtual const char* Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding );

	virtual const TiXmlDeclaration* ToDeclaration() const { return this; } ///< Cast to a more defined type. Will return null not of the requested type.
	virtual TiXmlDeclaration*       ToDeclaration()       { return this; } ///< Cast to a more defined type. Will return null not of the requested type.

	/** Walk the XML tree visiting this node and all of its children. 
	*/
	virtual bool Accept( TiXmlVisitor* visitor ) const;

protected:
	void CopyTo( TiXmlDeclaration* target ) const;
	// used to be public
	#ifdef TIXML_USE_STL
	virtual void StreamIn( std::istream * in, TIXML_STRING * tag );
	#endif

private:

	TIXML_STRING version;
	TIXML_STRING encoding;
	TIXML_STRING standalone;
};


/** Any tag that tinyXml doesn't recognize is saved as an
	unknown. It is a tag of text, but should not be modified.
	It will be written back to the XML, unchanged, when the file
	is saved.

	DTD tags get thrown into TiXmlUnknowns.
*/
class TiXmlUnknown : public TiXmlNode
{
public:
	TiXmlUnknown() : TiXmlNode( TiXmlNode::TINYXML_UNKNOWN )	{}
	virtual ~TiXmlUnknown() {}

	TiXmlUnknown( const TiXmlUnknown& copy ) : TiXmlNode( TiXmlNode::TINYXML_UNKNOWN )		{ copy.CopyTo( this ); }
	TiXmlUnknown& operator=( const TiXmlUnknown& copy )										{ copy.CopyTo( this ); return *this; }

	/// Creates a copy of this Unknown and returns it.
	virtual TiXmlNode* Clone() const;
	// Print this Unknown to a FILE stream.
	virtual void Print( FILE* cfile, int depth ) const;

	virtual const char* Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding );

	virtual const TiXmlUnknown*     ToUnknown()     const	{ return this; } ///< Cast to a more defined type. Will return null not of the requested type.
	virtual TiXmlUnknown*           ToUnknown()				{ return this; } ///< Cast to a more defined type. Will return null not of the requested type.

	/** Walk the XML tree visiting this node and all of its children. 
	*/
	virtual bool Accept( TiXmlVisitor* content ) const;

protected:
	void CopyTo( TiXmlUnknown* target ) const;

	#ifdef TIXML_USE_STL
	virtual void StreamIn( std::istream * in, TIXML_STRING * tag );
	#endif

private:

};


/** Always the top level node. A document binds together all the
	XML pieces. It can be saved, loaded, and printed to the screen.
	The 'value' of a document node is the xml file name.
*/
class TiXmlDocument : public TiXmlNode
{
public:
	/// Create an empty document, that has no name.
	TiXmlDocument();
	/// Create a document with a name. The name of the document is also the filename of the xml.
	TiXmlDocument( const char * documentName );

	#ifdef TIXML_USE_STL
	/// Constructor.
	TiXmlDocument( const std::string& documentName );
	#endif

	TiXmlDocument( const TiXmlDocument& copy );
	TiXmlDocument& operator=( const TiXmlDocument& copy );

	virtual ~TiXmlDocument() {}

	/** Load a file using the current document value.
		Returns true if successful. Will delete any existing
		document data before loading.
	*/
	bool LoadFile( TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING );
	/// Save a file using the current document value. Returns true if successful.
	bool SaveFile() const;
	/// Load a file using the given filename. Returns true if successful.
	bool LoadFile( const char * filename, TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING );
	/// Save a file using the given filename. Returns true if successful.
	bool SaveFile( const char * filename ) const;
	/** Load a file using the given FILE*. Returns true if successful. Note that this method
		doesn't stream - the entire object pointed at by the FILE*
		will be interpreted as an XML file. TinyXML doesn't stream in XML from the current
		file location. Streaming may be added in the future.
	*/
	bool LoadFile( FILE*, TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING );
	/// Save a file using the given FILE*. Returns true if successful.
	bool SaveFile( FILE* ) const;

	#ifdef TIXML_USE_STL
	bool LoadFile( const std::string& filename, TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING )			///< STL std::string version.
	{
		return LoadFile( filename.c_str(), encoding );
	}
	bool SaveFile( const std::string& filename ) const		///< STL std::string version.
	{
		return SaveFile( filename.c_str() );
	}
	#endif

	/** Parse the given null terminated block of xml data. Passing in an encoding to this
		method (either TIXML_ENCODING_LEGACY or TIXML_ENCODING_UTF8 will force TinyXml
		to use that encoding, regardless of what TinyXml might otherwise try to detect.
	*/
	virtual const char* Parse( const char* p, TiXmlParsingData* data = 0, TiXmlEncoding encoding = TIXML_DEFAULT_ENCODING );

	/** Get the root element -- the only top level element -- of the document.
		In well formed XML, there should only be one. TinyXml is tolerant of
		multiple elements at the document level.
	*/
	const TiXmlElement* RootElement() const		{ return FirstChildElement(); }
	TiXmlElement* RootElement()					{ return FirstChildElement(); }

	/** If an error occurs, Error will be set to true. Also,
		- The ErrorId() will contain the integer identifier of the error (not generally useful)
		- The ErrorDesc() method will return the name of the error. (very useful)
		- The ErrorRow() and ErrorCol() will return the location of the error (if known)
	*/	
	bool Error() const						{ return error; }

	/// Contains a textual (english) description of the error if one occurs.
	const char * ErrorDesc() const	{ return errorDesc.c_str (); }

	/** Generally, you probably want the error string ( ErrorDesc() ). But if you
		prefer the ErrorId, this function will fetch it.
	*/
	int ErrorId()	const				{ return errorId; }

	/** Returns the location (if known) of the error. The first column is column 1, 
		and the first row is row 1. A value of 0 means the row and column wasn't applicable
		(memory errors, for example, have no row/column) or the parser lost the error. (An
		error in the error reporting, in that case.)

		@sa SetTabSize, Row, Column
	*/
	int ErrorRow() const	{ return errorLocation.row+1; }
	int ErrorCol() const	{ return errorLocation.col+1; }	///< The column where the error occured. See ErrorRow()

	/** SetTabSize() allows the error reporting functions (ErrorRow() and ErrorCol())
		to report the correct values for row and column. It does not change the output
		or input in any way.
		
		By calling this method, with a tab size
		greater than 0, the row and column of each node and attribute is stored
		when the file is loaded. Very useful for tracking the DOM back in to
		the source file.

		The tab size is required for calculating the location of nodes. If not
		set, the default of 4 is used. The tabsize is set per document. Setting
		the tabsize to 0 disables row/column tracking.

		Note that row and column tracking is not supported when using operator>>.

		The tab size needs to be enabled before the parse or load. Correct usage:
		@verbatim
		TiXmlDocument doc;
		doc.SetTabSize( 8 );
		doc.Load( "myfile.xml" );
		@endverbatim

		@sa Row, Column
	*/
	void SetTabSize( int _tabsize )		{ tabsize = _tabsize; }

	int TabSize() const	{ return tabsize; }

	/** If you have handled the error, it can be reset with this call. The error
		state is automatically cleared if you Parse a new XML block.
	*/
	void ClearError()						{	error = false; 
												errorId = 0; 
												errorDesc = ""; 
												errorLocation.row = errorLocation.col = 0; 
												//errorLocation.last = 0; 
											}

	/** Write the document to standard out using formatted printing ("pretty print"). */
	void Print() const						{ Print( stdout, 0 ); }

	/* Write the document to a string using formatted printing ("pretty print"). This
		will allocate a character array (new char[]) and return it as a pointer. The
		calling code pust call delete[] on the return char* to avoid a memory leak.
	*/
	//char* PrintToMemory() const; 

	/// Print this Document to a FILE stream.
	virtual void Print( FILE* cfile, int depth = 0 ) const;
	// [internal use]
	void SetError( int err, const char* errorLocation, TiXmlParsingData* prevData, TiXmlEncoding encoding );

	virtual const TiXmlDocument*    ToDocument()    const { return this; } ///< Cast to a more defined type. Will return null not of the requested type.
	virtual TiXmlDocument*          ToDocument()          { return this; } ///< Cast to a more defined type. Will return null not of the requested type.

	/** Walk the XML tree visiting this node and all of its children. 
	*/
	virtual bool Accept( TiXmlVisitor* content ) const;

protected :
	// [internal use]
	virtual TiXmlNode* Clone() const;
	#ifdef TIXML_USE_STL
	virtual void StreamIn( std::istream * in, TIXML_STRING * tag );
	#endif

private:
	void CopyTo( TiXmlDocument* target ) const;

	bool error;
	int  errorId;
	TIXML_STRING errorDesc;
	int tabsize;
	TiXmlCursor errorLocation;
	bool useMicrosoftBOM;		// the UTF-8 BOM were found when read. Note this, and try to write.
};


/**
	A TiXmlHandle is a class that wraps a node pointer with null checks; this is
	an incredibly useful thing. Note that TiXmlHandle is not part of the TinyXml
	DOM structure. It is a separate utility class.

	Take an example:
	@verbatim
	<Document>
		<Element attributeA = "valueA">
			<Child attributeB = "value1" />
			<Child attributeB = "value2" />
		</Element>
	<Document>
	@endverbatim

	Assuming you want the value of "attributeB" in the 2nd "Child" element, it's very 
	easy to write a *lot* of code that looks like:

	@verbatim
	TiXmlElement* root = document.FirstChildElement( "Document" );
	if ( root )
	{
		TiXmlElement* element = root->FirstChildElement( "Element" );
		if ( element )
		{
			TiXmlElement* child = element->FirstChildElement( "Child" );
			if ( child )
			{
				TiXmlElement* child2 = child->NextSiblingElement( "Child" );
				if ( child2 )
				{
					// Finally do something useful.
	@endverbatim

	And that doesn't even cover "else" cases. TiXmlHandle addresses the verbosity
	of such code. A TiXmlHandle checks for null	pointers so it is perfectly safe 
	and correct to use:

	@verbatim
	TiXmlHandle docHandle( &document );
	TiXmlElement* child2 = docHandle.FirstChild( "Document" ).FirstChild( "Element" ).Child( "Child", 1 ).ToElement();
	if ( child2 )
	{
		// do something useful
	@endverbatim

	Which is MUCH more concise and useful.

	It is also safe to copy handles - internally they are nothing more than node pointers.
	@verbatim
	TiXmlHandle handleCopy = handle;
	@endverbatim

	What they should not be used for is iteration:

	@verbatim
	int i=0; 
	while ( true )
	{
		TiXmlElement* child = docHandle.FirstChild( "Document" ).FirstChild( "Element" ).Child( "Child", i ).ToElement();
		if ( !child )
			break;
		// do something
		++i;
	}
	@endverbatim

	It seems reasonable, but it is in fact two embedded while loops. The Child method is 
	a linear walk to find the element, so this code would iterate much more than it needs 
	to. Instead, prefer:

	@verbatim
	TiXmlElement* child = docHandle.FirstChild( "Document" ).FirstChild( "Element" ).FirstChild( "Child" ).ToElement();

	for( child; child; child=child->NextSiblingElement() )
	{
		// do something
	}
	@endverbatim
*/
class TiXmlHandle
{
public:
	/// Create a handle from any node (at any depth of the tree.) This can be a null pointer.
	TiXmlHandle( TiXmlNode* _node )					{ this->node = _node; }
	/// Copy constructor
	TiXmlHandle( const TiXmlHandle& ref )			{ this->node = ref.node; }
	TiXmlHandle operator=( const TiXmlHandle& ref ) { if ( &ref != this ) this->node = ref.node; return *this; }

	/// Return a handle to the first child node.
	TiXmlHandle FirstChild() const;
	/// Return a handle to the first child node with the given name.
	TiXmlHandle FirstChild( const char * value ) const;
	/// Return a handle to the first child element.
	TiXmlHandle FirstChildElement() const;
	/// Return a handle to the first child element with the given name.
	TiXmlHandle FirstChildElement( const char * value ) const;

	/** Return a handle to the "index" child with the given name. 
		The first child is 0, the second 1, etc.
	*/
	TiXmlHandle Child( const char* value, int index ) const;
	/** Return a handle to the "index" child. 
		The first child is 0, the second 1, etc.
	*/
	TiXmlHandle Child( int index ) const;
	/** Return a handle to the "index" child element with the given name. 
		The first child element is 0, the second 1, etc. Note that only TiXmlElements
		are indexed: other types are not counted.
	*/
	TiXmlHandle ChildElement( const char* value, int index ) const;
	/** Return a handle to the "index" child element. 
		The first child element is 0, the second 1, etc. Note that only TiXmlElements
		are indexed: other types are not counted.
	*/
	TiXmlHandle ChildElement( int index ) const;

	#ifdef TIXML_USE_STL
	TiXmlHandle FirstChild( const std::string& _value ) const				{ return FirstChild( _value.c_str() ); }
	TiXmlHandle FirstChildElement( const std::string& _value ) const		{ return FirstChildElement( _value.c_str() ); }

	TiXmlHandle Child( const std::string& _value, int index ) const			{ return Child( _value.c_str(), index ); }
	TiXmlHandle ChildElement( const std::string& _value, int index ) const	{ return ChildElement( _value.c_str(), index ); }
	#endif

	/** Return the handle as a TiXmlNode. This may return null.
	*/
	TiXmlNode* ToNode() const			{ return node; } 
	/** Return the handle as a TiXmlElement. This may return null.
	*/
	TiXmlElement* ToElement() const		{ return ( ( node && node->ToElement() ) ? node->ToElement() : 0 ); }
	/**	Return the handle as a TiXmlText. This may return null.
	*/
	TiXmlText* ToText() const			{ return ( ( node && node->ToText() ) ? node->ToText() : 0 ); }
	/** Return the handle as a TiXmlUnknown. This may return null.
	*/
	TiXmlUnknown* ToUnknown() const		{ return ( ( node && node->ToUnknown() ) ? node->ToUnknown() : 0 ); }

	/** @deprecated use ToNode. 
		Return the handle as a TiXmlNode. This may return null.
	*/
	TiXmlNode* Node() const			{ return ToNode(); } 
	/** @deprecated use ToElement. 
		Return the handle as a TiXmlElement. This may return null.
	*/
	TiXmlElement* Element() const	{ return ToElement(); }
	/**	@deprecated use ToText()
		Return the handle as a TiXmlText. This may return null.
	*/
	TiXmlText* Text() const			{ return ToText(); }
	/** @deprecated use ToUnknown()
		Return the handle as a TiXmlUnknown. This may return null.
	*/
	TiXmlUnknown* Unknown() const	{ return ToUnknown(); }

private:
	TiXmlNode* node;
};


/** Print to memory functionality. The TiXmlPrinter is useful when you need to:

	-# Print to memory (especially in non-STL mode)
	-# Control formatting (line endings, etc.)

	When constructed, the TiXmlPrinter is in its default "pretty printing" mode.
	Before calling Accept() you can call methods to control the printing
	of the XML document. After TiXmlNode::Accept() is called, the printed document can
	be accessed via the CStr(), Str(), and Size() methods.

	TiXmlPrinter uses the Visitor API.
	@verbatim
	TiXmlPrinter printer;
	printer.SetIndent( "\t" );

	doc.Accept( &printer );
	fprintf( stdout, "%s", printer.CStr() );
	@endverbatim
*/
class TiXmlPrinter : public TiXmlVisitor
{
public:
	TiXmlPrinter() : depth( 0 ), simpleTextPrint( false ),
					 buffer(), indent( "    " ), lineBreak( "\n" ) {}

	virtual bool VisitEnter( const TiXmlDocument& doc );
	virtual bool VisitExit( const TiXmlDocument& doc );

	virtual bool VisitEnter( const TiXmlElement& element, const TiXmlAttribute* firstAttribute );
	virtual bool VisitExit( const TiXmlElement& element );

	virtual bool Visit( const TiXmlDeclaration& declaration );
	virtual bool Visit( const TiXmlText& text );
	virtual bool Visit( const TiXmlComment& comment );
	virtual bool Visit( const TiXmlUnknown& unknown );

	/** Set the indent characters for printing. By default 4 spaces
		but tab (\t) is also useful, or null/empty string for no indentation.
	*/
	void SetIndent( const char* _indent )			{ indent = _indent ? _indent : "" ; }
	/// Query the indention string.
	const char* Indent()							{ return indent.c_str(); }
	/** Set the line breaking string. By default set to newline (\n). 
		Some operating systems prefer other characters, or can be
		set to the null/empty string for no indenation.
	*/
	void SetLineBreak( const char* _lineBreak )		{ lineBreak = _lineBreak ? _lineBreak : ""; }
	/// Query the current line breaking string.
	const char* LineBreak()							{ return lineBreak.c_str(); }

	/** Switch over to "stream printing" which is the most dense formatting without 
		linebreaks. Common when the XML is needed for network transmission.
	*/
	void SetStreamPrinting()						{ indent = "";
													  lineBreak = "";
													}	
	/// Return the result.
	const char* CStr()								{ return buffer.c_str(); }
	/// Return the length of the result string.
	size_t Size()									{ return buffer.size(); }

	#ifdef TIXML_USE_STL
	/// Return the result.
	const std::string& Str()						{ return buffer; }
	#endif

private:
	void DoIndent()	{
		for( int i=0; i<depth; ++i )
			buffer += indent;
	}
	void DoLineBreak() {
		buffer += lineBreak;
	}

	int depth;
	bool simpleTextPrint;
	TIXML_STRING buffer;
	TIXML_STRING indent;
	TIXML_STRING lineBreak;
};


#ifdef _MSC_VER
#pragma warning( pop )
#endif

#endif
```

## ServerLibrary\Util\tinyXml\tinyxmlerror.cpp
```cpp
/*
www.sourceforge.net/projects/tinyxml
Original code (2.0 and earlier )copyright (c) 2000-2006 Lee Thomason (www.grinninglizard.com)

This software is provided 'as-is', without any express or implied 
warranty. In no event will the authors be held liable for any 
damages arising from the use of this software.

Permission is granted to anyone to use this software for any 
purpose, including commercial applications, and to alter it and 
redistribute it freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must
not claim that you wrote the original software. If you use this
software in a product, an acknowledgment in the product documentation
would be appreciated but is not required.

2. Altered source versions must be plainly marked as such, and
must not be misrepresented as being the original software.

3. This notice may not be removed or altered from any source
distribution.
*/
#include "stdafx.h"
#include "tinyxml.h"

// The goal of the seperate error file is to make the first
// step towards localization. tinyxml (currently) only supports
// english error messages, but the could now be translated.
//
// It also cleans up the code a bit.
//

const char* TiXmlBase::errorString[ TiXmlBase::TIXML_ERROR_STRING_COUNT ] =
{
	"No error",
	"Error",
	"Failed to open file",
	"Error parsing Element.",
	"Failed to read Element name",
	"Error reading Element value.",
	"Error reading Attributes.",
	"Error: empty tag.",
	"Error reading end tag.",
	"Error parsing Unknown.",
	"Error parsing Comment.",
	"Error parsing Declaration.",
	"Error document empty.",
	"Error null (0) or unexpected EOF found in input stream.",
	"Error parsing CDATA.",
	"Error when TiXmlDocument added to document, because TiXmlDocument can only be at the root.",
};
```

## ServerLibrary\Util\tinyXml\tinyxmlparser.cpp
```cpp
/*
www.sourceforge.net/projects/tinyxml
Original code by Lee Thomason (www.grinninglizard.com)

This software is provided 'as-is', without any express or implied 
warranty. In no event will the authors be held liable for any 
damages arising from the use of this software.

Permission is granted to anyone to use this software for any 
purpose, including commercial applications, and to alter it and 
redistribute it freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must 
not claim that you wrote the original software. If you use this
software in a product, an acknowledgment in the product documentation
would be appreciated but is not required.

2. Altered source versions must be plainly marked as such, and 
must not be misrepresented as being the original software.

3. This notice may not be removed or altered from any source 
distribution.
*/
#include "stdafx.h"
#include <ctype.h>
#include <stddef.h>

#include "tinyxml.h"

//#define DEBUG_PARSER
#if defined( DEBUG_PARSER )
#	if defined( DEBUG ) && defined( _MSC_VER )
#		include <windows.h>
#		define TIXML_LOG OutputDebugString
#	else
#		define TIXML_LOG printf
#	endif
#endif

// Note tha "PutString" hardcodes the same list. This
// is less flexible than it appears. Changing the entries
// or order will break putstring.	
TiXmlBase::Entity TiXmlBase::entity[ TiXmlBase::NUM_ENTITY ] = 
{
	{ "&amp;",  5, '&' },
	{ "&lt;",   4, '<' },
	{ "&gt;",   4, '>' },
	{ "&quot;", 6, '\"' },
	{ "&apos;", 6, '\'' }
};

// Bunch of unicode info at:
//		http://www.unicode.org/faq/utf_bom.html
// Including the basic of this table, which determines the #bytes in the
// sequence from the lead byte. 1 placed for invalid sequences --
// although the result will be junk, pass it through as much as possible.
// Beware of the non-characters in UTF-8:	
//				ef bb bf (Microsoft "lead bytes")
//				ef bf be
//				ef bf bf 

const unsigned char TIXML_UTF_LEAD_0 = 0xefU;
const unsigned char TIXML_UTF_LEAD_1 = 0xbbU;
const unsigned char TIXML_UTF_LEAD_2 = 0xbfU;

const int TiXmlBase::utf8ByteTable[256] = 
{
	//	0	1	2	3	4	5	6	7	8	9	a	b	c	d	e	f
		1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	// 0x00
		1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	// 0x10
		1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	// 0x20
		1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	// 0x30
		1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	// 0x40
		1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	// 0x50
		1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	// 0x60
		1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	// 0x70	End of ASCII range
		1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	// 0x80 0x80 to 0xc1 invalid
		1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	// 0x90 
		1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	// 0xa0 
		1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	// 0xb0 
		1,	1,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	// 0xc0 0xc2 to 0xdf 2 byte
		2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	// 0xd0
		3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	// 0xe0 0xe0 to 0xef 3 byte
		4,	4,	4,	4,	4,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1	// 0xf0 0xf0 to 0xf4 4 byte, 0xf5 and higher invalid
};


void TiXmlBase::ConvertUTF32ToUTF8( unsigned long input, char* output, int* length )
{
	const unsigned long BYTE_MASK = 0xBF;
	const unsigned long BYTE_MARK = 0x80;
	const unsigned long FIRST_BYTE_MARK[7] = { 0x00, 0x00, 0xC0, 0xE0, 0xF0, 0xF8, 0xFC };

	if (input < 0x80) 
		*length = 1;
	else if ( input < 0x800 )
		*length = 2;
	else if ( input < 0x10000 )
		*length = 3;
	else if ( input < 0x200000 )
		*length = 4;
	else
		{ *length = 0; return; }	// This code won't covert this correctly anyway.

	output += *length;

	// Scary scary fall throughs.
	switch (*length) 
	{
		case 4:
			--output; 
			*output = (char)((input | BYTE_MARK) & BYTE_MASK); 
			input >>= 6;
		case 3:
			--output; 
			*output = (char)((input | BYTE_MARK) & BYTE_MASK); 
			input >>= 6;
		case 2:
			--output; 
			*output = (char)((input | BYTE_MARK) & BYTE_MASK); 
			input >>= 6;
		case 1:
			--output; 
			*output = (char)(input | FIRST_BYTE_MARK[*length]);
	}
}


/*static*/ int TiXmlBase::IsAlpha( unsigned char anyByte, TiXmlEncoding /*encoding*/ )
{
	// This will only work for low-ascii, everything else is assumed to be a valid
	// letter. I'm not sure this is the best approach, but it is quite tricky trying
	// to figure out alhabetical vs. not across encoding. So take a very 
	// conservative approach.

//	if ( encoding == TIXML_ENCODING_UTF8 )
//	{
		if ( anyByte < 127 )
			return isalpha( anyByte );
		else
			return 1;	// What else to do? The unicode set is huge...get the english ones right.
//	}
//	else
//	{
//		return isalpha( anyByte );
//	}
}


/*static*/ int TiXmlBase::IsAlphaNum( unsigned char anyByte, TiXmlEncoding /*encoding*/ )
{
	// This will only work for low-ascii, everything else is assumed to be a valid
	// letter. I'm not sure this is the best approach, but it is quite tricky trying
	// to figure out alhabetical vs. not across encoding. So take a very 
	// conservative approach.

//	if ( encoding == TIXML_ENCODING_UTF8 )
//	{
		if ( anyByte < 127 )
			return isalnum( anyByte );
		else
			return 1;	// What else to do? The unicode set is huge...get the english ones right.
//	}
//	else
//	{
//		return isalnum( anyByte );
//	}
}


class TiXmlParsingData
{
	friend class TiXmlDocument;
  public:
	void Stamp( const char* now, TiXmlEncoding encoding );

	const TiXmlCursor& Cursor() const	{ return cursor; }

  private:
	// Only used by the document!
	TiXmlParsingData( const char* start, int _tabsize, int row, int col )
	{
		assert( start );
		stamp = start;
		tabsize = _tabsize;
		cursor.row = row;
		cursor.col = col;
	}

	TiXmlCursor		cursor;
	const char*		stamp;
	int				tabsize;
};


void TiXmlParsingData::Stamp( const char* now, TiXmlEncoding encoding )
{
	assert( now );

	// Do nothing if the tabsize is 0.
	if ( tabsize < 1 )
	{
		return;
	}

	// Get the current row, column.
	int row = cursor.row;
	int col = cursor.col;
	const char* p = stamp;
	assert( p );

	while ( p < now )
	{
		// Treat p as unsigned, so we have a happy compiler.
		const unsigned char* pU = (const unsigned char*)p;

		// Code contributed by Fletcher Dunn: (modified by lee)
		switch (*pU) {
			case 0:
				// We *should* never get here, but in case we do, don't
				// advance past the terminating null character, ever
				return;

			case '\r':
				// bump down to the next line
				++row;
				col = 0;				
				// Eat the character
				++p;

				// Check for \r\n sequence, and treat this as a single character
				if (*p == '\n') {
					++p;
				}
				break;

			case '\n':
				// bump down to the next line
				++row;
				col = 0;

				// Eat the character
				++p;

				// Check for \n\r sequence, and treat this as a single
				// character.  (Yes, this bizarre thing does occur still
				// on some arcane platforms...)
				if (*p == '\r') {
					++p;
				}
				break;

			case '\t':
				// Eat the character
				++p;

				// Skip to next tab stop
				col = (col / tabsize + 1) * tabsize;
				break;

			case TIXML_UTF_LEAD_0:
				if ( encoding == TIXML_ENCODING_UTF8 )
				{
					if ( *(p+1) && *(p+2) )
					{
						// In these cases, don't advance the column. These are
						// 0-width spaces.
						if ( *(pU+1)==TIXML_UTF_LEAD_1 && *(pU+2)==TIXML_UTF_LEAD_2 )
							p += 3;	
						else if ( *(pU+1)==0xbfU && *(pU+2)==0xbeU )
							p += 3;	
						else if ( *(pU+1)==0xbfU && *(pU+2)==0xbfU )
							p += 3;	
						else
							{ p +=3; ++col; }	// A normal character.
					}
				}
				else
				{
					++p;
					++col;
				}
				break;

			default:
				if ( encoding == TIXML_ENCODING_UTF8 )
				{
					// Eat the 1 to 4 byte utf8 character.
					int step = TiXmlBase::utf8ByteTable[*((const unsigned char*)p)];
					if ( step == 0 )
						step = 1;		// Error case from bad encoding, but handle gracefully.
					p += step;

					// Just advance one column, of course.
					++col;
				}
				else
				{
					++p;
					++col;
				}
				break;
		}
	}
	cursor.row = row;
	cursor.col = col;
	assert( cursor.row >= -1 );
	assert( cursor.col >= -1 );
	stamp = p;
	assert( stamp );
}


const char* TiXmlBase::SkipWhiteSpace( const char* p, TiXmlEncoding encoding )
{
	if ( !p || !*p )
	{
		return 0;
	}
	if ( encoding == TIXML_ENCODING_UTF8 )
	{
		while ( *p )
		{
			const unsigned char* pU = (const unsigned char*)p;
			
			// Skip the stupid Microsoft UTF-8 Byte order marks
			if (	*(pU+0)==TIXML_UTF_LEAD_0
				 && *(pU+1)==TIXML_UTF_LEAD_1 
				 && *(pU+2)==TIXML_UTF_LEAD_2 )
			{
				p += 3;
				continue;
			}
			else if(*(pU+0)==TIXML_UTF_LEAD_0
				 && *(pU+1)==0xbfU
				 && *(pU+2)==0xbeU )
			{
				p += 3;
				continue;
			}
			else if(*(pU+0)==TIXML_UTF_LEAD_0
				 && *(pU+1)==0xbfU
				 && *(pU+2)==0xbfU )
			{
				p += 3;
				continue;
			}

			if ( IsWhiteSpace( *p ) )		// Still using old rules for white space.
				++p;
			else
				break;
		}
	}
	else
	{
		while ( *p && IsWhiteSpace( *p ) )
			++p;
	}

	return p;
}

#ifdef TIXML_USE_STL
/*static*/ bool TiXmlBase::StreamWhiteSpace( std::istream * in, TIXML_STRING * tag )
{
	for( ;; )
	{
		if ( !in->good() ) return false;

		int c = in->peek();
		// At this scope, we can't get to a document. So fail silently.
		if ( !IsWhiteSpace( c ) || c <= 0 )
			return true;

		*tag += (char) in->get();
	}
}

/*static*/ bool TiXmlBase::StreamTo( std::istream * in, int character, TIXML_STRING * tag )
{
	//assert( character > 0 && character < 128 );	// else it won't work in utf-8
	while ( in->good() )
	{
		int c = in->peek();
		if ( c == character )
			return true;
		if ( c <= 0 )		// Silent failure: can't get document at this scope
			return false;

		in->get();
		*tag += (char) c;
	}
	return false;
}
#endif

// One of TinyXML's more performance demanding functions. Try to keep the memory overhead down. The
// "assign" optimization removes over 10% of the execution time.
//
const char* TiXmlBase::ReadName( const char* p, TIXML_STRING * name, TiXmlEncoding encoding )
{
	// Oddly, not supported on some comilers,
	//name->clear();
	// So use this:
	*name = "";
	assert( p );

	// Names start with letters or underscores.
	// Of course, in unicode, tinyxml has no idea what a letter *is*. The
	// algorithm is generous.
	//
	// After that, they can be letters, underscores, numbers,
	// hyphens, or colons. (Colons are valid ony for namespaces,
	// but tinyxml can't tell namespaces from names.)
	if (    p && *p 
		 && ( IsAlpha( (unsigned char) *p, encoding ) || *p == '_' ) )
	{
		const char* start = p;
		while(		p && *p
				&&	(		IsAlphaNum( (unsigned char ) *p, encoding ) 
						 || *p == '_'
						 || *p == '-'
						 || *p == '.'
						 || *p == ':' ) )
		{
			//(*name) += *p; // expensive
			++p;
		}
		if ( p-start > 0 ) {
			name->assign( start, p-start );
		}
		return p;
	}
	return 0;
}

const char* TiXmlBase::GetEntity( const char* p, char* value, int* length, TiXmlEncoding encoding )
{
	// Presume an entity, and pull it out.
    TIXML_STRING ent;
	int i;
	*length = 0;

	if ( *(p+1) && *(p+1) == '#' && *(p+2) )
	{
		unsigned long ucs = 0;
		ptrdiff_t delta = 0;
		unsigned mult = 1;

		if ( *(p+2) == 'x' )
		{
			// Hexadecimal.
			if ( !*(p+3) ) return 0;

			const char* q = p+3;
			q = strchr( q, ';' );

			if ( !q || !*q ) return 0;

			delta = q-p;
			--q;

			while ( *q != 'x' )
			{
				if ( *q >= '0' && *q <= '9' )
					ucs += mult * (*q - '0');
				else if ( *q >= 'a' && *q <= 'f' )
					ucs += mult * (*q - 'a' + 10);
				else if ( *q >= 'A' && *q <= 'F' )
					ucs += mult * (*q - 'A' + 10 );
				else 
					return 0;
				mult *= 16;
				--q;
			}
		}
		else
		{
			// Decimal.
			if ( !*(p+2) ) return 0;

			const char* q = p+2;
			q = strchr( q, ';' );

			if ( !q || !*q ) return 0;

			delta = q-p;
			--q;

			while ( *q != '#' )
			{
				if ( *q >= '0' && *q <= '9' )
					ucs += mult * (*q - '0');
				else 
					return 0;
				mult *= 10;
				--q;
			}
		}
		if ( encoding == TIXML_ENCODING_UTF8 )
		{
			// convert the UCS to UTF-8
			ConvertUTF32ToUTF8( ucs, value, length );
		}
		else
		{
			*value = (char)ucs;
			*length = 1;
		}
		return p + delta + 1;
	}

	// Now try to match it.
	for( i=0; i<NUM_ENTITY; ++i )
	{
		if ( strncmp( entity[i].str, p, entity[i].strLength ) == 0 )
		{
			assert( strlen( entity[i].str ) == entity[i].strLength );
			*value = entity[i].chr;
			*length = 1;
			return ( p + entity[i].strLength );
		}
	}

	// So it wasn't an entity, its unrecognized, or something like that.
	*value = *p;	// Don't put back the last one, since we return it!
	//*length = 1;	// Leave unrecognized entities - this doesn't really work.
					// Just writes strange XML.
	return p+1;
}


bool TiXmlBase::StringEqual( const char* p,
							 const char* tag,
							 bool ignoreCase,
							 TiXmlEncoding encoding )
{
	assert( p );
	assert( tag );
	if ( !p || !*p )
	{
		assert( 0 );
		return false;
	}

	const char* q = p;

	if ( ignoreCase )
	{
		while ( *q && *tag && ToLower( *q, encoding ) == ToLower( *tag, encoding ) )
		{
			++q;
			++tag;
		}

		if ( *tag == 0 )
			return true;
	}
	else
	{
		while ( *q && *tag && *q == *tag )
		{
			++q;
			++tag;
		}

		if ( *tag == 0 )		// Have we found the end of the tag, and everything equal?
			return true;
	}
	return false;
}

const char* TiXmlBase::ReadText(	const char* p, 
									TIXML_STRING * text, 
									bool trimWhiteSpace, 
									const char* endTag, 
									bool caseInsensitive,
									TiXmlEncoding encoding )
{
    *text = "";
	if (    !trimWhiteSpace			// certain tags always keep whitespace
		 || !condenseWhiteSpace )	// if true, whitespace is always kept
	{
		// Keep all the white space.
		while (	   p && *p
				&& !StringEqual( p, endTag, caseInsensitive, encoding )
			  )
		{
			int len;
			char cArr[4] = { 0, 0, 0, 0 };
			p = GetChar( p, cArr, &len, encoding );
			text->append( cArr, len );
		}
	}
	else
	{
		bool whitespace = false;

		// Remove leading white space:
		p = SkipWhiteSpace( p, encoding );
		while (	   p && *p
				&& !StringEqual( p, endTag, caseInsensitive, encoding ) )
		{
			if ( *p == '\r' || *p == '\n' )
			{
				whitespace = true;
				++p;
			}
			else if ( IsWhiteSpace( *p ) )
			{
				whitespace = true;
				++p;
			}
			else
			{
				// If we've found whitespace, add it before the
				// new character. Any whitespace just becomes a space.
				if ( whitespace )
				{
					(*text) += ' ';
					whitespace = false;
				}
				int len;
				char cArr[4] = { 0, 0, 0, 0 };
				p = GetChar( p, cArr, &len, encoding );
				if ( len == 1 )
					(*text) += cArr[0];	// more efficient
				else
					text->append( cArr, len );
			}
		}
	}
	if ( p && *p )
		p += strlen( endTag );
	return ( p && *p ) ? p : 0;
}

#ifdef TIXML_USE_STL

void TiXmlDocument::StreamIn( std::istream * in, TIXML_STRING * tag )
{
	// The basic issue with a document is that we don't know what we're
	// streaming. Read something presumed to be a tag (and hope), then
	// identify it, and call the appropriate stream method on the tag.
	//
	// This "pre-streaming" will never read the closing ">" so the
	// sub-tag can orient itself.

	if ( !StreamTo( in, '<', tag ) ) 
	{
		SetError( TIXML_ERROR_PARSING_EMPTY, 0, 0, TIXML_ENCODING_UNKNOWN );
		return;
	}

	while ( in->good() )
	{
		int tagIndex = (int) tag->length();
		while ( in->good() && in->peek() != '>' )
		{
			int c = in->get();
			if ( c <= 0 )
			{
				SetError( TIXML_ERROR_EMBEDDED_NULL, 0, 0, TIXML_ENCODING_UNKNOWN );
				break;
			}
			(*tag) += (char) c;
		}

		if ( in->good() )
		{
			// We now have something we presume to be a node of 
			// some sort. Identify it, and call the node to
			// continue streaming.
			TiXmlNode* node = Identify( tag->c_str() + tagIndex, TIXML_DEFAULT_ENCODING );

			if ( node )
			{
				node->StreamIn( in, tag );
				bool isElement = node->ToElement() != 0;
				delete node;
				node = 0;

				// If this is the root element, we're done. Parsing will be
				// done by the >> operator.
				if ( isElement )
				{
					return;
				}
			}
			else
			{
				SetError( TIXML_ERROR, 0, 0, TIXML_ENCODING_UNKNOWN );
				return;
			}
		}
	}
	// We should have returned sooner.
	SetError( TIXML_ERROR, 0, 0, TIXML_ENCODING_UNKNOWN );
}

#endif

const char* TiXmlDocument::Parse( const char* p, TiXmlParsingData* prevData, TiXmlEncoding encoding )
{
	ClearError();

	// Parse away, at the document level. Since a document
	// contains nothing but other tags, most of what happens
	// here is skipping white space.
	if ( !p || !*p )
	{
		SetError( TIXML_ERROR_DOCUMENT_EMPTY, 0, 0, TIXML_ENCODING_UNKNOWN );
		return 0;
	}

	// Note that, for a document, this needs to come
	// before the while space skip, so that parsing
	// starts from the pointer we are given.
	location.Clear();
	if ( prevData )
	{
		location.row = prevData->cursor.row;
		location.col = prevData->cursor.col;
	}
	else
	{
		location.row = 0;
		location.col = 0;
	}
	TiXmlParsingData data( p, TabSize(), location.row, location.col );
	location = data.Cursor();

	if ( encoding == TIXML_ENCODING_UNKNOWN )
	{
		// Check for the Microsoft UTF-8 lead bytes.
		const unsigned char* pU = (const unsigned char*)p;
		if (	*(pU+0) && *(pU+0) == TIXML_UTF_LEAD_0
			 && *(pU+1) && *(pU+1) == TIXML_UTF_LEAD_1
			 && *(pU+2) && *(pU+2) == TIXML_UTF_LEAD_2 )
		{
			encoding = TIXML_ENCODING_UTF8;
			useMicrosoftBOM = true;
		}
	}

    p = SkipWhiteSpace( p, encoding );
	if ( !p )
	{
		SetError( TIXML_ERROR_DOCUMENT_EMPTY, 0, 0, TIXML_ENCODING_UNKNOWN );
		return 0;
	}

	while ( p && *p )
	{
		TiXmlNode* node = Identify( p, encoding );
		if ( node )
		{
			p = node->Parse( p, &data, encoding );
			LinkEndChild( node );
		}
		else
		{
			break;
		}

		// Did we get encoding info?
		if (    encoding == TIXML_ENCODING_UNKNOWN
			 && node->ToDeclaration() )
		{
			TiXmlDeclaration* dec = node->ToDeclaration();
			const char* enc = dec->Encoding();
			assert( enc );

			if ( *enc == 0 )
				encoding = TIXML_ENCODING_UTF8;
			else if ( StringEqual( enc, "UTF-8", true, TIXML_ENCODING_UNKNOWN ) )
				encoding = TIXML_ENCODING_UTF8;
			else if ( StringEqual( enc, "UTF8", true, TIXML_ENCODING_UNKNOWN ) )
				encoding = TIXML_ENCODING_UTF8;	// incorrect, but be nice
			else 
				encoding = TIXML_ENCODING_LEGACY;
		}

		p = SkipWhiteSpace( p, encoding );
	}

	// Was this empty?
	if ( !firstChild ) {
		SetError( TIXML_ERROR_DOCUMENT_EMPTY, 0, 0, encoding );
		return 0;
	}

	// All is well.
	return p;
}

void TiXmlDocument::SetError( int err, const char* pError, TiXmlParsingData* data, TiXmlEncoding encoding )
{	
	// The first error in a chain is more accurate - don't set again!
	if ( error )
		return;

	assert( err > 0 && err < TIXML_ERROR_STRING_COUNT );
	error   = true;
	errorId = err;
	errorDesc = errorString[ errorId ];

	errorLocation.Clear();
	if ( pError && data )
	{
		data->Stamp( pError, encoding );
		errorLocation = data->Cursor();
	}
}


TiXmlNode* TiXmlNode::Identify( const char* p, TiXmlEncoding encoding )
{
	TiXmlNode* returnNode = 0;

	p = SkipWhiteSpace( p, encoding );
	if( !p || !*p || *p != '<' )
	{
		return 0;
	}

	p = SkipWhiteSpace( p, encoding );

	if ( !p || !*p )
	{
		return 0;
	}

	// What is this thing? 
	// - Elements start with a letter or underscore, but xml is reserved.
	// - Comments: <!--
	// - Decleration: <?xml
	// - Everthing else is unknown to tinyxml.
	//

	const char* xmlHeader = { "<?xml" };
	const char* commentHeader = { "<!--" };
	const char* dtdHeader = { "<!" };
	const char* cdataHeader = { "<![CDATA[" };

	if ( StringEqual( p, xmlHeader, true, encoding ) )
	{
		#ifdef DEBUG_PARSER
			TIXML_LOG( "XML parsing Declaration\n" );
		#endif
		returnNode = new TiXmlDeclaration();
	}
	else if ( StringEqual( p, commentHeader, false, encoding ) )
	{
		#ifdef DEBUG_PARSER
			TIXML_LOG( "XML parsing Comment\n" );
		#endif
		returnNode = new TiXmlComment();
	}
	else if ( StringEqual( p, cdataHeader, false, encoding ) )
	{
		#ifdef DEBUG_PARSER
			TIXML_LOG( "XML parsing CDATA\n" );
		#endif
		TiXmlText* text = new TiXmlText( "" );
		text->SetCDATA( true );
		returnNode = text;
	}
	else if ( StringEqual( p, dtdHeader, false, encoding ) )
	{
		#ifdef DEBUG_PARSER
			TIXML_LOG( "XML parsing Unknown(1)\n" );
		#endif
		returnNode = new TiXmlUnknown();
	}
	else if (    IsAlpha( *(p+1), encoding )
			  || *(p+1) == '_' )
	{
		#ifdef DEBUG_PARSER
			TIXML_LOG( "XML parsing Element\n" );
		#endif
		returnNode = new TiXmlElement( "" );
	}
	else
	{
		#ifdef DEBUG_PARSER
			TIXML_LOG( "XML parsing Unknown(2)\n" );
		#endif
		returnNode = new TiXmlUnknown();
	}

	if ( returnNode )
	{
		// Set the parent, so it can report errors
		returnNode->parent = this;
	}
	return returnNode;
}

#ifdef TIXML_USE_STL

void TiXmlElement::StreamIn (std::istream * in, TIXML_STRING * tag)
{
	// We're called with some amount of pre-parsing. That is, some of "this"
	// element is in "tag". Go ahead and stream to the closing ">"
	while( in->good() )
	{
		int c = in->get();
		if ( c <= 0 )
		{
			TiXmlDocument* document = GetDocument();
			if ( document )
				document->SetError( TIXML_ERROR_EMBEDDED_NULL, 0, 0, TIXML_ENCODING_UNKNOWN );
			return;
		}
		(*tag) += (char) c ;
		
		if ( c == '>' )
			break;
	}

	if ( tag->length() < 3 ) return;

	// Okay...if we are a "/>" tag, then we're done. We've read a complete tag.
	// If not, identify and stream.

	if (    tag->at( tag->length() - 1 ) == '>' 
		 && tag->at( tag->length() - 2 ) == '/' )
	{
		// All good!
		return;
	}
	else if ( tag->at( tag->length() - 1 ) == '>' )
	{
		// There is more. Could be:
		//		text
		//		cdata text (which looks like another node)
		//		closing tag
		//		another node.
		for ( ;; )
		{
			StreamWhiteSpace( in, tag );

			// Do we have text?
			if ( in->good() && in->peek() != '<' ) 
			{
				// Yep, text.
				TiXmlText text( "" );
				text.StreamIn( in, tag );

				// What follows text is a closing tag or another node.
				// Go around again and figure it out.
				continue;
			}

			// We now have either a closing tag...or another node.
			// We should be at a "<", regardless.
			if ( !in->good() ) return;
			assert( in->peek() == '<' );
			int tagIndex = (int) tag->length();

			bool closingTag = false;
			bool firstCharFound = false;

			for( ;; )
			{
				if ( !in->good() )
					return;

				int c = in->peek();
				if ( c <= 0 )
				{
					TiXmlDocument* document = GetDocument();
					if ( document )
						document->SetError( TIXML_ERROR_EMBEDDED_NULL, 0, 0, TIXML_ENCODING_UNKNOWN );
					return;
				}
				
				if ( c == '>' )
					break;

				*tag += (char) c;
				in->get();

				// Early out if we find the CDATA id.
				if ( c == '[' && tag->size() >= 9 )
				{
					size_t len = tag->size();
					const char* start = tag->c_str() + len - 9;
					if ( strcmp( start, "<![CDATA[" ) == 0 ) {
						assert( !closingTag );
						break;
					}
				}

				if ( !firstCharFound && c != '<' && !IsWhiteSpace( c ) )
				{
					firstCharFound = true;
					if ( c == '/' )
						closingTag = true;
				}
			}
			// If it was a closing tag, then read in the closing '>' to clean up the input stream.
			// If it was not, the streaming will be done by the tag.
			if ( closingTag )
			{
				if ( !in->good() )
					return;

				int c = in->get();
				if ( c <= 0 )
				{
					TiXmlDocument* document = GetDocument();
					if ( document )
						document->SetError( TIXML_ERROR_EMBEDDED_NULL, 0, 0, TIXML_ENCODING_UNKNOWN );
					return;
				}
				assert( c == '>' );
				*tag += (char) c;

				// We are done, once we've found our closing tag.
				return;
			}
			else
			{
				// If not a closing tag, id it, and stream.
				const char* tagloc = tag->c_str() + tagIndex;
				TiXmlNode* node = Identify( tagloc, TIXML_DEFAULT_ENCODING );
				if ( !node )
					return;
				node->StreamIn( in, tag );
				delete node;
				node = 0;

				// No return: go around from the beginning: text, closing tag, or node.
			}
		}
	}
}
#endif

const char* TiXmlElement::Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding )
{
	p = SkipWhiteSpace( p, encoding );
	TiXmlDocument* document = GetDocument();

	if ( !p || !*p )
	{
		if ( document ) document->SetError( TIXML_ERROR_PARSING_ELEMENT, 0, 0, encoding );
		return 0;
	}

	if ( data )
	{
		data->Stamp( p, encoding );
		location = data->Cursor();
	}

	if ( *p != '<' )
	{
		if ( document ) document->SetError( TIXML_ERROR_PARSING_ELEMENT, p, data, encoding );
		return 0;
	}

	p = SkipWhiteSpace( p+1, encoding );

	// Read the name.
	const char* pErr = p;

    p = ReadName( p, &value, encoding );
	if ( !p || !*p )
	{
		if ( document )	document->SetError( TIXML_ERROR_FAILED_TO_READ_ELEMENT_NAME, pErr, data, encoding );
		return 0;
	}

    TIXML_STRING endTag ("</");
	endTag += value;

	// Check for and read attributes. Also look for an empty
	// tag or an end tag.
	while ( p && *p )
	{
		pErr = p;
		p = SkipWhiteSpace( p, encoding );
		if ( !p || !*p )
		{
			if ( document ) document->SetError( TIXML_ERROR_READING_ATTRIBUTES, pErr, data, encoding );
			return 0;
		}
		if ( *p == '/' )
		{
			++p;
			// Empty tag.
			if ( *p  != '>' )
			{
				if ( document ) document->SetError( TIXML_ERROR_PARSING_EMPTY, p, data, encoding );		
				return 0;
			}
			return (p+1);
		}
		else if ( *p == '>' )
		{
			// Done with attributes (if there were any.)
			// Read the value -- which can include other
			// elements -- read the end tag, and return.
			++p;
			p = ReadValue( p, data, encoding );		// Note this is an Element method, and will set the error if one happens.
			if ( !p || !*p ) {
				// We were looking for the end tag, but found nothing.
				// Fix for [ 1663758 ] Failure to report error on bad XML
				if ( document ) document->SetError( TIXML_ERROR_READING_END_TAG, p, data, encoding );
				return 0;
			}

			// We should find the end tag now
			// note that:
			// </foo > and
			// </foo> 
			// are both valid end tags.
			if ( StringEqual( p, endTag.c_str(), false, encoding ) )
			{
				p += endTag.length();
				p = SkipWhiteSpace( p, encoding );
				if ( p && *p && *p == '>' ) {
					++p;
					return p;
				}
				if ( document ) document->SetError( TIXML_ERROR_READING_END_TAG, p, data, encoding );
				return 0;
			}
			else
			{
				if ( document ) document->SetError( TIXML_ERROR_READING_END_TAG, p, data, encoding );
				return 0;
			}
		}
		else
		{
			// Try to read an attribute:
			TiXmlAttribute* attrib = new TiXmlAttribute();
			if ( !attrib )
			{
				return 0;
			}

			attrib->SetDocument( document );
			pErr = p;
			p = attrib->Parse( p, data, encoding );

			if ( !p || !*p )
			{
				if ( document ) document->SetError( TIXML_ERROR_PARSING_ELEMENT, pErr, data, encoding );
				delete attrib;
				return 0;
			}

			// Handle the strange case of double attributes:
			#ifdef TIXML_USE_STL
			TiXmlAttribute* node = attributeSet.Find( attrib->NameTStr() );
			#else
			TiXmlAttribute* node = attributeSet.Find( attrib->Name() );
			#endif
			if ( node )
			{
				if ( document ) document->SetError( TIXML_ERROR_PARSING_ELEMENT, pErr, data, encoding );
				delete attrib;
				return 0;
			}

			attributeSet.Add( attrib );
		}
	}
	return p;
}


const char* TiXmlElement::ReadValue( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding )
{
	TiXmlDocument* document = GetDocument();

	// Read in text and elements in any order.
	const char* pWithWhiteSpace = p;
	p = SkipWhiteSpace( p, encoding );

	while ( p && *p )
	{
		if ( *p != '<' )
		{
			// Take what we have, make a text element.
			TiXmlText* textNode = new TiXmlText( "" );

			if ( !textNode )
			{
			    return 0;
			}

			if ( TiXmlBase::IsWhiteSpaceCondensed() )
			{
				p = textNode->Parse( p, data, encoding );
			}
			else
			{
				// Special case: we want to keep the white space
				// so that leading spaces aren't removed.
				p = textNode->Parse( pWithWhiteSpace, data, encoding );
			}

			if ( !textNode->Blank() )
				LinkEndChild( textNode );
			else
				delete textNode;
		} 
		else 
		{
			// We hit a '<'
			// Have we hit a new element or an end tag? This could also be
			// a TiXmlText in the "CDATA" style.
			if ( StringEqual( p, "</", false, encoding ) )
			{
				return p;
			}
			else
			{
				TiXmlNode* node = Identify( p, encoding );
				if ( node )
				{
					p = node->Parse( p, data, encoding );
					LinkEndChild( node );
				}				
				else
				{
					return 0;
				}
			}
		}
		pWithWhiteSpace = p;
		p = SkipWhiteSpace( p, encoding );
	}

	if ( !p )
	{
		if ( document ) document->SetError( TIXML_ERROR_READING_ELEMENT_VALUE, 0, 0, encoding );
	}	
	return p;
}


#ifdef TIXML_USE_STL
void TiXmlUnknown::StreamIn( std::istream * in, TIXML_STRING * tag )
{
	while ( in->good() )
	{
		int c = in->get();	
		if ( c <= 0 )
		{
			TiXmlDocument* document = GetDocument();
			if ( document )
				document->SetError( TIXML_ERROR_EMBEDDED_NULL, 0, 0, TIXML_ENCODING_UNKNOWN );
			return;
		}
		(*tag) += (char) c;

		if ( c == '>' )
		{
			// All is well.
			return;		
		}
	}
}
#endif


const char* TiXmlUnknown::Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding )
{
	TiXmlDocument* document = GetDocument();
	p = SkipWhiteSpace( p, encoding );

	if ( data )
	{
		data->Stamp( p, encoding );
		location = data->Cursor();
	}
	if ( !p || !*p || *p != '<' )
	{
		if ( document ) document->SetError( TIXML_ERROR_PARSING_UNKNOWN, p, data, encoding );
		return 0;
	}
	++p;
    value = "";

	while ( p && *p && *p != '>' )
	{
		value += *p;
		++p;
	}

	if ( !p )
	{
		if ( document )	
			document->SetError( TIXML_ERROR_PARSING_UNKNOWN, 0, 0, encoding );
	}
	if ( p && *p == '>' )
		return p+1;
	return p;
}

#ifdef TIXML_USE_STL
void TiXmlComment::StreamIn( std::istream * in, TIXML_STRING * tag )
{
	while ( in->good() )
	{
		int c = in->get();	
		if ( c <= 0 )
		{
			TiXmlDocument* document = GetDocument();
			if ( document )
				document->SetError( TIXML_ERROR_EMBEDDED_NULL, 0, 0, TIXML_ENCODING_UNKNOWN );
			return;
		}

		(*tag) += (char) c;

		if ( c == '>' 
			 && tag->at( tag->length() - 2 ) == '-'
			 && tag->at( tag->length() - 3 ) == '-' )
		{
			// All is well.
			return;		
		}
	}
}
#endif


const char* TiXmlComment::Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding )
{
	TiXmlDocument* document = GetDocument();
	value = "";

	p = SkipWhiteSpace( p, encoding );

	if ( data )
	{
		data->Stamp( p, encoding );
		location = data->Cursor();
	}
	const char* startTag = "<!--";
	const char* endTag   = "-->";

	if ( !StringEqual( p, startTag, false, encoding ) )
	{
		if ( document )
			document->SetError( TIXML_ERROR_PARSING_COMMENT, p, data, encoding );
		return 0;
	}
	p += strlen( startTag );

	// [ 1475201 ] TinyXML parses entities in comments
	// Oops - ReadText doesn't work, because we don't want to parse the entities.
	// p = ReadText( p, &value, false, endTag, false, encoding );
	//
	// from the XML spec:
	/*
	 [Definition: Comments may appear anywhere in a document outside other markup; in addition, 
	              they may appear within the document type declaration at places allowed by the grammar. 
				  They are not part of the document's character data; an XML processor MAY, but need not, 
				  make it possible for an application to retrieve the text of comments. For compatibility, 
				  the string "--" (double-hyphen) MUST NOT occur within comments.] Parameter entity 
				  references MUST NOT be recognized within comments.

				  An example of a comment:

				  <!-- declarations for <head> & <body> -->
	*/

    value = "";
	// Keep all the white space.
	while (	p && *p && !StringEqual( p, endTag, false, encoding ) )
	{
		value.append( p, 1 );
		++p;
	}
	if ( p && *p ) 
		p += strlen( endTag );

	return p;
}


const char* TiXmlAttribute::Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding )
{
	p = SkipWhiteSpace( p, encoding );
	if ( !p || !*p ) return 0;

	if ( data )
	{
		data->Stamp( p, encoding );
		location = data->Cursor();
	}
	// Read the name, the '=' and the value.
	const char* pErr = p;
	p = ReadName( p, &name, encoding );
	if ( !p || !*p )
	{
		if ( document ) document->SetError( TIXML_ERROR_READING_ATTRIBUTES, pErr, data, encoding );
		return 0;
	}
	p = SkipWhiteSpace( p, encoding );
	if ( !p || !*p || *p != '=' )
	{
		if ( document ) document->SetError( TIXML_ERROR_READING_ATTRIBUTES, p, data, encoding );
		return 0;
	}

	++p;	// skip '='
	p = SkipWhiteSpace( p, encoding );
	if ( !p || !*p )
	{
		if ( document ) document->SetError( TIXML_ERROR_READING_ATTRIBUTES, p, data, encoding );
		return 0;
	}
	
	const char* end;
	const char SINGLE_QUOTE = '\'';
	const char DOUBLE_QUOTE = '\"';

	if ( *p == SINGLE_QUOTE )
	{
		++p;
		end = "\'";		// single quote in string
		p = ReadText( p, &value, false, end, false, encoding );
	}
	else if ( *p == DOUBLE_QUOTE )
	{
		++p;
		end = "\"";		// double quote in string
		p = ReadText( p, &value, false, end, false, encoding );
	}
	else
	{
		// All attribute values should be in single or double quotes.
		// But this is such a common error that the parser will try
		// its best, even without them.
		value = "";
		while (    p && *p											// existence
				&& !IsWhiteSpace( *p )								// whitespace
				&& *p != '/' && *p != '>' )							// tag end
		{
			if ( *p == SINGLE_QUOTE || *p == DOUBLE_QUOTE ) {
				// [ 1451649 ] Attribute values with trailing quotes not handled correctly
				// We did not have an opening quote but seem to have a 
				// closing one. Give up and throw an error.
				if ( document ) document->SetError( TIXML_ERROR_READING_ATTRIBUTES, p, data, encoding );
				return 0;
			}
			value += *p;
			++p;
		}
	}
	return p;
}

#ifdef TIXML_USE_STL
void TiXmlText::StreamIn( std::istream * in, TIXML_STRING * tag )
{
	while ( in->good() )
	{
		int c = in->peek();	
		if ( !cdata && (c == '<' ) ) 
		{
			return;
		}
		if ( c <= 0 )
		{
			TiXmlDocument* document = GetDocument();
			if ( document )
				document->SetError( TIXML_ERROR_EMBEDDED_NULL, 0, 0, TIXML_ENCODING_UNKNOWN );
			return;
		}

		(*tag) += (char) c;
		in->get();	// "commits" the peek made above

		if ( cdata && c == '>' && tag->size() >= 3 ) {
			size_t len = tag->size();
			if ( (*tag)[len-2] == ']' && (*tag)[len-3] == ']' ) {
				// terminator of cdata.
				return;
			}
		}    
	}
}
#endif

const char* TiXmlText::Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding encoding )
{
	value = "";
	TiXmlDocument* document = GetDocument();

	if ( data )
	{
		data->Stamp( p, encoding );
		location = data->Cursor();
	}

	const char* const startTag = "<![CDATA[";
	const char* const endTag   = "]]>";

	if ( cdata || StringEqual( p, startTag, false, encoding ) )
	{
		cdata = true;

		if ( !StringEqual( p, startTag, false, encoding ) )
		{
			if ( document )
				document->SetError( TIXML_ERROR_PARSING_CDATA, p, data, encoding );
			return 0;
		}
		p += strlen( startTag );

		// Keep all the white space, ignore the encoding, etc.
		while (	   p && *p
				&& !StringEqual( p, endTag, false, encoding )
			  )
		{
			value += *p;
			++p;
		}

		TIXML_STRING dummy; 
		p = ReadText( p, &dummy, false, endTag, false, encoding );
		return p;
	}
	else
	{
		bool ignoreWhite = true;

		const char* end = "<";
		p = ReadText( p, &value, ignoreWhite, end, false, encoding );
		if ( p && *p )
			return p-1;	// don't truncate the '<'
		return 0;
	}
}

#ifdef TIXML_USE_STL
void TiXmlDeclaration::StreamIn( std::istream * in, TIXML_STRING * tag )
{
	while ( in->good() )
	{
		int c = in->get();
		if ( c <= 0 )
		{
			TiXmlDocument* document = GetDocument();
			if ( document )
				document->SetError( TIXML_ERROR_EMBEDDED_NULL, 0, 0, TIXML_ENCODING_UNKNOWN );
			return;
		}
		(*tag) += (char) c;

		if ( c == '>' )
		{
			// All is well.
			return;
		}
	}
}
#endif

const char* TiXmlDeclaration::Parse( const char* p, TiXmlParsingData* data, TiXmlEncoding _encoding )
{
	p = SkipWhiteSpace( p, _encoding );
	// Find the beginning, find the end, and look for
	// the stuff in-between.
	TiXmlDocument* document = GetDocument();
	if ( !p || !*p || !StringEqual( p, "<?xml", true, _encoding ) )
	{
		if ( document ) document->SetError( TIXML_ERROR_PARSING_DECLARATION, 0, 0, _encoding );
		return 0;
	}
	if ( data )
	{
		data->Stamp( p, _encoding );
		location = data->Cursor();
	}
	p += 5;

	version = "";
	encoding = "";
	standalone = "";

	while ( p && *p )
	{
		if ( *p == '>' )
		{
			++p;
			return p;
		}

		p = SkipWhiteSpace( p, _encoding );
		if ( StringEqual( p, "version", true, _encoding ) )
		{
			TiXmlAttribute attrib;
			p = attrib.Parse( p, data, _encoding );		
			version = attrib.Value();
		}
		else if ( StringEqual( p, "encoding", true, _encoding ) )
		{
			TiXmlAttribute attrib;
			p = attrib.Parse( p, data, _encoding );		
			encoding = attrib.Value();
		}
		else if ( StringEqual( p, "standalone", true, _encoding ) )
		{
			TiXmlAttribute attrib;
			p = attrib.Parse( p, data, _encoding );		
			standalone = attrib.Value();
		}
		else
		{
			// Read over whatever it is.
			while( p && *p && *p != '>' && !IsWhiteSpace( *p ) )
				++p;
		}
	}
	return 0;
}

bool TiXmlText::Blank() const
{
	for ( unsigned i=0; i<value.length(); i++ )
		if ( !IsWhiteSpace( value[i] ) )
			return false;
	return true;
}
```

## ServerLibrary\Util\Type.h
```h
#pragma once
#include "stdafx.h"
#include <atomic>

// 타입 정의
typedef UINT64					object_t;
typedef UINT64					oid_t;
typedef int32_t					packet_size_t;

typedef std::time_t				tick_t;
typedef std::thread				thread_t;
typedef std::thread::id			threadId_t;

typedef std::recursive_mutex	lock_t;

typedef std::string				str_t;
typedef std::wstring			wstr_t;

// 크기 정의
#define SIZE_8				8
#define SIZE_64				64
#define SIZE_128			128
#define SIZE_256			256
#define SIZE_1024			1024
#define SIZE_4096			4096
#define SIZE_8192			8192

#define DB_PARAM_SIZE		8192
#define SOCKET_BUF_SIZE		1024 * 10

// 패킷을 type을 맞추기 위한 재정의 C# 기준
typedef unsigned char		Byte;
typedef char				Char;
typedef INT16				Int16;
typedef UINT16				UInt16;
typedef INT32				Int32;
typedef UINT32				UInt32;
typedef INT64				Int64;
typedef UINT64				UInt64;
typedef float				Float;

//for xml
typedef TiXmlDocument		xml_t;
typedef TiXmlElement		xmlNode_t;
typedef TiXmlHandle			xmlHandle_t;
```

## ServerLibrary\Util\Util.h
```h
#pragma once
#include <algorithm>


#define UNDEFINE_NAME		L"Undefine_Name"


#define snprintf(dst, format, ...)     _snprintf_s(dst.data(), dst.size(), _TRUNCATE, format, __VA_ARGS__)
#define snwprintf(dst, format, ...)    _snwprintf_s(dst.data(), dst.size(), _TRUNCATE, format, __VA_ARGS__)

//범위 보정 및 체크
#define fixInRange(minimum, x, maximum)     min(maximum, max(x, minimum)) 
#define isInRange(minimum, x, maximum)      (x == fixInRange(minimum, x, maximum)) ? true : false

//overflow 체크
inline bool isOverFlower_uint(unsigned int original, unsigned int add)
{
	unsigned int before = original;
	unsigned int after = original + add;
    if ((original & 0x80000000) != (after & 0x80000000)) {
        return false;
    }
    return true;
}


#define __W(x)              L##x
#define _W(x)               __W(x)


inline void StrConvA2T(CHAR *src, TCHAR *dest, size_t destLen) {
#ifdef  UNICODE                     
    if (destLen < 1) {
        return;
    }
    MultiByteToWideChar(CP_ACP, 0, src, -1, dest, (int) destLen - 1);
#endif
}

inline void StrConvT2A(TCHAR *src, CHAR *dest, size_t destLen) {
#ifdef  UNICODE                     
    if (destLen < 1) {
        return;
    }
	WideCharToMultiByte(CP_ACP, 0, src, -1, dest, (int) destLen, NULL, FALSE);
#endif
}

inline void StrConvA2W(CHAR *src, WCHAR *dest, size_t destLen) {
    if (destLen < 1) {
        return;
    }
	MultiByteToWideChar(CP_ACP, 0, src, -1, dest, (int) destLen - 1);
}
inline void StrConvW2A(WCHAR *src, CHAR *dest, size_t destLen) {
    if (destLen < 1) {
        return;
    }
	WideCharToMultiByte(CP_ACP, 0, src, -1, dest, (int) destLen, NULL, FALSE);
}

// delete object
#undef	SAFE_DELETE
#define SAFE_DELETE(obj)						\
{												\
	if ((obj)) delete(obj);		    			\
    (obj) = 0L;									\
}
// delete object array
#undef SAFE_DELETE_ARRAY
#define SAFE_DELETE_ARRAY(arr)					\
{												\
	if ((arr)) delete [] (arr);		    		\
    (arr) = 0L;									\
}

// delete gameObject
#define SAFE_FREE(obj)							\
{												\
	if ((obj)) obj->free();						\
    (obj) = 0L;									\
}

#define SAFE_RELEASE(obj)                       \
{                                               \
	if (obj) { obj.release(); }                 \
}
```

## ServerLibrary\x64\Debug\ServerLibrary.vcxproj.FileListAbsolute.txt
```txt

```
