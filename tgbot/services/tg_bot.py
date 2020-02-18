import logging

from telegram import Bot
from telegram.ext import Updater

from .bot_config import BOT_TOKEN, WEBHOOK_URL

bot = Bot(BOT_TOKEN)

bot.set_webhook(WEBHOOK_URL)

logging.basicConfig(level=logging.INFO)
