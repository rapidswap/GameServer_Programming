#pragma once
#include "pch.h"

bool conncetSMPT(SOCKET* sock);
bool sendMail(const char* from, const char* to, const char* subject, const char* body, const char* username, const char* password);