import logging

from telegram import Bot

from .bot_config import BOT_TOKEN, WEBHOOK_URL

bot = Bot(BOT_TOKEN)

bot.delete_webhook()
bot.set_webhook(WEBHOOK_URL)

logging.basicConfig(level=logging.INFO)


