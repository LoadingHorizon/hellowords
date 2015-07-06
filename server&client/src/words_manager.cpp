#include <fstream>
#include <cstdlib>

#include "words_manager.hpp"
#include "log.hpp"

namespace pj {

const int WordsManager::MaxLineLength = 1024;

WordsManager::WordsManager() {
    if (init_load_file() != 0) {
        LOG("File open fail.");
        exit(1);
    }
}

int WordsManager::init_load_file() {
    std::ifstream file;
    file.open("words.data", std::ifstream::in);

    if (!file.good()) {
        return -1;
    }

    char line_buffer[MaxLineLength];

    while (file.good()) {
        file.getline(line_buffer, MaxLineLength);
        std::string line(line_buffer);
        words.push_back(line);
    }

    file.close();

    return 0;
}

std::string WordsManager::GetOne() {
    if (words.size() > 0) {
        return words[0];
    } else {
        LOG("No Words.");
        return "hello words";
    }
}

}
