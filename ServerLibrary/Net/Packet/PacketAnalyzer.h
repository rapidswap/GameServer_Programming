#pragma once
#include "pch.h"

class PacketAnalyzer :public Singleton<PacketAnalyzer>
{
public:
	Packet* analyzer(const char* rowPacket, size_t size);
};