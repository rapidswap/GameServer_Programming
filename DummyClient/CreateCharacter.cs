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
            PK_C_REQ_CREATE_CHARACTER packet = new PK_C_REQ_CREATE_CHARACTER();
            packet.id_=Id_Text.Text;
            packet.name_=Name_Text.Text;
            packet.password_=Pw_Text.Text;
            packet.oidAccountId_=Convert.ToUInt64(Oid_Text.Text);
            packet.exp_=Convert.ToUInt64(Exp_Text.Text);
            packet.level_=Convert.ToUInt32(Lv_Text.Text);
            Program.programState_.sendPacket(packet);
        }

        private void Back_click(object sender, EventArgs e)
        {
            this.Close();
            Program.programState_.setState(PROGRAM_STATE.LOGIN, null, 0);
        }
    }
}
