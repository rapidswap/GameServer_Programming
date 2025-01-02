#include "pch.h"
#include "SMTPMail.h"

#include <openssl/ssl.h>
#include <openssl/err.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <iostream>
#include <array>
#include <vector>

std::string base64_encode(const std::string& in) {
    static const char* base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    std::string out;

    int val = 0, valb = -6;
    for (unsigned char c : in) {
        val = (val << 8) + c;
        valb += 8;
        while (valb >= 0) {
            out.push_back(base64_chars[(val >> valb) & 0x3F]);
            valb -= 6;
        }
    }
    if (valb > -6) out.push_back(base64_chars[((val << 8) >> valb) & 0x3F]);
    while (out.size() % 4) out.push_back('=');
    return out;
}

void smtpWriteLine(SSL* ssl, const char* str, const char* arg)
{
    array<char, SIZE_4096> buf; // std::array ���
    if (arg != NULL) {
        snprintf(buf, str, arg); // buf.data()�� ���� ������ ���
    }
    else {
        snprintf(buf, str); // buf.data()�� ���� ������ ���
    }


    // SSL_write ȣ�� �� buf�� NULL�� �ƴ��� Ȯ��
    int bytesWritten = SSL_write(ssl, buf.data(), strlen(buf.data()));
    if (bytesWritten <= 0) {
        // ���� ó�� �߰�
        int err = SSL_get_error(ssl, bytesWritten);
        fprintf(stderr, "SSL_write failed with error: %d\n", err);
    }
}

bool connectSMTP(SSL** ssl, const char* hostname) {
    // Winsock �ʱ�ȭ
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "WSAStartup failed." << std::endl;
        return false;
    }

    SOCKET sock = ::socket(AF_INET, SOCK_STREAM, 0);
    if (sock == SOCKET_ERROR) {
        std::cerr << "Socket creation failed with error: " << WSAGetLastError() << std::endl;
        return false;
    }

    const int SMTP_PORT = 465; // �Ǵ� 465�� ������ �� �� �ֽ��ϴ�
    struct sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(SMTP_PORT);
    inet_pton(AF_INET, "smtp.naver.com", &(serverAddr.sin_addr)); // ���̹� SMTP ���� �ּ�

    if (::connect(sock, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR) {
        std::cerr << "Connection failed with error: " << WSAGetLastError() << std::endl;
        return false;
    }

    // SSL �ʱ�ȭ
    SSL_library_init();
    SSL_CTX* ctx = SSL_CTX_new(TLS_client_method());
    *ssl = SSL_new(ctx);
    SSL_set_fd(*ssl, sock);

    if (SSL_connect(*ssl) <= 0) {
        ERR_print_errors_fp(stderr);
        return false;
    }

    return true;
}

bool sendMail(const char* from, const char* to, const char* subject, const char* body, const char* username, const char* password) {
    SSL* ssl;
    if (!connectSMTP(&ssl, "smtp.naver.com")) { // SSL ����
        std::cerr << "! smtp mail port connect fail, mail :[" << subject << "] body => " << body << std::endl;
        return false;
    }

    // SMTP AUTH
    smtpWriteLine(ssl, "EHLO %s", from);
    smtpWriteLine(ssl, "AUTH LOGIN", NULL);

    // ����� �̸��� ��й�ȣ�� Base64�� ���ڵ�
    std::cout << "Encoding Username: " << username << std::endl;
    std::cout << "Encoding Password: " << password << std::endl;

    std::string encodedUsername = base64_encode(username);
    std::string encodedPassword = base64_encode(password);

    smtpWriteLine(ssl, "%s", encodedUsername.c_str());
    smtpWriteLine(ssl, "%s", encodedPassword.c_str());

    smtpWriteLine(ssl, "MAIL FROM: %s", from);
    smtpWriteLine(ssl, "RCPT TO: %s", to);
    smtpWriteLine(ssl, "DATA", NULL);

    smtpWriteLine(ssl, "From: %s", from);
    smtpWriteLine(ssl, "To: %s", to);
    smtpWriteLine(ssl, "Subject: %s", subject);

    smtpWriteLine(ssl, "\n", NULL);
    smtpWriteLine(ssl, "%s", body);
    smtpWriteLine(ssl, ".", NULL);
    smtpWriteLine(ssl, "QUIT", NULL);

    SSL_shutdown(ssl);
    SSL_free(ssl);
    std::cout << "* send mail [" << subject << "]" << std::endl;

    return true;
}
