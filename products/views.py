from django.shortcuts import render
from products.models import *


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    # print(request.session.session_key)
    title = product.name
    properties = product.description.split('\n')
    return render(request, 'products/product.html', locals())


def home(request):
    products = Product.objects.filter(is_active=True)
    title = 'Home'
    return render(request, 'products/index.html', locals())