from django.urls import path

from orders.views import (
    OrderList,
    UserOrderView)

urlpatterns = [
    path("orders/", view=OrderList.as_view(), name="list"),
    path("my-orders/", view=UserOrderView.as_view(), name="user-orders"),
]
