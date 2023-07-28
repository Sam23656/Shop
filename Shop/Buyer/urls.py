from django.urls import path, include
from Buyer.views import show_product_page, show_index_page

urlpatterns = [
    path('', show_index_page, name="index"),
    path('product/<int:pk>', show_product_page, name="product_name")
]
