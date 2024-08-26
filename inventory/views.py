# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import *
# from rest_framework import status
# from .serializers import *
# class productView(APIView):
#     def get(self, request):
#         products = product.objects.all()
#         product_data=[]
#         for i in products:
#             single_p={
#                 "id":i.id,
#                 "product_name":i.product_name,
#                 "product_price":i.product_price
#             }
#             product_data.append(single_p)
#         return Response(product_data)
#     def post(self, request):
#         product_name = request.data.get('product_name')
#         product_price = request.data.get('product_price')

#         if product_name and product_price:
#             new_product = product(
#                 product_name=product_name,
#                 product_price=product_price
#             )
#             new_product.save()
#             return Response({"message": "Data saved successfully"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"error": "Missing data"}, status=status.HTTP_400_BAD_REQUEST)
        
# class productViewID(APIView):
#     def get(self,request,id):
#         product_id = product.objects.get(id=id)
#         single_p={
#                 "id":product_id.id,
#                 "product_name":product_id.product_name,
#                 "product_price":product_id.product_price
#             }
#         return Response(single_p) 
#     def patch(self, request, id):
#         try:
#             product_instance = product.objects.get(id=id)
#             product_name = request.data.get('product_name', product_instance.product_name)
#             product_price = request.data.get('product_price', product_instance.product_price)

#             product_instance.product_name = product_name
#             product_instance.product_price = product_price
#             product_instance.save()

#             return Response({
#                 "id": product_instance.id,
#                 "product_name": product_instance.product_name,
#                 "product_price": product_instance.product_price
#             }, status=status.HTTP_200_OK)
#         except product.DoesNotExist:
#             return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, id):
#         try:
#             product_instance = product.objects.get(id=id)
#             product_instance.delete()
#             return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
#         except product.DoesNotExist:
#             return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductView(APIView):
    @swagger_auto_schema(
        request_body=ProductSerializer,
        responses={201: ProductSerializer, 400: 'Bad Request'}
    )
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        responses={200: ProductSerializer(many=True), 400: 'Bad Request'}
    )
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductViewID(APIView):
    @swagger_auto_schema(
        responses={200: ProductSerializer, 404: 'Product not found'}
    )
    def get(self, request, id):
        try:
            product_instance = Product.objects.get(id=id)
            serializer = ProductSerializer(product_instance)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=ProductSerializer,
        responses={200: ProductSerializer, 400: 'Bad Request', 404: 'Product not found'}
    )
    def patch(self, request, id):
        try:
            product_instance = Product.objects.get(id=id)
            serializer = ProductSerializer(product_instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        responses={204: 'Product deleted successfully', 404: 'Product not found'}
    )
    def delete(self, request, id):
        try:
            product_instance = Product.objects.get(id=id)
            product_instance.delete()
            return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
