#import requests
#from .bot import bot, plag
from celery import shared_task
from .telegram_ import send_ #tBot #, GROUP_ID, start_t, stop_t, sen, ex, dp
from mmpy_bot import Bot, Settings
from .my_plugin import MyPlugin
import asyncio


plag = MyPlugin()
#plag.set_plug()

bot = Bot(
    settings=Settings(
        MATTERMOST_URL = "http://mattermost.dbr.gov.ua",
        MATTERMOST_PORT = 80,
        #BOT_TOKEN = "pn3pzam6bb8adrexymn8uhad3e",
        BOT_TOKEN = "q51dn8wnupgrbfw6iopqi34xcr",
        BOT_TEAM = "helpdesk_bot",
        SSL_VERIFY = False,
    ),  # Either specify your settings here or as environment variables.
    plugins=[plag],  # Add your own plugins here.
)


@shared_task
def add(x, y):
    a = x + y
    print(a)
    return a

#@shared_task
#def bot_run(tikets):
    #bot.run('tikets')


@shared_task
def bot_run(tiket):
    plag._text = tiket
    bot.plugins=[plag]
    print(bot.plugins[0]._text)
    if bot.running:
        bot.stop()
        print('STOP Bot')
    try:
       print('status bot', bot.running)
       #bot.run(tiket)
       bot.run()
       print('RUN Bot')
    except RuntimeError as E:
       print("ERROR = ", E)
    else:
        try:
            print('status bot', bot.running)
            #bot.run(tiket)
            bot.run()
            print('RUN Bot')
        except RuntimeError as E:
            print("ERROR ", E)


@shared_task
def bot_stop():
    if bot.running:
      bot.stop()
      print('STOP Bot')


#tel_bot = Tel_bot()

@shared_task
def tel_bot_start(message):
    #start_t(message)
    #start_bot_t()
    None

@shared_task
def tel_bot_stop():

    print('stop bot t')


@shared_task
def tel_bot_send(message):
    #tBot.send_message(GROUP_ID, message)
    send_(message)








