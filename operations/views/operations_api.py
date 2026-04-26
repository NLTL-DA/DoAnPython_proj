from rest_framework import viewsets
from ..models import Table, Reservation, Order, OrderItem
from ..serializers import TableSerializer, ReservationSerializer, OrderSerializer, OrderItemSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    filterset_fields = ['status', 'zone', 'capacity']


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filterset_fields = ['status', 'customer', 'reservation_date']
    ordering_fields = ['reservation_date', 'reservation_time']
    ordering = ['reservation_date', 'reservation_time']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_fields = ['status', 'table', 'customer']
    ordering_fields = ['created_at', 'total']
    ordering = ['-created_at']

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filterset_fields = ['order', 'status']
