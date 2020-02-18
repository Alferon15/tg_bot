from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from .services.tg_bot import *


class TelegramBotView(View):
    def get(self, request):
        bot.send_message(100204219, 'Главная страница посещена!')
        bot.send_message(100204219, bot.get_webhook_info())
        return JsonResponse({"ok": "GET request processed"})

    def post(self, request):
        msg = str(request.POST.data)
        bot.send_message(100204219, msg)
        return JsonResponse({"ok": "POST request processed"})
