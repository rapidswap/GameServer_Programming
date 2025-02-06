using DummyClient.Source.Network;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DummyClient.Source
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
