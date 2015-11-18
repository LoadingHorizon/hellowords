#ifndef _WORDS_MANAGER_H_
#define _WORDS_MANAGER_H_

#include <vector>
#include <string>

namespace pj {

class WordsManager {
public:
    WordsManager();
    std::string GetOne();
    static const int MaxLineLength;
private:
    std::vector<std::string> words;
    int init_load_file();
};

}
#endif