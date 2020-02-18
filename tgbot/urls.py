from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import TelegramBotView

app_name = 'tg_bot'

urlpatterns = [
    path('', csrf_exempt(TelegramBotView.as_view()), name='index'),
]
