using System.Windows.Forms;

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