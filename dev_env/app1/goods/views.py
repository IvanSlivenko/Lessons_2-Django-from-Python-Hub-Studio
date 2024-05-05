from django.shortcuts import render

# Create your views here.

# import http
# from turtle import title
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Products



def catalog(request, category_slug):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:    
        goods = Products.objects.filter(category__slug=category_slug)
    
    context = {
        "title": "Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


# def product(request, product_slug=False, product_id=False):
def product(request, product_slug ):
    

    # if product_id:
    #     product = Products.objects.get(id=product_id)
    # else:
        # product = Products.objects.get(slug=product_slug)
    product = Products.objects.get(slug=product_slug)
    
    context = {
        "title": "Product",
        "product": product,
    } 

    

    return render(request, "goods/product.html", context=context)
