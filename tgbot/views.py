import time

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from .services.tg_bot import send_message_to_admin, process_updates


class TelegramBotView(View):
    def get(self, request):
        send_message_to_admin('Страница бота посещена!!!')
        return JsonResponse({"ok": True})

    def post(self, request):
        json_string = request.read().decode('utf-8')
        return process_updates(json_string)
