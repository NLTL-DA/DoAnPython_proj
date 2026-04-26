from operations.models import Order, OrderItem, Table

def create_order(data):
    table = Table.objects.get(id=data['table_id'])
    order = Order.objects.create(table=table)
    total = 0
    for item in data['items']:
        OrderItem.objects.create(order=order, menu_item_id=item['menu_item_id'], quantity=item['quantity'])
    return order
        
def calculate_total(order):
    total = 0
    for item in order.items.all():
        total += item.menu_item.price * item.quantity
    return total
