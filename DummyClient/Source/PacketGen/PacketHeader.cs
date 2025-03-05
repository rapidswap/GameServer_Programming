using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.IO;

namespace DummyClient
{
    static class PacketMakeDate
    {
        static public string stamp()
        {
            return "2025/03/01 12:13:55";
        }
    }
    enum PacketType : long
    {
        E_C_REQ_EXIT = 128,
        E_S_ANS_EXIT = 129,
        E_I_NOTIFY_TERMINAL = 130,
        E_C_NOTIFY_HEARTBEAT = 131,
        E_C_REQ_ID_PW = 132,
        E_S_ANS_ID_PW_FAIL = 133,
        E_S_ANS_ID_PW_SUCCESS = 134,
        E_I_DB_REQ_ID_PW = 135,
        E_I_DB_ANS_ID_PW = 136,
        E_I_CHTTING_NOTIFY_ID = 137,
        E_I_DB_REQ_LOAD_DATA = 138,
        E_I_DB_ANS_PARSE_DATA = 139,
        E_I_LOGIN_NOTIFY_ID_LOADED = 140,
        E_C_REQ_REGIST_CHATTING_NAME = 141,
        E_C_REQ_CHATTING = 142,
        E_S_ANS_CHATTING = 143,
        E_S_ANS_NEW_USER_NOTIFY = 144,
        E_S_ANS_USER_LIST = 145,
        E_S_ANS_EXIT_USER = 146,
        E_C_REQ_CHAT_EXIT=147,
    }
};
