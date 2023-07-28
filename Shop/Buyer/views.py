from django.shortcuts import render, redirect
from django.urls import reverse
from Admin.models import Product
from datetime import date

# Create your views here.


def show_index_page(request):
    context = {"Products": Product.objects.all()}
    return render(request, "index.html", context=context)


def show_product_page(request, pk):
    if request.method == "POST":
        product = Product.objects.get(pk=pk)
        product.Status = "false"
        product.Date = date.today()
        product.save()
        return redirect("index")
    context = {"Product": Product.objects.get(pk=pk)}
    return render(request, "Product.html", context=context)
