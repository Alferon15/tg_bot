from django.contrib.auth.models import User
from django.db import models


class TelegramUser(models.Model):
    class Meta:
        verbose_name = 'Пользователь Телеграм'
        verbose_name_plural = 'Пользователи Телеграм'

    id = models.PositiveIntegerField(verbose_name='Telegram ID', primary_key=True)
    username = models.CharField(verbose_name='Имя пользователя Telegram', max_length=50)
    is_admin = models.BooleanField(verbose_name='Админ?', default=False, null=False)
    is_allowed = models.BooleanField(verbose_name='Допущен?', default=False, null=False)
