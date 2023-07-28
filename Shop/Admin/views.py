from django.shortcuts import render, get_object_or_404, redirect
from Admin.forms import ProductEditModelForm, ProductAddModelForm
from Admin.models import Product


# Create your views here.

def show_index_page(request):
    context = {"Products": Product.objects.all()}
    return render(request, "admin_index.html", context=context)


def show_product_edit_page(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductEditModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_index')
    else:
        form = ProductEditModelForm(instance=product)

    context = {"Product": form, "form": ProductEditModelForm(instance=product)}
    return render(request, "Edit.html", context=context)


def show_delete_page(request, pk):
    Product.objects.get(pk=pk).delete()
    return redirect("admin_index")


def show_add_page(request):

    if request.method == 'POST':
        form = ProductAddModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_index')
    else:
        form = ProductAddModelForm()
    context = {"form": form}
    return render(request, "Add_Product.html", context=context)
