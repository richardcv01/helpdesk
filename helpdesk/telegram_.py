import logging

from aiogram import Bot, Dispatcher, executor, types, filters
#from .REQUEST import GET_tikets, UPDATE_tikets, get_id_user
import re

#from .REQUEST import GET_tikets, UPDATE_tikets, get_id_user, get_stan_tiket
import asyncio
from asgiref.sync import async_to_sync
#API_TOKEN = '5541780288:AAFDKbfLXfkuhDqY0wWHfdlx8WqlG-c3SWA'





import telebot

API_TOKEN = '5541780288:AAFDKbfLXfkuhDqY0wWHfdlx8WqlG-c3SWA'
GROUP_ID = -680022832
tBot = telebot.TeleBot(API_TOKEN)


#@tBot.message_handler(regexp = "^\\+\\ ([0-9]+)$")
#def func_viko( message):
   # first_name = message.from_user.first_name
   # print("start BOT")
    # if not user_name:
   #    #global user_name
   # user_name = message.from_user.first_name
   # tBot.send_message(GROUP_ID, user_name)

#@tBot.message_handler(content_types=['new_chat_members'])
#def welcome_new_member(message):
    #first_name = message.json['new_chat_member']['first_name']
   # Создайте пользователя и сохраните его в базе данных
    #tBot.send_message(GROUP_ID, message)
    #print(first_name)
    #user = User.objects.create_user(username=first_name, password = 'Dbr202020')
    #tBot.send_message(GROUP_ID, first_name + ' Вітаю в чаті')
    #MypyBot.send_message(GROUP_ID, user_name)


def send_(message):
    tBot.send_message(GROUP_ID, message)

#send_('sdadas')

#tBot.infinity_polling()