import logging
import time

import telebot

from .bot_config import BOT_TOKEN, WEBHOOK_URL, admin_id


logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(BOT_TOKEN)

logging.basicConfig(level=logging.INFO)


def process_updates(data):
    update = telebot.types.Update.de_json(data)
    bot.process_new_updates([update])
    # send_message_to_admin(f'{update}')
    time.sleep(1)
    # send_message_to_admin('------')


def parse_updates(data):
    pass


def send_message_to_admin(msg):
    bot.send_message(admin_id, msg)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print('send_welcome')
    bot.reply_to(message,
                 ("Привет, я бот\n"
                  "Стартыыы!"))


@bot.message_handler(commands=['help'])
def send_welcome(message):
    print('send_welcome')
    bot.reply_to(message,
                 ("Привет, я бот\n"
                  "Помощь!"))


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, f'Ты написал:\n{message.text}')


bot.delete_webhook()
bot.set_webhook(WEBHOOK_URL)
