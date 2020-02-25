from django.contrib import admin
from .models import TelegramUser


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    fields = ['id', 'username', 'is_admin', 'is_allowed']
