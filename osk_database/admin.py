from django.contrib import admin
from .models import ServiceCode


@admin.register(ServiceCode)
class ServiceCodeAdmin(admin.ModelAdmin):
    pass