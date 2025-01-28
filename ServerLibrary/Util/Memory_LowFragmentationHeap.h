#pragma once
#include "pch.h"

class LowFragmentationHeap
{
public:
	LowFragmentationHeap()
	{
		static bool init = false;
		if (init) {
			return;
		}
		init = true;

		ULONG HeapFragValue = 2;
		HANDLE hHeaps[100];
		DWORD dwHeapCount = GetProcessHeaps(100, hHeaps);

		for (DWORD i = 0; i < dwHeapCount; i++) {
			HeapSetInformation(hHeaps[i],
				HeapCompatibilityInformation,
				&HeapFragValue,
				sizeof(HeapFragValue));

		}
		printf("* Low-fragmentation Heap setting\n");
	}
};

static LowFragmentationHeap lfh;
