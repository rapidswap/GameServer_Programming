namespace DummyClient
{
    class ChattingContents:ContentsProcess
    {
        public void recvChatting(PacketInterface rowPacket)
        {
            PK_S_ANS_CHATTING packet=(PK_S_ANS_CHATTING)rowPacket;
            Program.programState_.putMessage(packet.name_+packet.text_);
        }

        public void notifyNewUser(PacketInterface rowPacket)
        {
            PK_S_ANS_NEW_USER_NOTIFY packet = (PK_S_ANS_NEW_USER_NOTIFY)rowPacket;
            Program.programState_.putMessage(packet.name_+"님이 입장하셨습니다.");
        }

        public void notifyUserList(PacketInterface rowPacket)
        {
            PK_S_ANS_USER_LIST packet = (PK_S_ANS_USER_LIST)rowPacket;
            if (packet.names_ == null || packet.names_.Count == 0)
            {
                Program.programState_.putMessage("현재 접속자가 없습니다.");
                return;
            }

            foreach (string userName in packet.names_)
            {
                Program.programState_.putMessage($"현재 접속중: [{userName}]");
            }
        }

        public void C_REQ_CHAT_EXIT(PacketInterface rowPacket)
        {
            MessageBox.Show("종료 됨", "확인", MessageBoxButtons.OK);
            PK_S_ANS_EXIT_USER packet =(PK_S_ANS_EXIT_USER)rowPacket;
            Program.programState_.putMessage(packet.name_+"님이 퇴장하셨습니다.");
        }
    }
}
