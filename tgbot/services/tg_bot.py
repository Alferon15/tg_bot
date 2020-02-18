import logging

from telegram import Bot, Update, Message

from .bot_config import BOT_TOKEN, WEBHOOK_URL, admin_id

bot = Bot(BOT_TOKEN)

bot.delete_webhook()
bot.set_webhook(WEBHOOK_URL)

logging.basicConfig(level=logging.INFO)


def process_request(data):
    pass


def parse_updates(data):
    update = data
    msg = update

    send_message_to_admin(f'---\n{msg}\n---')


def send_message_to_admin(msg):
    bot.send_message(admin_id, msg)
