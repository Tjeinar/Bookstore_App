from django.shortcuts import get_object_or_404, render
from .models import Book

# Create your views here.
def product(request):
    book = Book.objects.all()
    context = {
        'bookstore_list' :book
    }
    return render(request, "bookstore_list.html", context)

def product_details(request, id):
    product = get_object_or_404(Book, pk=id)
    context = {'product': product}
    return render(request, 'product_details.html', context)


def shopping_cart(request):
    context = {}
    return render(request, 'shopping_cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'shopping_cart.html', context)