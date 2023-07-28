from django import forms
from Admin.models import Product


class ProductEditModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Name', 'Category', 'Price', 'Status', 'Date']


class ProductAddModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
