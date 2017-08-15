#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from TwitterAPI import TwitterAPI

bot_directory = os.path.dirname(os.path.abspath(__file__))

BOT1_APP_KEY = ''
BOT1_APP_SECRET = ''
BOT1_OAUTH_TOKEN = ''
BOT1_OAUTH_TOKEN_SECRET = ''

bot1 = TwitterAPI(BOT1_APP_KEY, BOT1_APP_SECRET, BOT1_OAUTH_TOKEN, BOT1_OAUTH_TOKEN_SECRET)

f = open(os.path.join(bot_directory, 'diccionario.txt'), 'r')
palabra = f.readline().rstrip()
palabras = f.readlines()

if palabra is not None:

    print(palabra)

    r = bot1.request('statuses/update', {'status': palabra})

    for item in r.get_iterator():
        if 'text' in item:
            print(item['text'])
        elif 'message' in item:
            print ('%s (%d)' % (item['message'], item['code']))

    f = open(os.path.join(bot_directory, 'diccionario.txt'), 'w')
    f.writelines(palabras[0:])
    f.close()
