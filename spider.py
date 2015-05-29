# -*- coding: utf-8 -*-
__author__ = 'PlayJokes'

import urllib.request
import re
import sentence_manager

def getHtml(url):
    req = urllib.request.Request(url)
    try:
        data = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(e.code)
    data = data.read().decode('utf8')
    return data

def oneProcess():
    db = sentence_manager.SentenceManager("text")
    site = 'http://wufazhuce.com/one/vol.'
    pattern = re.compile('<div class="one-cita">([\s\S]*?)</div>')

    for i in range (1, 965):
        content = getHtml(site + str(i))
        sentence = pattern.search(content).group(1).strip()
        if sentence.find('by') > 0:
            tmp = sentence.split('by')
            db.insertSentence(tmp[0], tmp[1], None)
        elif sentence.find('from') > 0:
            tmp = sentence.split('from')
            db.insertSentence(tmp[0], None, tmp[1])
        else:
            db.insertSentence(tmp[0], None, None)
        print(i)


if __name__ == '__main__':
    oneProcess()