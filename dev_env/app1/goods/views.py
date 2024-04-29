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
                "name": "Угловой диван для гостинной",
                "description": "Угловой диван, раскладывается в двухспальную кровать, для гостинной и приема гостей самое то!",
                "price": 610.00,
            },
            {
                "image": "deps/images/goods/bedside table.jpg",
                "name": "Прикроватный столик",
                "description": "Прикроватный столик с двумя выдвижными ящиками (цветок не входит в комплект).",
                "price": 55.00,
            },
            {
                "image": "deps/images/goods/sofa.jpg",
                "name": "Диван обыкновенный",
                "description": "Диван, он же софа обыкновенная, ничего примечательного для описания.",
                "price": 190.00,
            },
            {
                "image": "deps/images/goods/office chair.jpg",
                "name": "Стул офисный",
                "description": "Описание товара, про то какой он классный, но это стул, что тут сказать...",
                "price": 30.00,
            },
            {
                "image": "deps/images/goods/plants.jpg",
                "name": "Растение",
                "description": "Растение для украшения вашего интерьера подарит свежесть и безмятежность обстановке.",
                "price": 10.00,
            },
            {
                "image": "deps/images/goods/flower.jpg",
                "name": "Цветок стилизированный",
                "description": "Дизайнерский цветок (возможно искусственный) для украшения интерьера.",
                "price": 15.00,
            },
            {
                "image": "deps/images/goods/strange table.jpg",
                "name": "Прикроватный столик",
                "description": "Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.",
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
