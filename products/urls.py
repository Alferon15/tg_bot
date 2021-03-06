from django.urls import path
from .views import ProductIndexView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', ProductIndexView.as_view(), name='index'),
    path('<int:pk>', ProductDetailView.as_view(), name='detail'),
]
