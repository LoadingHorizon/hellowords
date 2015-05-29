# coding: utf-8
__author__ = 'PlayJokes'
import database
import text_file

class SentenceManager:
    def __init__(self, type):
        if type == 'database':
            self.container = database.DataBase();
        elif type == 'text':
            self.container = text_file.TextFile("./words.data")

    def insertSentence(self, sentence, author, source):
        self.container.insertSentence(sentence, author, source)