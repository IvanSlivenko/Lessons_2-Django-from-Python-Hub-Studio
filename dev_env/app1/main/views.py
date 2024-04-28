# import http
# from turtle import title
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('Home page')
    context={
        'title': 'Home',
        'content':'Головна сторінка магазину - HOME',
        'list':['fsrst','second'],
        'dict':{'first':1},
        'is_authenticated': False 
    }
    return render(request, 'main/index.html', context)

def about(request):
    # return HttpResponse('About page')
    context={
        'title': 'Про нас',
        'content':' Тут буде написано текст про нас'    
        }
    return render(request,'main/about.html', context)

