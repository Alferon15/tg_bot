import logging

from telegram import Bot
from telegram.ext import Updater

from .bot_config import BOT_TOKEN, WEBHOOK_URL

bot = Bot(BOT_TOKEN)
updater = Updater(BOT_TOKEN)

bot.delete_webhook()
bot.set_webhook(WEBHOOK_URL)

updater.start_webhook(
    listen='0.0.0.0',
    port=80,
    webhook_url=WEBHOOK_URL
)
logging.basicConfig(level=logging.INFO)
