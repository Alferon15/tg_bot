import logging

import telebot

from .bot_config import BOT_TOKEN, WEBHOOK_URL, admin_id

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(BOT_TOKEN)

bot.delete_webhook()
bot.set_webhook(WEBHOOK_URL)

logging.basicConfig(level=logging.INFO)


def process_updates(data):
    update = telebot.types.Update.de_json(data)
    bot.process_new_updates([update])
    send_message_to_admin(f'---\n{update}\n---')


def parse_updates(data):
    update = telebot.types.Update.de_json(data)
    bot.process_new_updates([update])
    send_message_to_admin(f'---\n{update}\n---')
    send_message_to_admin('end')


def send_message_to_admin(msg):
    bot.send_message(admin_id, msg)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message,
                 ("Hi there, I am EchoBot.\n"
                  "I am here to echo your kind words back to you."))