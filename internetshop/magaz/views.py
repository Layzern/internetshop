from django.http import HttpResponse
from django.shortcuts import render

from .models import  Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    print(products)
    return render(request, "index.html", {
        'products': products
    })


def view_product(request, id):
    product = Product.objects.filter(id=id).first()
    print(product.review_set.all)
    charTable = []

    characterstics = [
        [product.weight, 'Вес']
    ]

    if product.weight:
        charTable.append([
            'Вес',
            f'{product.weight} грамм'
        ])

    return  render(request, 'product.html', {
       'product' : product
    })