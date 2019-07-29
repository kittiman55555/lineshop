from rest_framework import serializers
from customer.models import Customer
from rest_framework.response import Response
from django.http import JsonResponse


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



