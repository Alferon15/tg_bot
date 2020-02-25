import logging

from django.http import JsonResponse
import telebot

from .bot_config import BOT_TOKEN, WEBHOOK_URL, admin_id

from ..models import TelegramUser

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(BOT_TOKEN)

logging.basicConfig(level=logging.INFO)


def process_updates(data):
    update = telebot.types.Update.de_json(data)
    message = update.message
    user_id = message.from_user.id
    username = message.from_user.username

    if not TelegramUser.objects.get(user_id):
        TelegramUser.objects.create(user_id=user_id, username=username)

    msg = f'update_id - {update.update_id}\n' \
          f'from_user - {message.from_user.id}\n' \
          f'username - {message.from_user.username}\n\n' \
          f'content_type - {message.content_type}\n' \
          f'{message.text}'

    send_message_to_admin(msg)
    return JsonResponse({"ok": True})


def send_message_to_admin(msg):
    bot.send_message(admin_id, msg)


bot.delete_webhook()
bot.set_webhook(WEBHOOK_URL)
