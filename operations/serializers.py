from rest_framework import serializers
from .models import Table, Reservation, Order, OrderItem


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'number', 'capacity', 'status', 'zone']


class OrderItemSerializer(serializers.ModelSerializer):
    menu_item_name = serializers.CharField(source='menu_item.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'menu_item_name', 'quantity', 
                'unit_price', 'status', 'note', 'subtotal']
        read_only_fields = ['subtotal']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    table_number = serializers.CharField(source='table.number', read_only=True)
    customer_name = serializers.CharField(source='customers.name', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'table', 'table_number', 'customers', 'customer_name', 
                'status', 'payment_method', 'discount', 'note', 'items',
                'subtotal', 'total', 'created_at', 'updated_at', 'paid_at',]
        read_only_fields = ['subtotal', 'total', 'created_at', 'updated_at']


class ReservationSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customers.name', read_only=True)
    table_number = serializers.CharField(source='table.number', read_only=True)

    class Meta:
        model = Reservation
        fields = ['id', 'customers', 'customer_name', 'table', 'table_number', 
                'party_size', 'reservation_date', 'reservation_time', 'status', 
                'note', 'created_at']
        read_only_fields = ['created_at']
