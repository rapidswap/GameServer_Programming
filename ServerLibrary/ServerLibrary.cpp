#include "pch.h"

int main()
{
    const char* from = "kjseoin7988@naver.com";  // 발신자 이메일 주소
    const char* to = "kjseoin7988@naver.com"; // 수신자 이메일 주소
    const char* subject = "Test Email"; // 이메일 제목
    const char* body = "This is a test email sent from C++ using SMTP."; // 이메일 본문
    const char* username = "kjseoin7988@naver.com"; // 네이버 이메일 주소
    const char* password = ""; // 네이버 이메일 비밀번호

    // 이메일 보내기
    if (sendMail(from, to, subject, body, username, password)) {
        printf("Email sent successfully!\n");
    }
    else {
        printf("Failed to send email.\n");
    }

    return 0;
}
