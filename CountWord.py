#-*- coding:utf-8 -*-
__author__ = 'Defei'

import requests

def count_words_at_url(url):
    resp = requests.get(url)
    with open('demo.txt', 'a') as f:
        f.write("hello\n")
    return len(resp.text.split())

