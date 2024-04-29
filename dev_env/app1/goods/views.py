from django.shortcuts import render

# Create your views here.

# import http
# from turtle import title
from django.http import HttpResponse
from django.shortcuts import render

def catalog(request): 
    context={
        'title': 'Каталог',
        

    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    context={
        'title': 'Product',
        

    }
    return render(request, 'goods/product.html', context)

