from django.urls import path

from .views import OSKView

app_name = 'osk'

urlpatterns = [
    path('', OSKView.as_view(), name='index'),
]
