# -*- coding: utf-8 -*-
import redis
import os
import telebot
import random
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
chatlist = list()
with open("chatline.txt", "r", encoding="utf-8") as lines:
	for line in lines:
		chatlist.append(line)
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis

#       Your bot code below
bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	x = random.choice(chatlist)
	print("who : "+ message.from_user.username+"said : "+message.text+"reply :" +x)
	bot.reply_to(message, x)

bot.polling()