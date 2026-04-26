from django.shortcuts import render
from .service.dashboard_service import get_dashboard_data
from operations.models import Order
def home_page(request):
    return render(request, "home.html")

def dashboard_view(request):
    output = get_dashboard_data()
    return render(request, 'dashboard.html', output)

def don_hang_view(request):
    search_query = request.GET.get('donhang', '')
    current_status = request.GET.get('status', 'all')
    orders = Order.objects.prefetch_related('items').all().order_by('-created_at')
    if current_status == 'open':
        orders = orders.filter(status='open')
    elif current_status == 'paid':
        orders = orders.filter(status='paid')
    if search_query:
        if search_query.isdigit(): 
            orders = orders.filter(id=search_query)
        else:
            orders = Order.objects.none()
    context = {
        'orders': orders,
        'search_query': search_query,
        'current_status': current_status,
    }
    return render(request, 'home.html', context)