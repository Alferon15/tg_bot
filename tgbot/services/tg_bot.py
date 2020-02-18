import logging

from telegram import Bot
from telegram.ext import Updater

from .bot_config import BOT_TOKEN, WEBHOOK_URL, SECRET


updater = Updater(BOT_TOKEN)
updater.start_webhook(
    listen='0.0.0.0',
    port=80,
    url_path=SECRET,
    key='certificate/private.key',
    cert='certificate/cert.pem',
    webhook_url=WEBHOOK_URL
)

logging.basicConfig(level=logging.INFO)
