# coding: utf-8

__author__ = 'PlayJokes'


import mysql.connector
import sys
import os

class DataBase:
    config = {
        'user': 'root',
        'password': '123654',
        'host': '127.0.0.1',
        'database': 'hellowords'
    }

    create_table_sql = """CREATE TABLE IF NOT EXISTS words(
                    sid int AUTO_INCREMENT PRIMARY KEY,
                    sentence nvarchar(200),
                    author nvarchar(50),
                    source varchar(50),
                    count int)"""

    def __init__(self):
        # load_config
        self.connect = mysql.connector.connect(**DataBase.config)
        self.update(DataBase.create_table_sql)

    def query(self, sql):
        cursor = self.connect.cursor()
        try:
            cursor.execute(sql)
        except mysql.connector.Error as err:
            print('Error: {}'.format(err.msg))
            sys.exit(1)
        return cursor.fetchall()

    def update(self, sql):
        cursor = self.connect.cursor()
        try:
            n = cursor.execute(sql)
            self.connect.commit()
        except mysql.connector.Error as err:
            print('Error: {}'.format(err.msg))
            sys.exit(1)
        return n

    def selectSentence(self):
        select_sql = 'select * from words'
        rows = self.query(select_sql)
        for (sid, sentence, author, source, count) in rows:
            print('SID:{}  Sentence:{}  Author:{} Source:{}  Count:{} '.format(sid, sentence, author, source, count))

    def insertSentence(self, sentence, author, source):
        insert_sql = 'INSERT INTO words(sentence, author, source, count) VALUES (\'{}\', \'{}\', \'{}\', {})'
        result = self.update(insert_sql.format(sentence, author, source, 0))
        return result

    def __del__(self):
        self.connect.close()
