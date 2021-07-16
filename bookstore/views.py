from django.shortcuts import render
from .models import Book

# Create your views here.
def bookstore_book(request):
    book = Book.objects.all()
    context = {
        'bookstore_list' :book
    }
    return render(request, "bookstore_list.html", context)

def shopping_cart(request):
    context = {}
    return render(request, 'shopping_cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'shopping_cart.html', context)