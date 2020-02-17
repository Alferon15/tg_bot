from django.urls import path
from .views import TelegramBotView

app_name = 'tg_bot'

urlpatterns = [
    path('', TelegramBotView.as_view(), name='index'),
]
