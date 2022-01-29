from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


@api_view(["GET"])
def product_List(request):
    products = Product.objects.all()
    products_serialize = ProductSerializer(products, many=True)
    return Response(products_serialize.data)

@api_view(["GET"])
def product_Details(request,pk):
    product = Product.objects.get(id=pk)
    product_serialize = ProductSerializer(product, many=False)
    return Response(product_serialize.data)

@api_view(["POST"])
def product_Save(request):
    product=ProductSerializer(data=request.data)

    if product.is_valid():
        product.save()

    return Response(product.data)


@api_view(["POST"])
def product_Update(request,pk):
    instance=Product.objects.get(id=pk)
    product=ProductSerializer(instance=instance,data=request.data)

    if product.is_valid():
        product.save()

    return Response(product.data)


@api_view(["DELETE"])
def product_Delete(request,pk):
    instance=Product.objects.get(id=pk)
    instance.delete()

    return Response("Product Deleted!")
