from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from .services.tg_bot import *


class TelegramBotView(View):
    def get(self, request):
        bot.send_message(100204219, 'Главная страница посещена!')
        return JsonResponse({"ok": "GET request processed"})

    def post(self, request):
        msg = request
        bot.send_message(100204219, msg.method)
        bot.send_message(100204219, msg.body)
        bot.send_message(100204219, msg.POST)
        return JsonResponse({"ok": "POST request processed"})
