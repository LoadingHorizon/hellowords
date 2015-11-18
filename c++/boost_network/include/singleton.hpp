#ifndef _SINGLETON_H_
#define _SINGLETON_H_

#include "words_manager.hpp"

namespace pj {

class Singleton {
public:
    static inline WordsManager* GetInstance();
private:
    static WordsManager* pInstance;
    Singleton() {}
    Singleton(const Singleton &){}
    Singleton& operator =(const Singleton &){}
};

WordsManager* Singleton::pInstance = 0;

inline WordsManager* Singleton::GetInstance() {
    if(0 == pInstance) {
        pInstance = new WordsManager();
    }

    return pInstance;
}

}
#endif
