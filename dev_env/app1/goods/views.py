from django.shortcuts import render

# Create your views here.

# import http
# from turtle import title
from django.http import HttpResponse
from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Каталог",
        "goods": [
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Чайний столик та три стільця",
                "description": "Комплект з трьох стільців та дизайнерский столик для вітальні.",
                "price": 150.00,
            },
            {
                "image": "deps/images/goods/set of tea table and two chairs.jpg",
                "name": "Чайный столик та два стільця",
                "description": "Набір -  стіл та два стільці в мінімалістичному  стилі.",
                "price": 93.00,
            },
            {
                "image": "deps/images/goods/double bed.jpg",
                "name": "Двухспальне ліжко",
                "description": "Ліжко двухспальная з надголовником ортопедична.",
                "price": 670.00,
            },
            {
                "image": "deps/images/goods/kitchen table.jpg",
                "name": "Кухонний стіл з раковиною",
                "description": "Кухонний стіл з вбудованою раковиною та стільцями.",
                "price": 365.00,
            },
            {
                "image": "deps/images/goods/kitchen table 2.jpg",
                "name": "Кухонний стіл з вбудованою раковиною",
                "description": "Кухонный стол з вбудованою плитою та раковиною.",
                "price": 430.00,
            },
            {
                "image": "deps/images/goods/corner sofa.jpg",
                "name": "Кутовий диван для вітальні",
                "description": "Кутовий диван для затишної вітальні",
                "price": 610.00,
            },
            {
                "image": "deps/images/goods/bedside table.jpg",
                "name": "Приліжковий столик",
                "description": "Приліжковий столик з двома висувними ящиками.",
                "price": 55.00,
            },
            {
                "image": "deps/images/goods/sofa.jpg",
                "name": "Диван звичайний",
                "description": "Диван, він же софа звичайна.",
                "price": 190.00,
            },
            {
                "image": "deps/images/goods/office chair.jpg",
                "name": "Стілець офісний",
                "description": "Зручний стілець офісний ",
                "price": 30.00,
            },
            {
                "image": "deps/images/goods/plants.jpg",
                "name": "Рослина",
                "description": "Рослина для інтер'єру.",
                "price": 10.00,
            },
            {
                "image": "deps/images/goods/flower.jpg",
                "name": "Квітка стилізована",
                "description": "Дизайнерська квітка для створення затишку в інтер'єрі.",
                "price": 15.00,
            },
            {
                "image": "deps/images/goods/strange table.jpg",
                "name": "Приліжковий столик",
                "description": "Столик для спальні.",
                "price": 25.00,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    context = {
        "title": "Product",
    }
    return render(request, "goods/product.html", context)
