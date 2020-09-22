from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .services.load_data_from_file import load_data_from_file


class OSKView(View):
    def get(self, request):
        s = load_data_from_file()
        return JsonResponse({"ok": True, "str": s})