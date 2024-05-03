from django.shortcuts import render

# Create your views here.

# import http
# from turtle import title
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Products



def catalog(request):

    goods = Products.objects.all()
    
    context = {
        "title": "Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    context = {
        "title": "Product",
    }
    return render(request, "goods/product.html", context)
