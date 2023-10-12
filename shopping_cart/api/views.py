from django.shortcuts import render
from django.http import JsonResponse

from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import CartItem

import json

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCart(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))

        p_name = data.get("product_name")
        p_price = data.get("product_price")
        p_quantity = data.get("product_quantity")

        product_data = {
            'product_name': p_name,
            'product_price': p_price,
            'product_quantity': p_quantity
        }

        cart_item = CartItem.objects.create(**product_data)

        data = {"message:": f"New Item added to Cart with Id: {cart_item.id}"}

        print(data)
        return JsonResponse(data, status=201)
    