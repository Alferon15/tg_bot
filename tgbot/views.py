from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from .services.tg_bot import send_message_to_admin, parse_updates


class TelegramBotView(View):
    def get(self, request):
        send_message_to_admin('Главная страница посещена!')
        return JsonResponse({"ok": "GET request processed"})

    def post(self, request):
        json_string = request.get_data().decode('utf-8')
        parse_updates(json_string)
        return JsonResponse({"ok": "POST request processed"})
