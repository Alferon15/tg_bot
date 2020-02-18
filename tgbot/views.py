from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from .services.tg_bot import *


class TelegramBotView(View):
    def get(self, request):
        bot.send_message(100204219, 'GET')
        return JsonResponse({"ok": "GET request processed"})

    def post(self, request):
        bot.send_message(100204219, 'POST')
        return JsonResponse({"ok": "POST request processed"})
