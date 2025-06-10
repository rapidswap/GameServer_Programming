using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.IO;
using System.Net.Sockets;

namespace DummyClient
{
    public class PK_C_REQ_EXIT : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_C_REQ_EXIT; }
        Int64 type() { return (Int64)PacketType.E_C_REQ_EXIT; }
        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_S_ANS_EXIT : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_EXIT; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_EXIT; }
        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_I_NOTIFY_TERMINAL : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_NOTIFY_TERMINAL; }
        Int64 type() { return (Int64)PacketType.E_I_NOTIFY_TERMINAL; }
        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_C_NOTIFY_HEARTBEAT : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_C_NOTIFY_HEARTBEAT; }
        Int64 type() { return (Int64)PacketType.E_C_NOTIFY_HEARTBEAT; }
        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_C_REQ_ID_PW : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_C_REQ_ID_PW; }
        Int64 type() { return (Int64)PacketType.E_C_REQ_ID_PW; }
        public string id_;
        public string password_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, id_);
            PacketUtil.encode(packet_, password_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            id_ = PacketUtil.decodestring(packet, ref offset);
            password_ = PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_S_ANS_ID_PW_FAIL : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_ID_PW_FAIL; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_ID_PW_FAIL; }
        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_S_ANS_ID_PW_SUCCESS : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_ID_PW_SUCCESS; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_ID_PW_SUCCESS; }
        public string ip_;
        public UInt32 port_;
        public string name_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, ip_);
            PacketUtil.encode(packet_, port_);
            PacketUtil.encode(packet_, name_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            ip_ = PacketUtil.decodestring(packet, ref offset);
            port_ = PacketUtil.decodeUInt32(packet, ref offset);
            name_ = PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_I_DB_REQ_ID_PW : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_DB_REQ_ID_PW; }
        Int64 type() { return (Int64)PacketType.E_I_DB_REQ_ID_PW; }
        public UInt64 clientId_;
        public string id_;
        public string password_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, id_);
            PacketUtil.encode(packet_, password_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            id_ = PacketUtil.decodestring(packet, ref offset);
            password_ = PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_I_DB_ANS_ID_PW : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_DB_ANS_ID_PW; }
        Int64 type() { return (Int64)PacketType.E_I_DB_ANS_ID_PW; }
        public UInt64 clientId_;
        public UInt64 oidAccountId_;
        public Byte result_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, oidAccountId_);
            PacketUtil.encode(packet_, result_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            oidAccountId_ = PacketUtil.decodeUInt64(packet, ref offset);
            result_ = PacketUtil.decodeByte(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_I_CHTTING_NOTIFY_ID : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_CHTTING_NOTIFY_ID; }
        Int64 type() { return (Int64)PacketType.E_I_CHTTING_NOTIFY_ID; }
        public UInt64 clientId_;
        public UInt64 oidAccountId_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, oidAccountId_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            oidAccountId_ = PacketUtil.decodeUInt64(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_I_DB_REQ_LOAD_DATA : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_DB_REQ_LOAD_DATA; }
        Int64 type() { return (Int64)PacketType.E_I_DB_REQ_LOAD_DATA; }
        public UInt64 clientId_;
        public UInt64 oidAccountId_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, oidAccountId_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            oidAccountId_ = PacketUtil.decodeUInt64(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_I_DB_ANS_PARSE_DATA : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_DB_ANS_PARSE_DATA; }
        Int64 type() { return (Int64)PacketType.E_I_DB_ANS_PARSE_DATA; }
        public UInt64 clientId_;
        public string name_;
        public Byte result_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, name_);
            PacketUtil.encode(packet_, result_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            name_ = PacketUtil.decodestring(packet, ref offset);
            result_ = PacketUtil.decodeByte(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_I_LOGIN_NOTIFY_ID_LOADED : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_LOGIN_NOTIFY_ID_LOADED; }
        Int64 type() { return (Int64)PacketType.E_I_LOGIN_NOTIFY_ID_LOADED; }
        public UInt64 clientId_;
        public string name_;
        public Byte result_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, name_);
            PacketUtil.encode(packet_, result_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            name_ = PacketUtil.decodestring(packet, ref offset);
            result_ = PacketUtil.decodeByte(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_C_REQ_REGIST_CHATTING_NAME : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_C_REQ_REGIST_CHATTING_NAME; }
        Int64 type() { return (Int64)PacketType.E_C_REQ_REGIST_CHATTING_NAME; }
        public string name_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, name_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            name_ = PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_C_REQ_CHATTING : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_C_REQ_CHATTING; }
        Int64 type() { return (Int64)PacketType.E_C_REQ_CHATTING; }
        public string text_ = "";
        public UInt64 clientTimestamp_ = 0; // 클라이언트가 메시지를 보낸 시간 (명시적 초기화)

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, text_);
            PacketUtil.encode(packet_, clientTimestamp_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            text_ = PacketUtil.decodestring(packet, ref offset);
            clientTimestamp_ = PacketUtil.decodeUInt64(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_S_ANS_CHATTING : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_CHATTING; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_CHATTING; }
        public string name_;
        public string text_;
        public UInt64 serverTimestamp_; // 서버가 응답을 보낸 시간

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, name_);
            PacketUtil.encode(packet_, text_);
            PacketUtil.encode(packet_, serverTimestamp_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            name_ = PacketUtil.decodestring(packet, ref offset);
            text_ = PacketUtil.decodestring(packet, ref offset);
            serverTimestamp_ = PacketUtil.decodeUInt64(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_S_ANS_NEW_USER_NOTIFY : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_NEW_USER_NOTIFY; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_NEW_USER_NOTIFY; }
        public string name_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, name_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            name_ = PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_S_ANS_USER_LIST : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_USER_LIST; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_USER_LIST; }

        public List<string> names_ = new List<string>();

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());

            PacketUtil.encode(packet_, (Int32)names_.Count);

            foreach (string name in names_)
            {
                PacketUtil.encode(packet_, name);
            }
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            Int32 count = PacketUtil.decodeInt32(packet, ref offset);

            names_.Clear();

            for (int i = 0; i < count; i++)
            {
                string name = PacketUtil.decodestring(packet, ref offset);
                names_.Add(name);
            }
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_S_ANS_EXIT_USER : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_EXIT_USER; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_EXIT_USER; }
        public string name_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, name_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            name_ = PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
    public class PK_C_REQ_CHAT_EXIT : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_C_REQ_CHAT_EXIT; }
        Int64 type() { return (Int64)PacketType.E_C_REQ_CHAT_EXIT; }
        //public string name_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            // PacketUtil.encode(packet_, name_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            // name_ = PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_C_REQ_CREATE_CHARACTER : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_C_REQ_CREATE_CHARACTER; }
        Int64 type() { return (Int64)PacketType.E_C_REQ_CREATE_CHARACTER; }
        public UInt64 clientId_;
        public string id_;
        public string password_;
        public UInt64 oidAccountId_;
        public UInt32 level_;
        public UInt64 exp_;
        public string name_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, id_);
            PacketUtil.encode(packet_, password_);
            PacketUtil.encode(packet_, oidAccountId_);
            PacketUtil.encode(packet_, level_);
            PacketUtil.encode(packet_, exp_);
            PacketUtil.encode(packet_, name_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            id_ = PacketUtil.decodestring(packet, ref offset);
            password_ = PacketUtil.decodestring(packet, ref offset);
            oidAccountId_ = PacketUtil.decodeUInt64(packet,ref offset);
            level_ = PacketUtil.decodeUInt32(packet, ref offset);
            exp_= PacketUtil.decodeUInt64(packet, ref offset);
            name_= PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_I_DB_REQ_CHARACTER : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_DB_REQ_CHARACTER; }
        Int64 type() { return (Int64)PacketType.E_I_DB_REQ_CHARACTER; }
        public UInt64 clientId_;
        //public string id_;
        //public string password_;
        public UInt64 oidAccountId_;
        //public UInt32 level_;
        //public UInt64 exp_;
        public string name_;
        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
           // PacketUtil.encode(packet_, id_);
           // PacketUtil.encode(packet_, password_);
            PacketUtil.encode(packet_, oidAccountId_);
           // PacketUtil.encode(packet_, level_);
           // PacketUtil.encode(packet_, exp_);
            PacketUtil.encode(packet_, name_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
           // id_ = PacketUtil.decodestring(packet, ref offset);
          //  password_ = PacketUtil.decodestring(packet, ref offset);
            oidAccountId_ = PacketUtil.decodeUInt64(packet, ref offset);
           // level_ = PacketUtil.decodeUInt32(packet, ref offset);
           // exp_= PacketUtil.decodeUInt64(packet, ref offset);
            name_= PacketUtil.decodestring(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_I_DB_ANS_CREATE_CHARACTER : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_DB_ANS_CREATE_CHARACTER; }
        Int64 type() { return (Int64)PacketType.E_I_DB_ANS_CREATE_CHARACTER; }
        public UInt64 clientId_;
        public UInt64 oidAccountId_;
        public string name_;
        public Byte result_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, oidAccountId_);
            PacketUtil.encode(packet_, name_);
            PacketUtil.encode(packet_, result_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            oidAccountId_ = PacketUtil.decodeUInt64(packet, ref offset);
            name_=PacketUtil.decodestring(packet,ref offset); 
            result_ = PacketUtil.decodeByte(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_C_REQ_CREATE_USER : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_C_REQ_CREATE_USER; }
        Int64 type() { return (Int64)PacketType.E_C_REQ_CREATE_USER; }
        public UInt64 clientId_;
        public string id_;
        public string password_;
        public Byte result_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, id_);
            PacketUtil.encode(packet_, password_);
            PacketUtil.encode(packet_, result_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            id_ = PacketUtil.decodestring(packet, ref offset);
            password_ = PacketUtil.decodestring(packet, ref offset);
            result_ = PacketUtil.decodeByte(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_I_DB_REQ_CREATE_USER : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_DB_REQ_CREATE_USER; }
        Int64 type() { return (Int64)PacketType.E_I_DB_REQ_CREATE_USER; }
        public UInt64 clientId_;
        public UInt64 oidAccountId_;
        public string id_;
        public string password_;
        public Byte result_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, oidAccountId_);
            PacketUtil.encode(packet_, id_);
            PacketUtil.encode(packet_, password_);
            PacketUtil.encode(packet_, result_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            oidAccountId_ = PacketUtil.decodeUInt64(packet,ref offset);
            id_ = PacketUtil.decodestring(packet, ref offset);
            password_ = PacketUtil.decodestring(packet, ref offset);
            result_ = PacketUtil.decodeByte(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_I_DB_ANS_CREATE_USER : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_DB_ANS_CREATE_USER; }
        Int64 type() { return (Int64)PacketType.E_I_DB_ANS_CREATE_USER; }
        public UInt64 clientId_;
        public UInt64 oidAccountId_;
        public string name_;
        public Byte result_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, oidAccountId_);
            PacketUtil.encode(packet_, name_);
            PacketUtil.encode(packet_, result_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            oidAccountId_ = PacketUtil.decodeUInt64(packet, ref offset);
            name_ = PacketUtil.decodestring(packet, ref offset);
            result_ = PacketUtil.decodeByte(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_C_REQ_CREATE_CHARACTER_ID_PW : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_C_REQ_CREATE_CHARACTER_ID_PW; }
        Int64 type() { return (Int64)PacketType.E_C_REQ_CREATE_CHARACTER_ID_PW; }
        public UInt64 clientId_;
        public string id_;
        public string password_;
        public string name_;
        public Byte result_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, id_);
            PacketUtil.encode(packet_, password_);
            PacketUtil.encode(packet_, name_);
            PacketUtil.encode(packet_, result_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            id_= PacketUtil.decodestring(packet, ref offset);
            password_= PacketUtil.decodestring(packet,  ref offset);
            name_ = PacketUtil.decodestring(packet, ref offset);
            result_ = PacketUtil.decodeByte(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_I_DB_REQ_CREATE_CHARACTER_ID_PW : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_DB_REQ_CREATE_CHARACTER_ID_PW; }
        Int64 type() { return (Int64)PacketType.E_I_DB_REQ_CREATE_CHARACTER_ID_PW; }
        public UInt64 clientId_;
        public string id_;
        public string password_;
        public string name_;
        public Byte result_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            PacketUtil.encode(packet_, id_);
            PacketUtil.encode(packet_, password_);
            PacketUtil.encode(packet_, name_);
            PacketUtil.encode(packet_, result_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            id_= PacketUtil.decodestring(packet, ref offset);
            password_= PacketUtil.decodestring(packet, ref offset);
            name_ = PacketUtil.decodestring(packet, ref offset);
            result_ = PacketUtil.decodeByte(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_S_ANS_CREATE_FAIL : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_CREATE_FAIL; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_CREATE_FAIL; }
        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_I_DB_ANS_CREATE_CHARACTER_SUCCESS : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_I_DB_ANS_CREATE_CHARACTER_SUCCESS; }
        Int64 type() { return (Int64)PacketType.E_I_DB_ANS_CREATE_CHARACTER_SUCCESS; }
        public UInt64 clientId_;
        //public UInt64 oidAccountId_;
        public Byte result_;

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientId_);
            //PacketUtil.encode(packet_, oidAccountId_);
            PacketUtil.encode(packet_, result_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientId_ = PacketUtil.decodeUInt64(packet, ref offset);
            //oidAccountId_ = PacketUtil.decodeUInt64(packet, ref offset);
            result_ = PacketUtil.decodeByte(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_S_ANS_CREATE_CHARACTER_SUCCESS : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_CREATE_CHARACTER_SUCCESS; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_CREATE_CHARACTER_SUCCESS; }
        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_C_REQ_PING : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_C_REQ_PING; }
        Int64 type() { return (Int64)PacketType.E_C_REQ_PING; }
        
        public UInt64 clientTimestamp_;    // Client timestamp when ping was sent
        public UInt32 sequenceNumber_;     // Sequence number for tracking

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientTimestamp_);
            PacketUtil.encode(packet_, sequenceNumber_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientTimestamp_ = PacketUtil.decodeUInt64(packet, ref offset);
            sequenceNumber_ = PacketUtil.decodeUInt32(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }

    public class PK_S_ANS_PONG : PacketData, PacketInterface
    {
        Int64 PacketInterface.type() { return (Int64)PacketType.E_S_ANS_PONG; }
        Int64 type() { return (Int64)PacketType.E_S_ANS_PONG; }
        
        public UInt64 clientTimestamp_;    // Original client timestamp
        public UInt64 serverTimestamp_;    // Server timestamp when received
        public UInt32 sequenceNumber_;     // Sequence number for tracking

        void PacketInterface.encode()
        {
            PacketUtil.encodeHeader(packet_, this.type());
            PacketUtil.encode(packet_, clientTimestamp_);
            PacketUtil.encode(packet_, serverTimestamp_);
            PacketUtil.encode(packet_, sequenceNumber_);
        }
        void PacketInterface.decode(byte[] packet, ref int offset)
        {
            clientTimestamp_ = PacketUtil.decodeUInt64(packet, ref offset);
            serverTimestamp_ = PacketUtil.decodeUInt64(packet, ref offset);
            sequenceNumber_ = PacketUtil.decodeUInt32(packet, ref offset);
        }
        MemoryStream PacketInterface.getStream()
        {
            return packet_;
        }
    }
}
