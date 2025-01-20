//#include "pch.h"
#include <vector>
#include <iostream>
#include "./Net/Packet/Stream.h"

class Packet
{
public:
	int a;
	int8_t b;
	float c;
	vector<int> d;

	Packet()
	{

	}

	Packet(Stream& stream)
	{
		this->decode(stream);
	}
	void encode(Stream& stream)
	{
		stream << a;
		stream << b;
		stream << c;
		stream << d;
	}
	void decode(Stream& stream)
	{
		stream >> &a;
		stream >> &b;
		stream >> &c;
		stream >> &d;
	}
};

int t_main(int argc, _TCHAR* argv[])
{
	Stream sender;
	{
		Packet sendPacket;
		sendPacket.a = 0xff00f1;
		sendPacket.b = 'A';
		sendPacket.c = 2.12395f;
		sendPacket.d.push_back(124);
		sendPacket.d.push_back(2623);
		sendPacket.d.push_back(4568);
		sendPacket.d.push_back(2346);
		sendPacket.d.push_back(6708);

		sendPacket.encode(sender);
	}

	Stream reciever;
	reciever = sender;
	{
		Packet recvPacket;
		recvPacket.decode(reciever);

		cout << recvPacket.a << endl;
		cout << recvPacket.b << endl;
		cout << recvPacket.c << endl;
		for (auto n : recvPacket.d) {
			cout << n << endl;
		}
	}
	return 0;
}