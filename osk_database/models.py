from django.db import models


class ServiceCode(models.Model):
    class Meta:
        verbose_name = 'ШК'
        verbose_name_plural = 'ШК'

    service_code = models.CharField(verbose_name='ШК СК', max_length=13, primary_key=True)
    status = models.CharField(verbose_name='Статус', max_length=30)
    org_owner = models.CharField(verbose_name='Подразделение-владелец', max_length=50)
    object_type = models.CharField(verbose_name='Тип объекта', max_length=30)
    address = models.CharField(verbose_name='Адрес', max_length=50)
    responsible = models.CharField(verbose_name='Ответственный', max_length=50)
    name_pc = models.CharField(verbose_name='Наименование ПК', max_length=50)
    level = models.CharField(verbose_name='Уровень обслуживания', max_length=50)
    category = models.CharField(verbose_name='Категория', max_length=50)
    model = models.CharField(verbose_name='Производитель модель', max_length=50)
    sn = models.CharField(verbose_name='Серийный номер', max_length=50)
    ais_tp = models.CharField(verbose_name='АИС ТП', max_length=50)
