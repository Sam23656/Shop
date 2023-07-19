from django.urls import path, include
from Buyer.views import show_index_page, show_product_page

urlpatterns = [
    path('', show_index_page),
    path('product/<int:id>', show_product_page)
]
