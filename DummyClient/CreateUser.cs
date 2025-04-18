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
    public partial class CreateUser : Form
    {
        public CreateUser()
        {
            InitializeComponent();
        }

        private void Create_Click(object sender, EventArgs e)
        {
            PK_C_REQ_CREATE_USER packet = new PK_C_REQ_CREATE_USER();
            packet.id_=ID_Create.Text;
            packet.password_=PW_Create.Text;
            Program.programState_.sendPacket(packet);
        }

        private void Back_Click(object sender, EventArgs e)
        {
            this.Close();
            Program.programState_.setState(PROGRAM_STATE.LOGIN, null, 0);
        }

        private void ID_Click(object sender, EventArgs e)
        {

        }
    }
}
