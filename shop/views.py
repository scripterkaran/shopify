from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings import SHOP_API_URL


class SPAIndex(View):

    def get(self, request):
        if request.user.is_anonymous:
            return HttpResponseRedirect('/accounts/login/')
        return render(request, template_name='shop-index-spa.html')


class ProductList(APIView):
    url = "{}/{}.json".format(SHOP_API_URL, "products")

    def get(self, request, *args, **kwargs):
        response = requests.get(self.url)
        return Response(response.json())


class ProductDetail(APIView):

    def get(self, request, *args, **kwargs):
        url = "{}/{}/{}.json".format(SHOP_API_URL, "products", kwargs.get('id'))
        response = requests.get(url)
        return Response(response.json())
