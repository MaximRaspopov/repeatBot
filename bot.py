# -*- coding: utf-8 -*-

import requests
from time import sleep
import telegramBot
token = '690289812:AAHUXep5LlyqEPyMInufozj3feGQ54UHTzg' #токен

repeat_bot = telegramBot.teleBot(token)




def main():
    new_offset = None

    while True:
        repeat_bot.get_updates(new_offset)

        last_update = repeat_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        repeat_bot.send_message(last_chat_id, '*{} said: {}*'.format(last_chat_name, last_chat_text))

        new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()


