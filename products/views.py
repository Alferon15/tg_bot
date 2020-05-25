from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView


class ProductIndexView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
