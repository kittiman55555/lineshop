from rest_framework import viewsets
from api.serializers import CustomerSerializer, ProductSerializer, CategorySerializer, OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from product.models import Product
from customer.models import Customer
from categories.models import Category
from orders.models import Order

# class CustomerList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = CustomerSerializer
    
#     lookup_url_kwarg = 'line_id'

#     def get_queryset(self):
#         queryset = Customer.objects.all()
#         name = self.request.query_params.get('line_id', None)
#         if name is not None:
#             queryset = queryset.filter(line_id=name) 
#         return queryset
      
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def get_queryset(self):
        queryset = Product.objects.all()
        cat_name = self.request.query_params.get('cat', None)
        print(cat_name)
        if cat_name is not None:
            #Article.objects.filter(categories__in = preference.categories.all())
            queryset = queryset.filter(categories__name=cat_name)
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer