#pragma once
#include "pch.h"

class SessionMonitor : public Work
{
public:
	SessionMonitor();
	void tick();
};
static SessionMonitor sessionMonitor;