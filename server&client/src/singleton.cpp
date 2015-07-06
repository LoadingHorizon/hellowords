#include "singleton.hpp"

namespace pj {

WordsManager* Singleton::pInstance = 0;

inline WordsManager* Singleton::GetInstance() {
    if (0 == pInstance) {
        pInstance = new WordsManager();
    }

    return pInstance;
}

}
