using System;
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
