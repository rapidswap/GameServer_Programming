# Project Structure
```
📦 root
    ├── 📂 ChattingServer
        ├── 📂 Server
            ├── 📄 ChattingProcess.cpp
            ├── 📄 ChattingProcess.h
            ├── 📄 User.h
            └── 📄 UserManager.h
        ├── 📂 x64
            └── 📂 Debug
                ├── 📂 ChattingServer.tlog
                    ├── 📄 ChattingServer.lastbuildstate
                ├── 📄 ChattingServer.exe.recipe
                ├── 📄 vc143.idb
        ├── 📄 ChattingServer.cpp
        ├── 📄 ChattingServer.vcxproj
        ├── 📄 ChattingServer.vcxproj.filters
        ├── 📄 config.xml
        ├── 📄 stdafx.cpp
        ├── 📄 stdafx.h
        └── 📄 targetver.h
    ├── 📂 DBAgent
        ├── 📂 Query
            ├── 📄 QI_DB_REQ_ID_PW.h
            └── 📄 QI_DB_REQ_LOAD_DATA.h
        ├── 📂 x64
            └── 📂 Debug
                ├── 📂 DBAgent.tlog
                    ├── 📄 DBAgent.lastbuildstate
                ├── 📄 DBAgent.exe.recipe
                ├── 📄 vc143.idb
        ├── 📄 DBAgent.vcxproj
        ├── 📄 DBAgent.vcxproj.filters
        ├── 📄 DBAgentProcess.cpp
        ├── 📄 DBAgentProcess.h
        ├── 📄 config.xml
        ├── 📄 main.cpp
        ├── 📄 stdafx.cpp
        ├── 📄 stdafx.h
        └── 📄 targetver.h
    ├── 📂 DummyClient
        ├── 📂 .vs
            ├── 📂 DummyClient
                ├── 📂 DesignTimeBuild
                    └── 📄 .dtbcache.v2
                ├── 📂 FileContentIndex
                    ├── 📄 0294584c-5a86-4ac0-83d3-b3ffdab10ce2.vsidx
                    ├── 📄 47e644de-1029-4b96-b610-b12b18ebbf9d.vsidx
                    ├── 📄 647aa712-fd7b-4373-b4a1-4c2d2d1bf084.vsidx
                    ├── 📄 82708b24-0d7f-41df-8de2-0f6d7e8f8f50.vsidx
                    ├── 📄 d9e3fecd-1970-43ff-8348-11d4dfbd1587.vsidx
                    └── 📄 f631d53b-74c4-4983-ae59-bb3fb5bc3e86.vsidx
                └── 📂 v17
                    ├── 📄 .futdcache.v2
                    ├── 📄 DocumentLayout.backup.json
                    └── 📄 DocumentLayout.json
            └── 📂 ProjectEvaluation
                ├── 📄 dummyclient.metadata.v9.bin
                ├── 📄 dummyclient.projects.v9.bin
                └── 📄 dummyclient.strings.v9.bin
        ├── 📂 Source
            ├── 📂 Chatting
                ├── 📄 ChatWnd.cs
                ├── 📄 ChattingContents.cs
                └── 📄 ChattingPacketProcess.cs
            ├── 📂 CreateCharacter
                ├── 📄 CreateCharacterContents.cs
                └── 📄 CreateCharacterProcess.cs
            ├── 📂 Login
                ├── 📄 LoginContents.cs
                └── 📄 LoginPacketProcess.cs
            ├── 📂 Network
                ├── 📄 Network.cs
                ├── 📄 Packet.cs
                ├── 📄 PacketObfuscation.cs
                └── 📄 PacketUtil.cs
            ├── 📂 PacketGen
                ├── 📄 PacketClass.cs
                ├── 📄 PacketFactory.cs
                └── 📄 PacketHeader.cs
            ├── 📄 ContentsProcess.cs
            ├── 📄 FormState.cs
            ├── 📄 PacketProcess.cs
            └── 📄 ProgramState.cs
        ├── 📂 bin
            └── 📂 Debug
                ├── 📂 net6.0-windows7.0
                    ├── 📄 DummyClient.deps.json
                    └── 📄 DummyClient.runtimeconfig.json
                ├── 📂 net8.0-windows
                    ├── 📄 DummyClient.deps.json
                    └── 📄 DummyClient.runtimeconfig.json
        ├── 📂 obj
            ├── 📂 Debug
                ├── 📂 net5.0-windows7.0
                    ├── 📄 .NETCoreApp,Version=v5.0.AssemblyAttributes.cs
                    ├── 📄 DummyClient.AssemblyInfo.cs
                    ├── 📄 DummyClient.GeneratedMSBuildEditorConfig.editorconfig
                    ├── 📄 DummyClient.GlobalUsings.g.cs
                    ├── 📄 DummyClient.designer.deps.json
                    └── 📄 DummyClient.designer.runtimeconfig.json
                ├── 📂 net6.0-windows7.0
                    ├── 📄 .NETCoreApp,Version=v6.0.AssemblyAttributes.cs
                    ├── 📄 DummyClient.AssemblyInfo.cs
                    ├── 📄 DummyClient.ChattingForm.resources
                    ├── 📄 DummyClient.DummyClient.resources
                    ├── 📄 DummyClient.GeneratedMSBuildEditorConfig.editorconfig
                    ├── 📄 DummyClient.GlobalUsings.g.cs
                    ├── 📄 DummyClient.LoginForm.resources
                    ├── 📄 DummyClient.csproj.BuildWithSkipAnalyzers
                    ├── 📄 DummyClient.csproj.FileListAbsolute.txt
                    ├── 📄 DummyClient.designer.deps.json
                    ├── 📄 DummyClient.designer.runtimeconfig.json
                    ├── 📄 DummyClient.sourcelink.json
                ├── 📂 net7.0-windows7.0
                    ├── 📄 .NETCoreApp,Version=v7.0.AssemblyAttributes.cs
                    ├── 📄 DummyClient.AssemblyInfo.cs
                    ├── 📄 DummyClient.GeneratedMSBuildEditorConfig.editorconfig
                    ├── 📄 DummyClient.GlobalUsings.g.cs
                ├── 📂 net8.0-windows
                    ├── 📄 .NETCoreApp,Version=v8.0.AssemblyAttributes.cs
                    ├── 📄 DummyClient.AssemblyInfo.cs
                    ├── 📄 DummyClient.ChattingForm.resources
                    ├── 📄 DummyClient.DummyClient.resources
                    ├── 📄 DummyClient.GeneratedMSBuildEditorConfig.editorconfig
                    ├── 📄 DummyClient.GlobalUsings.g.cs
                    ├── 📄 DummyClient.LoginForm.resources
                    ├── 📄 DummyClient.csproj.BuildWithSkipAnalyzers
                    ├── 📄 DummyClient.csproj.FileListAbsolute.txt
                    ├── 📄 DummyClient.designer.deps.json
                    ├── 📄 DummyClient.designer.runtimeconfig.json
                    ├── 📄 DummyClient.sourcelink.json
                └── 📂 net8.0-windows7.0
                    ├── 📄 .NETCoreApp,Version=v8.0.AssemblyAttributes.cs
                    ├── 📄 DummyClient.AssemblyInfo.cs
                    ├── 📄 DummyClient.GeneratedMSBuildEditorConfig.editorconfig
                    ├── 📄 DummyClient.GlobalUsings.g.cs
            ├── 📄 DummyClient.csproj.nuget.dgspec.json
            ├── 📄 DummyClient.csproj.nuget.g.props
            ├── 📄 DummyClient.csproj.nuget.g.targets
            ├── 📄 project.assets.json
        ├── 📄 ChattingForm.Designer.cs
        ├── 📄 ChattingForm.cs
        ├── 📄 ChattingForm.resx
        ├── 📄 CreateCharacter.Designer.cs
        ├── 📄 CreateCharacter.cs
        ├── 📄 CreateCharacter.resx
        ├── 📄 DummyClient.Designer.cs
        ├── 📄 DummyClient.cs
        ├── 📄 DummyClient.csproj
        ├── 📄 DummyClient.resx
        ├── 📄 DummyClient.sln
        ├── 📄 LoginForm.Designer.cs
        ├── 📄 LoginForm.cs
        ├── 📄 LoginForm.resx
        └── 📄 Program.cs
    ├── 📂 LoginServer
        ├── 📂 Server
            ├── 📄 LoginProcess.cpp
            └── 📄 LoginProcess.h
        ├── 📂 x64
            └── 📂 Debug
                ├── 📂 LoginServer.tlog
                    ├── 📄 LoginServer.lastbuildstate
                ├── 📄 LoginServer.exe.recipe
                ├── 📄 vc143.idb
        ├── 📄 LoginServer.cpp
        ├── 📄 LoginServer.vcxproj
        ├── 📄 LoginServer.vcxproj.filters
        ├── 📄 config.xml
        ├── 📄 stdafx.cpp
        ├── 📄 stdafx.h
        └── 📄 targetver.h
    ├── 📂 Output
        └── 📂 Debug
            └── 📂 ServerLibrary
                └── 📄 ServerLibrary.lib
    ├── 📂 ServerLibrary
        ├── 📂 .vs
            ├── 📂 ServerCore
                ├── 📂 FileContentIndex
                    ├── 📄 2a073c1e-5d59-4c80-804d-230d3380f70c.vsidx
                    ├── 📄 411536ae-1d07-499d-99c7-6defe778288c.vsidx
                    ├── 📄 468fe45b-4466-4daa-809e-d39f79006442.vsidx
                    ├── 📄 6926235d-7064-4811-afd4-ebecea21ddbc.vsidx
                    └── 📄 cb18be68-ee0c-4db2-83ce-92cbaee2b695.vsidx
                └── 📂 v17
                    ├── 📂 ipch
                        ├── 📂 AutoPCH
                            ├── 📂 13cff57c53a3a817
                                └── 📄 LOGINSERVER.ipch
                            ├── 📂 1831ea1c97aecbf1
                                └── 📄 STDAFX.ipch
                            ├── 📂 1f66473376955872
                                └── 📄 TARGETVER.ipch
                            ├── 📂 3ed8e15c6287f58b
                                └── 📄 VCTMP12656_716219.LOGINSERVER.00000000.ipch
                            ├── 📂 4f7d03b26c3ad8cf
                                └── 📄 DBAGENT.ipch
                            ├── 📂 50c82e6f02b17e0b
                                └── 📄 PCH.ipch
                            ├── 📂 6cd5da97a5415f9e
                                └── 📄 THREAD.ipch
                            ├── 📂 9ff8d571ab352520
                                └── 📄 STDAFX.ipch
                            ├── 📂 a28445fd5d6aca9e
                                └── 📄 TARGETVER.ipch
                            ├── 📂 a5ac833e010c4d3
                                └── 📄 CHATTINGSERVER.ipch
                            ├── 📂 c3624ec6416a2c87
                                └── 📄 MAIN.ipch
                            ├── 📂 c4e1198dabd67ed6
                                └── 📄 PCH.ipch
                            ├── 📂 cac4345029cb2c14
                                └── 📄 STDAFX.ipch
                            └── 📂 db7ab61d4abf8f0c
                                └── 📄 ADODATABASE.ipch
                        ├── 📄 32c9bc3a2434fd15.ipch
                        ├── 📄 86cde73365c2b22e.ipch
                        ├── 📄 98f831cb0b284446.ipch
                        ├── 📄 a5383a19e0b79c32.ipch
                        ├── 📄 c2b05d5ac50cc7f7.ipch
                        └── 📄 ea98cd5edadc7428.ipch
                    ├── 📄 DocumentLayout.backup.json
                    ├── 📄 DocumentLayout.json
                    └── 📄 fileList.bin
            └── 📂 ServerLibrary
                └── 📂 FileContentIndex
                    ├── 📄 0ff3eca7-6dab-4bb0-b290-725bb9a73781.vsidx
                    ├── 📄 1f3aefd9-d4c6-44d7-b3e5-56d3e676dc5e.vsidx
                    ├── 📄 85728970-e604-4803-980b-ff83972d688f.vsidx
                    ├── 📄 baa84d9a-9f38-43dd-93ac-3b22a962677e.vsidx
                    └── 📄 bf77c4b5-34dd-4b70-b50f-d25785de525a.vsidx
        ├── 📂 Contents
            ├── 📄 ContentsProcess.cpp
            └── 📄 ContentsProcess.h
        ├── 📂 Database
            ├── 📄 ADODatabase.cpp
            ├── 📄 ADODatabase.h
            ├── 📄 DBManager.cpp
            ├── 📄 DBManager.h
            ├── 📄 Database.h
            ├── 📄 Query.cpp
            ├── 📄 Query.h
            ├── 📄 QueryRecord.cpp
            ├── 📄 QueryRecord.h
            ├── 📄 QueryStatement.cpp
            └── 📄 QueryStatement.h
        ├── 📂 Net
            ├── 📂 IOCP
                ├── 📄 IOCPServer.cpp
                ├── 📄 IOCPServer.h
                ├── 📄 IOCPSession.cpp
                └── 📄 IOCPSession.h
            ├── 📂 Packet
                ├── 📄 Package.h
                ├── 📄 PacketAnalyzer.cpp
                ├── 📄 PacketAnalyzer.h
                ├── 📄 PacketClass.h
                ├── 📄 PacketFactory.h
                ├── 📄 PacketHeader.h
                ├── 📄 PacketObfuscation.cpp
                ├── 📄 PacketObfuscation.h
                ├── 📄 Stream.cpp
                └── 📄 Stream.h
            ├── 📂 Terminal
                ├── 📄 Terminal.cpp
                ├── 📄 Terminal.h
                ├── 📄 TerminalManager.cpp
                ├── 📄 TerminalManager.h
                ├── 📄 TerminalSession.cpp
                └── 📄 TerminalSession.h
            ├── 📄 Packet.h
            ├── 📄 PacketHeader.h
            ├── 📄 PacketManager.h
            ├── 📄 Server.cpp
            ├── 📄 Server.h
            ├── 📄 Session.cpp
            ├── 📄 Session.h
            ├── 📄 SessionManager.cpp
            ├── 📄 SessionManager.h
            ├── 📄 SessionMonitor.cpp
            ├── 📄 SessionMonitor.h
            ├── 📄 Stream.h
            └── 📄 Winsocket.h
        ├── 📂 ServerLibrary
            └── 📂 x64
                └── 📂 Debug
                    ├── 📂 ServerLibrary.tlog
                        ├── 📄 ServerLibrary.lastbuildstate
                        └── 📄 unsuccessfulbuild
                    ├── 📄 ServerLibrary.exe.recipe
                    ├── 📄 ServerLibrary.lib.recipe
                    ├── 📄 ServerLibrary.vcxproj.FileListAbsolute.txt
        ├── 📂 Util
            ├── 📂 csv_parser
                ├── 📄 csv_parser.cpp
                └── 📄 csv_parser.hpp
            ├── 📂 tinyXml
                ├── 📄 tinystr.cpp
                ├── 📄 tinystr.h
                ├── 📄 tinyxml.cpp
                ├── 📄 tinyxml.h
                ├── 📄 tinyxmlerror.cpp
                └── 📄 tinyxmlparser.cpp
            ├── 📄 Assert.cpp
            ├── 📄 Assert.h
            ├── 📄 Clock.cpp
            ├── 📄 Clock.h
            ├── 📄 Config.cpp
            ├── 📄 Config.h
            ├── 📄 GameObject.h
            ├── 📄 Lock.cpp
            ├── 📄 Lock.h
            ├── 📄 Logger.cpp
            ├── 📄 Logger.h
            ├── 📄 MemoryLeak.h
            ├── 📄 Memory_LowFragmentationHeap.h
            ├── 📄 Minidump.cpp
            ├── 📄 Minidump.h
            ├── 📄 Monitoring.h
            ├── 📄 ProgramValidation.h
            ├── 📄 Singleton.h
            ├── 📄 Table.h
            ├── 📄 Task.cpp
            ├── 📄 Task.h
            ├── 📄 Thread.cpp
            ├── 📄 Thread.h
            ├── 📄 ThreadJobQueue.h
            ├── 📄 Type.h
            └── 📄 Util.h
        ├── 📂 x64
            └── 📂 Debug
                ├── 📂 ServerLibrary.tlog
                    └── 📄 ServerLibrary.lastbuildstate
                ├── 📄 ServerLibrary.idb
                ├── 📄 ServerLibrary.lib.recipe
                ├── 📄 ServerLibrary.vcxproj.FileListAbsolute.txt
        ├── 📄 ServerCore.sln
        ├── 📄 ServerLibrary.h
        ├── 📄 ServerLibrary.vcxproj
        ├── 📄 ServerLibrary.vcxproj.filters
        ├── 📄 Shutdown.cpp
        ├── 📄 Shutdown.h
        ├── 📄 item.csv
        ├── 📄 stdafx.cpp
        ├── 📄 stdafx.h
        └── 📄 targetver.h
```