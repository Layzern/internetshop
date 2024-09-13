from django.http import HttpResponse
from django.shortcuts import render

from .models import  Product, Review

# Create your views here.
def home(request):
    products = Product.objects.all()
    print(products)
    return render(request, "index.html", {
        'products': products
    })


def view_product(request, id):
    product = Product.objects.filter(id=id).first()

    if request.method == "POST":
        author = request.POST.get('author')
        rating = request.POST.get('rating')
        text = request.POST.get('text')
        review = Review(author=author, rating=int(rating), text=text, product=product)
        review.save()

    print(product.review_set.all)
    reviews = product.review_set.all()
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
       'product' : product,
       'reviews' : reviews,
    })

def payment(request):
    return render(request, 'payment.html')