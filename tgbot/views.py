from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

# from .services.tg_bot import send_message_to_admin, process_updates


class TelegramBotView(View):
    def get(self, request):
        send_message_to_admin('Главная страница посещена!')
        return JsonResponse({"ok": "GET request processed"})

    def post(self, request):
        json_string = request.read().decode('utf-8')
        process_updates(json_string)
        return JsonResponse({"ok": "POST request processed"})


import logging

import telebot

from tgbot.services.bot_config import BOT_TOKEN, WEBHOOK_URL, admin_id

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(BOT_TOKEN)

logging.basicConfig(level=logging.INFO)


def process_updates(data):
    update = telebot.types.Update.de_json(data)
    bot.process_new_updates({update})
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
    print('send_welcome')
    bot.reply_to(message,
                 ("Привет, я бот\n"
                  "Я ничего не умею!"))


bot.delete_webhook()
bot.set_webhook(WEBHOOK_URL)
