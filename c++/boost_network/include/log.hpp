#ifndef _LOG_H_
#define _LOG_H_

#include <cstdarg>
#include <stdio.h>

#define LOG(fmt, arg...) \
    do { \
        _log("[%s:%d][%s]"fmt, __FILE__, __LINE__, __FUNCTION__, ##arg); \
    } while(0)

namespace pj {

extern void _log(const char *fmt, ...); 

}

#endif
