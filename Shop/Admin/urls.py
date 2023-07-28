from django.urls import path
from Admin.views import show_index_page, show_product_edit_page, show_delete_page, show_add_page

urlpatterns = [
    path('', show_index_page, name="admin_index"),
    path('edit/<int:pk>', show_product_edit_page, name="edit"),
    path('delete/<int:pk>', show_delete_page, name="delete"),
    path('add/', show_add_page, name="add")
]