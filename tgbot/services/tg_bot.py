import logging

from telegram import Bot
from telegram.ext import Updater

from .bot_config import BOT_TOKEN, WEBHOOK_URL, SECRET

bot = Bot(BOT_TOKEN)

updater = Updater(BOT_TOKEN)
updater.start_webhook(
    listen='0.0.0.0',
    port=80,
    url_path=SECRET,
    key='certificate/private.key',
    cert='certificate/cert.pem',
    webhook_url=WEBHOOK_URL
)
updater.bot.set_webhook(WEBHOOK_URL, certificate='certificate/cert.pem')

logging.basicConfig(level=logging.INFO)
