from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings import SHOP_API_URL
from orders.models import Order
from orders.serializers import OrderSerializer
from rest_framework import status


class OrderList(APIView):
    url = "{}/{}.json".format(SHOP_API_URL, "orders")

    def get(self, request, *args, **kwargs):
        user = request.user
        query = Order.objects.filter(user=user)
        serializer = OrderSerializer(query, many=True, context=self.get_renderer_context())
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        user = request.user
        items = request.data.get('items')
        shopify_json = Order.create_order_schema(items)
        response = requests.post(self.url, json=shopify_json)
        order = Order.objects.create(user=user, json_received=response.text)
        # order.addItems(response.text)
        return Response(response.json())


class UserOrderView(APIView):

    def get(self, request, *args, **kwargs):
        orders = request.user.get_orders()
        return Response(OrderSerializer(orders, many=True).data)
