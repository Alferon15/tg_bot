from django.shortcuts import render
from .models import Product
from django.views.generic import ListView


class ProductIndexView(ListView):
    model = Product
