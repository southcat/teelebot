# -*- coding:utf-8 -*-
from teelebot import Bot

def Hello(message):
    #print("你好,世界!")
    bot = Bot()
    status = bot.sendPhoto(message["chat"]["id"], bot.plugin_dir + "Hello/helloworld.png")