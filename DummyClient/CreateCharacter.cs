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
    public partial class CreateCharacter : Form
    {
        public CreateCharacter()
        {
            InitializeComponent();
        }

        private void Create_click(object sender, EventArgs e)
        {
            PK_C_REQ_CREATE_CHARACTER_ID_PW packet = new PK_C_REQ_CREATE_CHARACTER_ID_PW();
            packet.id_=Id_Text.Text;
            packet.password_=Pw_Text.Text;
            packet.name_=Name_Text.Text;
            Program.programState_.sendPacket(packet);
        }

        private void Back_click(object sender, EventArgs e)
        {
            this.Close();
            Program.programState_.setState(PROGRAM_STATE.LOGIN, null, 0);
        }
    }
}
