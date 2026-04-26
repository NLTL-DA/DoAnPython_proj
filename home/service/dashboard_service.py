# home/dashboard_service.py
from operations.models import Order, Table
from django.utils import timezone

def get_dashboard_data():
    now = timezone.now()
    first_day = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    
    monthly_orders = Order.objects.filter(created_at__gte=first_day)
    total_orders = monthly_orders.count()
    total_revenue = sum(order.total() for order in monthly_orders)
    total_tables = Table.objects.count()
    occupied_tables = Table.objects.filter(status='available').count()

    return {
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'total_tables': total_tables,
        'occupied_tables': occupied_tables,
    }