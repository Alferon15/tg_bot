import logging

from django.http import JsonResponse
import telebot

from .bot_config import BOT_TOKEN, WEBHOOK_URL, admin_id


logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(BOT_TOKEN)

logging.basicConfig(level=logging.INFO)


def process_updates(data):
    update = telebot.types.Update.de_json(data)
    send_message_to_admin(update)
    send_message_to_admin(update.message)
    return JsonResponse({"ok": True})


def send_message_to_admin(msg):
    bot.send_message(admin_id, msg)


bot.delete_webhook()
bot.set_webhook(WEBHOOK_URL)
