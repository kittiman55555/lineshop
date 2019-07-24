from rest_framework import viewsets
from api.serializers import CustomerSerializer
from customer.models import Customer
from rest_framework.views import APIView
from rest_framework.response import Response



class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request, *args, **kwargs):
        customer =  Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)