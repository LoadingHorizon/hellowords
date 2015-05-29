# coding: utf-8
__author__ = 'PlayJokes'

import os

class TextFile:
    def __init__(self, filename):
        if os.path.exists(filename):
            self.file = open(filename, 'a', encoding="UTF-8")
        else:
            self.file = open(filename, 'w', encoding="UTF-8")

    def insertSentence(self, sentence, author, source):
        self.file.write(sentence)
        self.file.write('\n')

    def __del__(self):
        self.file.close()
