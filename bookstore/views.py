from django.shortcuts import get_object_or_404, render, redirect
from .models import Book
from bookstoreSite.forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

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

# Register
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('/index/')
        messages.error(request, "Unsuccessful registration. Invalid information")
    form = NewUserForm()
    return render(request, 'register.html', context={"register_form":form})



# Shopping cart
def shopping_cart(request):
    context = {}
    return render(request, 'shopping_cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'shopping_cart.html', context)