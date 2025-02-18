using System;
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
                case PacketType.E_S_ANS_USER_EXIT_NOTIFY:
                    contents_.leaveUser(packet);
                    return;
                //case PacketType.E_S_ANS_EXIT:
                //    contents_.leaveUser(packet);  // 먼저 퇴장 처리
                //    if (Application.OpenForms["ChattingForm"] is ChattingForm chattingForm)
                //    {
                //        chattingForm.BeginInvoke(new Action(() => {
                //            chattingForm.Close();  // 채팅폼 닫기
                //            Application.Exit();    // 프로그램 종료
                //        }));
                //    }
                //    return;

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
