from django.urls import path

from myapp.views import product_List, product_Details, product_Save, product_Update, product_Delete

urlpatterns = [
    path("product_list", product_List),
    path("product_details/<pk>", product_Details),
    path("product_save", product_Save),
    path("product_update/<pk>", product_Update),
    path("product_delete/<pk>", product_Delete),
]