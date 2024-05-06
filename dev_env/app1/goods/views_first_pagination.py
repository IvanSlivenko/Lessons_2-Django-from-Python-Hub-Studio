from django.shortcuts import get_object_or_404, get_list_or_404, render

# Create your views here.

# import http
# from turtle import title
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from goods.models import Products



def catalog(request, category_slug, page=1):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:    
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
        

    paginator = Paginator(goods, 3)
    current_page= paginator.page(page)
    
    context = {
        "title": "Каталог",
        "goods": current_page,
        "slug_url" : category_slug
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
