#include <iostream>

#include "log.hpp" 

namespace pj {

void _log(const char *fmt, ...) {
    static const int MAX_MESSAGE_LEN = 1024;

    char message[MAX_MESSAGE_LEN];
    va_list parglist;
    va_start(parglist, fmt);
    vsprintf(message, fmt, parglist);
    va_end(parglist);

    std::cout << "[ERROR] " << message << std::endl;
}


}
