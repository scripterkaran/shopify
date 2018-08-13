from django.urls import path

from shop.views import (
    ProductList,
    ProductDetail)

urlpatterns = [
    path("products/", view=ProductList.as_view(), name="list"),
    path("products/<int:id>/", view=ProductDetail.as_view(), name="product-detail"),
]
