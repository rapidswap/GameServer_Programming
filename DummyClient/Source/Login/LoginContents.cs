using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DummyClient
{
    class LoginContents : ContentsProcess
    {
        public void S_ANS_ID_PW_FAIL(PacketInterface rowPacket)
        {
            MessageBox.Show("로그인 실패, 아이디와 패스워드를 확인해주세요.", "로그인", MessageBoxButtons.OK);
        }

        public void S_ANS_ID_PW_SUCCESS(PacketInterface rowPacket)
        {
            PK_S_ANS_ID_PW_SUCCESS packet = (PK_S_ANS_ID_PW_SUCCESS)rowPacket;

            Program.programState_.setState(PROGRAM_STATE.CHATTING, packet.ip_, packet.port_);
            Program.programState_.setName(packet.name_);

            PK_C_REQ_REGIST_CHATTING_NAME rPacket = new PK_C_REQ_REGIST_CHATTING_NAME();
            rPacket.name_ = packet.name_;
            Program.programState_.sendPacket(rPacket);
        }

        public void S_ANS_EXIT(PacketInterface rowPacket)
        {
            MessageBox.Show("종료 됨", "확인", MessageBoxButtons.OK);
        }

        public void I_DB_ANS_CREATE_USER(PacketInterface rowPacket)
        {
            MessageBox.Show("유저 생성을 성공하였습니다.", "확인", MessageBoxButtons.OK);
            Program.programState_.setState(PROGRAM_STATE.LOGIN, null, 0);
        }


        public void S_ANS_CREATE_CHARACTER_SUCCESS(PacketInterface rowPacket)
        {
            MessageBox.Show("캐릭터 생성을 성공하였습니다.", "확인", MessageBoxButtons.OK);
            Program.programState_.setState(PROGRAM_STATE.LOGIN, null, 0);
        }

        public void S_ANS_CREATE_CHARACTER_FAIL(PacketInterface rowPacket)
        {
            MessageBox.Show("캐릭터 생성을 실패하였습니다. 다른 이름을 사용하세요.", "확인", MessageBoxButtons.OK);
           
        }

        public void S_ANS_CREATE_FAIL(PacketInterface rowPacket)
        {
            MessageBox.Show("유저 생성을 실패하였습니다. 다른 아이디를 이용하세요.", "확인", MessageBoxButtons.OK);
        }

    }
}
