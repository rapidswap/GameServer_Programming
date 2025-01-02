#include "pch.h"
#include "Config.h"

bool loadConfig(xml_t* config)
{
	if (!config->LoadFile("C:/github/GameServer_Programming/ServerLibrary/Util/config.xml")) {
		printf("! not exist config file.");
		return false;
	}
	return true;
}