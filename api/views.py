from rest_framework import viewsets
from api.serializers import CustomerSerializer
from customer.models import Customer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

# class CustomerViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

class CustomerList(generics.ListCreateAPIView):
    #queryset = Product.objects.all()
    serializer_class = CustomerSerializer
    lookup_url_kwarg = 'line_id'

    def get_queryset(self):
        queryset = Customer.objects.all()
        name = self.request.query_params.get('line_id', None)
        if name is not None:
            queryset = queryset.filter(line_id=name) 
        return queryset
      
