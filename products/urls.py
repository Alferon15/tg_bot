from django.urls import path
from .views import ProductIndexView

app_name = 'products'

urlpatterns = [
    path('', ProductIndexView.as_view(), name='index'),
]
