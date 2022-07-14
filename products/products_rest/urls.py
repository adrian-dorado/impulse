from django.urls import path

from .views import (
    api_product_category,
    api_product,
    api_clothing_inventory,
)

urlpatterns = [
    path("product_categories/", api_product_category, name="api_product_category"),
    path("products/", api_product, name="api_product"),
    path("clothing_inventory/", api_clothing_inventory, name="api_clothing_inventory"),
]