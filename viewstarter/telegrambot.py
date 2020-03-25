from threading import Thread

import win32gui
from mouseControl import windowRef
import telepot

TOKEN = '1135370561:AAFFU02DMWZcpsXW1kB5Wm9j-THnzDM9Pwg'
bot = telepot.Bot(TOKEN)


def getTitle ():
    windowRef()
    w = win32gui
    w.GetWindowText(w.GetForegroundWindow())
    return str(w.GetWindowText(w.GetForegroundWindow()))


def on_chat_message (msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        name = msg["from"]["first_name"]
        txt = msg['text']
        if txt == '/start'or'/Start':
            bot.sendMessage(chat_id, 'ciao %s, sono al tuo servizio!' %name)
            bot.sendMessage(chat_id, 'Digita /stats per tutte le info')
        if txt == '/stats'or'/Stats':
            bot.sendMessage(chat_id, getTitle())
        else:
            bot.sendMessage(chat_id, 'Ei %s sei proprio un coglione, controlla linput' %name)


t = Thread(target=bot.message_loop(on_chat_message))
