from telethon.sync import TelegramClient, events
from datetime import date, timedelta
import datetime
import schedule
import time
import pandas as pd
import configparser
import json
import asyncio
import re

config = configparser.ConfigParser()
config.read("config.ini")

api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

client = TelegramClient(username, api_id, api_hash, system_version='4.16.30-vxCUSTOM')
client.start()
print(client.get_me())

def time_now():
  current_time = datetime.datetime.now().time()
  current_hour = current_time.hour
  current_minute = current_time.minute
  time_now = f'{current_hour}:{current_minute}'
  return time_now

def parcer_chats():
  chats = ['https://t.me/chat_1', 'https://t.me/chat_2', 'https://t.me/chat_3', 'https://t.me/chat_4', 'https://t.me/chat_5']
  date_message = date.today() - timedelta(days=1)

  for chat in chats:
    part_mes= client.get_messages(chat, limit = 2000)

    for message in part_mes:
      if message.text:
        if re.search('(\s|\A)[LlЛл][DdДд](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Кк][Рр][Аа][Нн](\s|\Z|[^a-zA-Zа-ъА-Ъь-яЬ-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Шш][Аа][Рр][Оо][Вв][Оо][Йй](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Шш][Аа][Рр][Оо][Вв][Ыы][Йй](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Bb][Uu][Gg][Aa][Tt][Tt][Ii](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Бб][Уу][Гг][Аа][Тт]{1,2}[Ии](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Gg][Ii][Aa][Cc][Oo][Mm]{1,2}[Ii][Nn][Ii](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Лл][Аа][Тт][Уу][Нн][Нн][Ыы][Йй](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Лл][Оо][Пп][Нн][Уу][Лл](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Тт][Рр][Ее][Сс][Нн][Уу][Лл](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Зз][Аа][Тт][Оо][Пп][Ии][Лл](\s|\Z|[^a-zA-Zа-нА-Нп-яП-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[GgГг][IiИи][DdДд][RrРр][OoОо][LlЛл][OoОо][CcКк](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Аа][Кк][Вв][Аа][Сс][Тт][Оо][Рр][Оо][Жж](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Пп][Рр][Аа][Йй][Дд](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Pp][Rr][Ii][Dd][Ee](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Чч][Сс][Гг][Сс](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Чч][Фф][Зз](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Чч][Ее][Лл][Яя][Бб][Ии][Нн][Сс][Кк](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Фф][Ии][Тт][Ии][Нн][Гг](\s|\Z|[^a-zA-Zа-зА-зй-яЙ-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Гг][Аа][Лл]{1,2}[Оо][Пп](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Бб][Аа][Зз](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Бб][Оо][Лл][Оо][Гг][Оо][Ее](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Вв][Аа][Лл][Фф][ЕеЭэ][Кк][Сс](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Vv][Aa][Ll][Ff][Ee][Kk][Cc](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Вв][Аа][Фф][Лл][Ее][Кк][Сс](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Аа][Кк][Вв][Аа][Сс][Фф][Ее][Рр][Аа](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[Aa][Qq][Uu][Aa][Ss][Ff][Ee][Rr][Aa](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[IiИи][TtТт][AaАа][PpПп](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message or re.search('(\s|\A)[DdДд][IiИи][CcСс][TtТт](\s|\Z|[^a-zA-Zа-яА-Я0-9])', message.text) and message.date.date() == date_message:
          client.send_message('https://t.me/parcer_chat_tdld', f'<a href={chat}>{message.chat.title}</a>', parse_mode = 'HTML')
          client.send_message('https://t.me/parcer_chat_tdld', str(message.date))
          message.forward_to('https://t.me/parcer_chat_tdld')
          client.send_message('https://t.me/parcer_chat_tdld', '-----------------------')

while True:
  if time_now() in ['7:00']:
    parcer_chats()
    time.sleep(60)