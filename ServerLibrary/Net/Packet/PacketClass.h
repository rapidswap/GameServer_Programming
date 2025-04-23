#pragma once
#include "stdafx.h"
#include "packetHeader.h"
#include "Stream.h"


class Packet {

public:
    virtual PacketType type() = 0;
    virtual void encode(Stream &stream) { stream << (Int64) this->type(); };
    virtual void decode(Stream &stream) { };

};

class PK_C_REQ_EXIT : public Packet
{
public:
    PacketType type() { return E_C_REQ_EXIT; }

};

class PK_S_ANS_EXIT : public Packet
{

public:
    PacketType type() { return E_S_ANS_EXIT; }

};

class PK_I_NOTIFY_TERMINAL : public Packet
{
public:
    PacketType type() { return E_I_NOTIFY_TERMINAL; }

};

class PK_C_NOTIFY_HEARTBEAT : public Packet
{
public:
    PacketType type() { return E_C_NOTIFY_HEARTBEAT; }

};

class PK_C_REQ_ID_PW : public Packet
{
public:
    PacketType type() { return E_C_REQ_ID_PW; }

    std::string     id_;
    std::string     password_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << id_;
        stream << password_;
    }

    void decode(Stream &stream) {
        stream >> &id_;
        stream >> &password_;
    }
};

class PK_S_ANS_ID_PW_FAIL : public Packet
{
public:
    PacketType type() { return E_S_ANS_ID_PW_FAIL; }

};

class PK_S_ANS_ID_PW_SUCCESS : public Packet
{
public:
    PacketType type() { return E_S_ANS_ID_PW_SUCCESS; }

    std::string     ip_;
    UInt32     port_;
    std::string     name_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << ip_;
        stream << port_;
        stream << name_;
    }

    void decode(Stream &stream) {
        stream >> &ip_;
        stream >> &port_;
        stream >> &name_;
    }
};

class PK_I_DB_REQ_ID_PW : public Packet
{
public:
    PacketType type() { return E_I_DB_REQ_ID_PW; }

    UInt64     clientId_;
    std::string     id_;
    std::string     password_;


    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << clientId_;
        stream << id_;
        stream << password_;
    }

    void decode(Stream &stream) {
        stream >> &clientId_;
        stream >> &id_;
        stream >> &password_;
    }
};

class PK_I_DB_ANS_ID_PW : public Packet
{
public:
    PacketType type() { return E_I_DB_ANS_ID_PW; }

    UInt64     clientId_;
    UInt64     oidAccountId_;
    Byte     result_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << clientId_;
        stream << oidAccountId_;
        stream << result_;
    }

    void decode(Stream &stream) {
        stream >> &clientId_;
        stream >> &oidAccountId_;
        stream >> &result_;
    }
};

class PK_I_CHTTING_NOTIFY_ID : public Packet
{
public:
    PacketType type() { return E_I_CHTTING_NOTIFY_ID; }

    UInt64     clientId_;
    UInt64     oidAccountId_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << clientId_;
        stream << oidAccountId_;
    }

    void decode(Stream &stream) {
        stream >> &clientId_;
        stream >> &oidAccountId_;
    }
};

class PK_I_DB_REQ_LOAD_DATA : public Packet
{
public:
    PacketType type() { return E_I_DB_REQ_LOAD_DATA; }

    UInt64     clientId_;
    UInt64     oidAccountId_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << clientId_;
        stream << oidAccountId_;
    }

    void decode(Stream &stream) {
        stream >> &clientId_;
        stream >> &oidAccountId_;
    }
};

class PK_I_DB_ANS_PARSE_DATA : public Packet
{
public:
    PacketType type() { return E_I_DB_ANS_PARSE_DATA; }

    UInt64     clientId_;
    std::string     name_;
    Byte     result_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << clientId_;
        stream << name_;
        stream << result_;
    }

    void decode(Stream &stream) {
        stream >> &clientId_;
        stream >> &name_;
        stream >> &result_;
    }
};

class PK_I_LOGIN_NOTIFY_ID_LOADED : public Packet
{
public:
    PacketType type() { return E_I_LOGIN_NOTIFY_ID_LOADED; }

    UInt64     clientId_;
    std::string     name_;
    Byte     result_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << clientId_;
        stream << name_;
        stream << result_;
    }

    void decode(Stream &stream) {
        stream >> &clientId_;
        stream >> &name_;
        stream >> &result_;
    }
};

class PK_C_REQ_REGIST_CHATTING_NAME : public Packet
{
public:
    PacketType type() { return E_C_REQ_REGIST_CHATTING_NAME; }

    std::string     name_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << name_;
    }

    void decode(Stream &stream) {
        stream >> &name_;
    }
};

class PK_C_REQ_CHATTING : public Packet
{
public:
    PacketType type() { return E_C_REQ_CHATTING; }

    std::string     text_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << text_;
    }

    void decode(Stream &stream) {
        stream >> &text_;
    }
};

class PK_S_ANS_CHATTING : public Packet
{
public:
    PacketType type() { return E_S_ANS_CHATTING; }

    std::string     name_;
    std::string     text_;

    void encode(Stream &stream) {
        stream << (Int64) this->type();
        stream << name_;
        stream << text_;
    }

    void decode(Stream &stream) {
        stream >> &name_;
        stream >> &text_;
    }
};

class PK_S_ANS_NEW_USER_NOTIFY :public Packet
{
public:
    PacketType type() { return E_S_ANS_NEW_USER_NOTIFY; }

    std::string name_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << name_;
    }

    void decode(Stream& stream) {
        stream >> &name_;
    }
};

class PK_S_ANS_USER_LIST :public Packet
{
public:
    PacketType type() { return E_S_ANS_USER_LIST; }

    std::vector<std::string> names_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << (Int32)names_.size();
        for (const auto& name : names_) {
            stream << name;
        }
    }

    void decode(Stream& stream) {
        Int32 size;
        stream >> &size;

        names_.clear();
        for (Int32 i = 0; i < size; i++) {
            std::string name;
            stream >> &name;
            names_.push_back(name);
        }
    }
};

class PK_S_ANS_EXIT_USER :public Packet
{
public:
    PacketType type() { return E_S_ANS_EXIT_USER; }

    std::string name_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << name_;
    }

    void decode(Stream& stream) {
        stream >> &name_;
    }
};
class PK_C_REQ_CHAT_EXIT :public Packet
{
public:
    PacketType type() { return E_C_REQ_CHAT_EXIT; }
    std::string name_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << name_;
    }

    void decode(Stream& stream) {
        stream >> &name_;
    }
};

class PK_C_REQ_CREATE_CHARACTER : public Packet
{
public:
    PacketType type() { return E_C_REQ_CREATE_CHARACTER; }

    UInt64     clientId_;
    std::string     id_;
    std::string     password_;
    UInt64          oidAccountId_;
    UInt32          level_;
    UInt64          exp_;
    std::string     name_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << clientId_;
        stream << id_;
        stream << password_;
        stream << oidAccountId_;
        stream << level_;
        stream << exp_;
        stream << name_;
    }

    void decode(Stream& stream) {
        stream >> &clientId_;
        stream >> &id_;
        stream >> &password_;
        stream >> &oidAccountId_;
        stream >> &level_;
        stream >> &exp_;
        stream >> &name_;
    }
};


class PK_I_DB_REQ_CREATE_CHARACTER : public Packet
{
public:
    PacketType type() { return E_I_DB_REQ_CREATE_CHARACTER; }

    UInt64     clientId_;
    UInt64          oidAccountId_;
    //UInt32          level_;
    //UInt64          exp_;
    std::string     name_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << clientId_;
        //stream << id_;
        //stream << password_;
        stream << oidAccountId_;
        //stream << level_;
        //stream << exp_;
        stream << name_;
    }

    void decode(Stream& stream) {
        stream >> &clientId_;
        //stream >> &id_;
        //stream >> &password_;
        stream >> &oidAccountId_;
        //stream >> &level_;
        //stream >> &exp_;
        stream >> &name_;
    }
};

class PK_I_DB_ANS_CREATE_CHARACTER : public Packet
{
public:
    PacketType type() { return E_I_DB_ANS_CREATE_CHARACTER; }

    UInt64     clientId_;
    UInt64     oidAccountId_;
    std::string name_;
    Byte     result_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << clientId_;
        stream << oidAccountId_;
        stream << name_;
        stream << result_;
    }

    void decode(Stream& stream) {
        stream >> &clientId_;
        stream >> &oidAccountId_;
        stream >> &name_;
        stream >> &result_;
    }
};

class PK_C_REQ_CREATE_USER :public Packet
{
public:
    PacketType type() { return E_C_REQ_CREATE_USER; }

    UInt64     clientId_;
    std::string id_;
    std::string password_;
    Byte     result_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << clientId_;
        stream << id_;
        stream << password_;
        stream << result_;
    }

    void decode(Stream& stream) {
        stream >> &clientId_;
        stream >> &id_;
        stream >> &password_;
        stream >> &result_;
    }
};

class PK_I_DB_REQ_CREATE_USER :public Packet
{
public:
    PacketType type() { return E_I_DB_REQ_CREATE_USER; }

    UInt64     clientId_;
    UInt64 oidAccoundId_;
    std::string id_;
    std::string password_;
    Byte     result_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << clientId_;
        stream << oidAccoundId_;
        stream << id_;
        stream << password_;
        stream << result_;
    }

    void decode(Stream& stream) {
        stream >> &clientId_;
        stream >> &oidAccoundId_;
        stream >> &id_;
        stream >> &password_;
        stream >> &result_;
    }
};

class PK_I_DB_ANS_CREATE_USER :public Packet
{
public:
    PacketType type() { return E_I_DB_ANS_CREATE_USER; }

    UInt64     clientId_;
    UInt64 oidAccountId_;
    std::string name_;
    Byte     result_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << clientId_;
        stream << oidAccountId_;
        stream << name_;
        stream << result_;
    }

    void decode(Stream& stream) {
        stream >> &clientId_;
        stream >> &oidAccountId_;
        stream >> &name_;
        stream >> &result_;
    }
};

class PK_C_REQ_CREATE_CHARACTER_ID_PW :public Packet
{
public:
    PacketType type() { return E_C_REQ_CREATE_CHARACTER_ID_PW; }

    UInt64     clientId_;
    std::string id_;
    std::string password_;
    std::string name_;
    Byte     result_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << clientId_;
        stream << id_;
        stream << password_;
        stream << name_;
        stream << result_;
    }

    void decode(Stream& stream) {
        stream >> &clientId_;
        stream >> &id_;
        stream >> &password_;
        stream >> &name_;
        stream >> &result_;
    }
};

class PK_I_DB_REQ_CREATE_CHARACTER_ID_PW :public Packet
{
public:
    PacketType type() { return E_I_DB_REQ_CREATE_CHARACTER_ID_PW; }

    UInt64     clientId_;
    std::string id_;
    std::string password_;
    std::string name_;
    Byte     result_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << clientId_;
        stream << id_;
        stream << password_;
        stream << name_;
        stream << result_;
    }

    void decode(Stream& stream) {
        stream >> &clientId_;
        stream >> &id_;
        stream >> &password_;
        stream >> &name_;
        stream >> &result_;
    }
};

class PK_S_ANS_CREATE_FAIL : public Packet
{
public:
    PacketType type() { return E_S_ANS_CREATE_FAIL; }

};

class PK_I_DB_ANS_CREATE_CHARACTER_SUCCESS :public Packet
{
public:
    PacketType type() { return E_I_DB_ANS_CREATE_CHARACTER_SUCCESS; }

    UInt64     clientId_;
    //UInt64 oidAccountId_;
    Byte     result_;

    void encode(Stream& stream) {
        stream << (Int64)this->type();
        stream << clientId_;
        //stream << oidAccountId_;
        stream << result_;
    }

    void decode(Stream& stream) {
        stream >> &clientId_;
        //stream >> &oidAccountId_;
        stream >> &result_;
    }
};

class PK_S_ANS_CREATE_CHARACTER_SUCCESS : public Packet
{
public:
    PacketType type() { return E_S_ANS_CREATE_CHARACTER_SUCCESS; }

};

class PK_S_ANS_CREATE_CHARACTER_FAIL :public Packet
{
    PacketType type() { return E_S_ANS_CREATE_CHARACTER_FAIL; }
};