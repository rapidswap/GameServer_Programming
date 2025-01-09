#include "pch.h"

int main()
{
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        SLog(L"! WSAStartup failed");
        return false;
    }

    sendMail("testserver@ipaddr.co.kr", "kjseoin7988@naver.com", "test mail", "this is test news");
    WSACleanup();

    return 0;
}
