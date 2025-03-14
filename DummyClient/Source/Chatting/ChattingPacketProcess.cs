﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DummyClient
{
    class ChattingPacketProcess : PacketProcess
    {
        ChattingContents contents_ = null;
        public ChattingPacketProcess()
        {
            contents_ = new ChattingContents();
        }

        public override void run(PacketInterface packet)
        {
            PacketType type = (PacketType)packet.type();
            switch (type)
            {
                case PacketType.E_S_ANS_NEW_USER_NOTIFY:
                    contents_.notifyNewUser(packet);
                    return;
                case PacketType.E_S_ANS_USER_LIST:
                    contents_.notifyUserList(packet);
                    return;
                case PacketType.E_S_ANS_CHATTING:
                    contents_.recvChatting(packet);
                    return;
                case PacketType.E_S_ANS_EXIT_USER:
                    contents_.C_REQ_CHAT_EXIT(packet);
                    return;
                case PacketType.E_S_ANS_EXIT:
                    return;
                
            }
            if (base.defaultRun(packet)==false)
            {
#if DEBUG
                MessageBox.Show("잘못된 패킷이 수신되었습니다 : "+type.ToString(), "error", MessageBoxButtons.OK);
                Application.Exit();
#endif
            }
        }
    }
}
