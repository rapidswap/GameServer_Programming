using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DummyClient.Source.Network
{
    public interface PacketInterface
    {
        void encode();
        void decode(byte[] packet, ref int offset);

        Int64 type();
        MemoryStream getStream();
    }

    public class PacketData
    {
        protected MemoryStream packet_ = new MemoryStream();

        ~PacketData() 
        {
            packet_=null;
        }
    }
}
