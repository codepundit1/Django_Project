from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Category, Customer, Product, Order
from .forms import OrderForms

# Create your views here.
def index(request):

    # sql = select * from categories

    # orm -> object relational mapping

    categories = Category.objects.all()

    context = {
        "categories": categories,
    }

    return render(request, "index.html", context=context)

def about(request):
    return render(request, "about.html")

def orders(request):
    form = OrderForms()

    if request.method == "POST":
        form = OrderForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("orderlist")

    context = {
        "forms" : form
    }
    return render(request, "orders.html", context=context)

def orderlist(request):
    orderlists = Order.objects.all()

    context = {
        "orders" : orderlists,
    }

    return render(request, "orderlist.html", context=context)


