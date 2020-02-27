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
    res = JsonResponse({"ok": True})
    update = telebot.types.Update.de_json(data)
    message = update.message
    user_id = message.from_user.id
    username = message.from_user.username

    try:
        user = TelegramUser.objects.get(id=user_id)
    except TelegramUser.DoesNotExist:
        user = None

    if not user:
        user = TelegramUser.objects.create(id=user_id, username=username, is_admin=admin_id == user_id)

    msg = f'user - {user.id}\n' \
          f'update_id - {update.update_id}\n' \
          f'from_user - {message.from_user.id}\n' \
          f'username - {message.from_user.username}\n\n' \
          f'content_type - {message.content_type}\n' \
          f'{message.text}'
    if user.is_admin:
        msg += '\nАдмин!'
    if user.is_allowed:
        msg += '\nДопущен!'

    bot.reply_to(message, msg)

    # send_message_to_admin(msg)
    return res


def send_message_to_admin(msg):
    bot.send_message(admin_id, msg)


bot.delete_webhook()
bot.set_webhook(WEBHOOK_URL)
