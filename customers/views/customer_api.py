from rest_framework import viewsets
from ..models import Customer
from ..serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    search_fields = ['name', 'phone', 'email']
    filterset_fields = ['created_at']
