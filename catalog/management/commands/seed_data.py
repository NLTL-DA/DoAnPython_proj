import csv
import os
from django.core.management.base import BaseCommand
from catalog.models import MenuItem, Category, Ingredient
from customer.models import Customer
from staff.models import Staff
from operations.models import Order, OrderItem, Table
from django.contrib.auth.models import User
from datetime import datetime
from decimal import Decimal


class Command(BaseCommand):
    help = 'Seed database with sample data from CSV files'

    def handle(self, *args, **options):
        data_dir = os.path.join(os.path.dirname(__file__), '../../../../DataToUse')
        
        self.stdout.write('Clearing existing data...')
        MenuItem.objects.all().delete()
        Category.objects.all().delete()
        Customer.objects.all().delete()
        Order.objects.all().delete()
        OrderItem.objects.all().delete()
        Staff.objects.filter(user__username__startswith='staff_').delete()
        User.objects.filter(username__startswith='staff_').delete()
        Table.objects.all().delete()
        
        # Create basic data first
        self.stdout.write('Creating tables...')
        for i in range(1, 11):
            Table.objects.create(number=i, capacity=4, status='available', zone='indoor')
        
        self.stdout.write('Creating categories...')
        category, _ = Category.objects.get_or_create(
            name='Thực đơn chính',
            defaults={'description': 'Các món ăn chính'}
        )
        
        self.stdout.write('Creating menu items from CSV...')
        csv_file = os.path.join(data_dir, 'san_pham.csv')
        if os.path.exists(csv_file):
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        MenuItem.objects.get_or_create(
                            name=row['Ten_sp'],
                            defaults={
                                'category': category,
                                'price': Decimal(row['Don_gia']),
                                'description': f"Sản phẩm: {row['Ma_sp']}",
                                'status': 'available'
                            }
                        )
                    except Exception as e:
                        self.stdout.write(f'Error creating menu item: {e}')
        
        self.stdout.write('Creating customers from CSV...')
        csv_file = os.path.join(data_dir, 'khach_hang.csv')
        if os.path.exists(csv_file):
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        Customer.objects.get_or_create(
                            phone=row['Sdt'],
                            defaults={
                                'name': row['Ten_kh'],
                                'email': row.get('Email', ''),
                            }
                        )
                    except Exception as e:
                        self.stdout.write(f'Error creating customer: {e}')
        
        self.stdout.write('Creating staff from CSV...')
        csv_file = os.path.join(data_dir, 'nhan_vien.csv')
        if os.path.exists(csv_file):
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        username = row['Ma_nv'].lower()
                        user, _ = User.objects.get_or_create(
                            username=username,
                            defaults={
                                'first_name': row['Ten_nv'].split()[0] if row['Ten_nv'] else '',
                                'last_name': ' '.join(row['Ten_nv'].split()[1:]) if len(row['Ten_nv'].split()) > 1 else '',
                                'email': row.get('Email', ''),
                            }
                        )
                        Staff.objects.get_or_create(
                            user=user,
                            defaults={
                                'role': 'waiter',
                                'phone': row.get('Sdt', ''),
                            }
                        )
                    except Exception as e:
                        self.stdout.write(f'Error creating staff: {e}')
        
        self.stdout.write('Creating orders from CSV...')
        csv_file = os.path.join(data_dir, 'hoa_don.csv')
        if os.path.exists(csv_file):
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                tables = list(Table.objects.all())
                customers = list(Customer.objects.all())
                
                for idx, row in enumerate(reader):
                    try:
                        table = tables[idx % len(tables)] if tables else None
                        customer = customers[idx % len(customers)] if customers else None
                        
                        Order.objects.get_or_create(
                            id=idx + 1,
                            defaults={
                                'table': table,
                                'customer': customer,
                                'status': 'paid',
                                'payment_method': 'cash',
                                'note': f"Đơn hàng: {row['Ma_hd']}",
                            }
                        )
                    except Exception as e:
                        self.stdout.write(f'Error creating order: {e}')
        
        self.stdout.write(self.style.SUCCESS('Data seeding completed successfully!'))
