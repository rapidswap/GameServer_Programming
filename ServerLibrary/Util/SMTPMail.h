#pragma once
#include "pch.h"

bool connectSMTP(SOCKET* sock);
bool sendMail(const char* from, const char* to, const char* subject, const char* body);