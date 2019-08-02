from rest_framework import serializers
from rest_framework.response import Response
from django.http import JsonResponse
from customer.models import Customer
from product.models import Product
from categories.models import Category 
from orders.models import Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        line_id = validated_data.get('line_id', None)
        store_id = validated_data.get('store_id', None)
        customer_line = Customer.objects.filter(line_id=line_id, store_id=store_id).first()
        if customer_line is None:
            customer_line = Customer.objects.create(**validated_data)
        return customer_line


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    class Meta:
        model = Product
        fields =  '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

        print('999')

    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     cat_id = self.request.query_params.get('cat', None)
    #     print(cat_id)
    #     if cat_id is not None:
    #     queryset = queryset.filter(categories_id=cat_id)
    #     return queryset