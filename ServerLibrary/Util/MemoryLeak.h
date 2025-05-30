#pragma once
#include "stdafx.h"

#ifndef _DEBUG
#define USE_VISUAL_LEAK_DETECTOR
#endif

#ifdef USE_VISUAL_LEAK_DETECTOR
#include <vld.h>

#else 


#define _CRTDBG_MAP_ALLOC
#include "crtdbg.h"

#if 0 //실제 내부는 아래와 같이 선언되어 있다.
#ifdef  _CRTDBG_MAP_ALLOC

#define   malloc(s)
_malloc_dbg(s, _NORMAL_BLOCK, __FILE__, __LINE__)
#define   calloc(c, s)
_calloc_dbg(c, s, _NORMAL_BLOCK, __FILE__, __LINE__)
#define   realloc(p, s)
_realloc_dbg(p, s, _NORMAL_BLOCK, __FILE__, __LINE__)
#define   _expand(p, s)
_expand_dbg(p, s, _NORMAL_BLOCK, __FILE__, __LINE__)
#define   free(p)
_free_dbg(p, _NORMAL_BLOCK)
#define   _msize(p)         _msize_dbg(p, _NORMAL_BLOCK)

#endif  /* _CRTDBG_MAP_ALLOC */
#endif

class MemoryLeckDetct
{
public:
    MemoryLeckDetct()
    {
        _CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF);
        // Send all reports to STDOUT
        _CrtSetReportMode(_CRT_WARN, _CRTDBG_MODE_FILE);
        _CrtSetReportFile(_CRT_WARN, _CRTDBG_FILE_STDOUT);
        _CrtSetReportMode(_CRT_ERROR, _CRTDBG_MODE_FILE);
        _CrtSetReportFile(_CRT_ERROR, _CRTDBG_FILE_STDOUT);
        _CrtSetReportMode(_CRT_ASSERT, _CRTDBG_MODE_FILE);
        _CrtSetReportFile(_CRT_ASSERT, _CRTDBG_FILE_STDOUT);


    }

    ~MemoryLeckDetct()
    {
        //서버 종료시 메모리 체크해줍니다.
        _ASSERTE(_CrtCheckMemory());
    }
};

//static MemoryLeckDetct leck;
#endif //USE_VISUAL_LEAK_DETECTOR