from django.shortcuts import render
from Admin.models import Product


# Create your views here.


def show_index_page(request):
    context = {"Products": Product.objects.all()}
    return render(request, "index.html", context=context)

def show_product_page(request, id):
    context = {"Product": Product.objects.get(pk=id)}
    return render(request, "Product.html", context=context)