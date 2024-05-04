# import http
# from turtle import title
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):
    # return HttpResponse('Home page')

    # categories= Categories.objects.all()

    



    context={
        'title': 'Home  - Головна',
        'content': 'Магазин меблів HOME',
        # 'categories': categories
    }
    return render(request, 'main/index.html', context)

def about(request):
    # return HttpResponse('About page')
    context={
        'title': 'Home - Про нас',
        'content':'Про нас',
        'text_on_page': 'Детальний  текст про нас', 
        }
    return render(request,'main/about.html', context)

def test(request):
    # return HttpResponse('About page')
    context={
        'title': 'test',
        'content':'test',
        'text_on_page': 'test test test', 
        }
    return render(request,'main/test.html', context)

