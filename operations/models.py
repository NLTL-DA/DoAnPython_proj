from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer
from catalog.models import MenuItem

# Create your models here.

class Table(models.Model):
    STATUS_CHOICES = [
        ('available', 'Trống'),
        ('occupied', 'Đang dùng'),
        ('reserved', 'Đã đặt'),
        ('cleaning', 'Đang dọn'),
    ]
    ZONE_CHOICES = [
        ('indoor', 'Trong nhà'),
        ('outdoor', 'Ngoài trời'),
        ('vip', 'VIP'),
        ('bar', 'Quầy bar'),
    ]

    number = models.IntegerField(unique=True, verbose_name="Số bàn")
    capacity = models.IntegerField(default=4, verbose_name="Sức chứa")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name="Trạng thái")
    zone = models.CharField(max_length=20, choices=ZONE_CHOICES, default='indoor', verbose_name="Khu vực")

    class Meta:
        verbose_name = "Bàn"
        verbose_name_plural = "Quản lý bàn"
        ordering = ['number']

    def __str__(self):
        return f"Bàn {self.number} ({self.get_status_display()})"

    
class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Chờ xác nhận'),
        ('confirmed', 'Đã xác nhận'),
        ('arrived', 'Đã đến'),
        ('cancelled', 'Đã huỷ'),
        ('no_show', 'Không đến'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='reservations', verbose_name="Khách hàng")
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, related_name='reservations', verbose_name="Bàn")
    party_size = models.IntegerField(verbose_name="Số người")
    reservation_date = models.DateField(verbose_name="Ngày đặt")
    reservation_time = models.TimeField(verbose_name="Giờ đặt")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Trạng thái")
    note = models.TextField(blank=True, verbose_name="Ghi chú")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Nhân viên tạo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Đặt bàn"
        verbose_name_plural = "Quản lý đặt bàn"
        ordering = ['-reservation_date', 'reservation_time']

    def __str__(self):
        return f"Đặt bàn #{self.id} - Bàn {self.table.number if self.table else '?'} - {self.reservation_date}"

    @property
    def subtotal(self):
        return sum(item.subtotal for item in self.items.all())


class Order(models.Model):
    STATUS_CHOICES = [
        ('open', 'Đang phục vụ'),
        ('pending_payment', 'Chờ thanh toán'),
        ('paid', 'Đã thanh toán'),
        ('cancelled', 'Đã huỷ'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Tiền mặt'),
        ('card', 'Thẻ ngân hàng'),
        ('transfer', 'Chuyển khoản'),
        ('momo', 'MoMo'),
        ('vnpay', 'VNPay'),
    ]

    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, related_name='orders', verbose_name="Bàn")
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders', verbose_name="Khách hàng")
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders', verbose_name="Nhân viên phục vụ")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open', verbose_name="Trạng thái")
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, blank=True, verbose_name="Phương thức thanh toán")
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Giảm giá (%)")
    note = models.TextField(blank=True, verbose_name="Ghi chú")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders_created', verbose_name="Nhân viên")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Đơn hàng"
        verbose_name_plural = "Đơn hàng"
        ordering = ['-created_at']

    def __str__(self):
        return f"Đơn #{self.id} - Bàn {self.table.number if self.table else '?'}"

    @property
    def subtotal(self):
        return sum(item.subtotal for item in self.items.all())
    @property
    def total_items(self):
        return self.items.count()
    
    def total(self):
        sub = sum(item.subtotal for item in self.items.all())
        return sub * (1 - self.discount / 100)

    @property
    def price(self):
        return self.total


class OrderItem(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Chờ chế biến'),
        ('preparing', 'Đang làm'),
        ('ready', 'Sẵn sàng'),
        ('served', 'Đã phục vụ'),
        ('cancelled', 'Đã huỷ'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="Đơn hàng")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, verbose_name="Món ăn")
    quantity = models.IntegerField(default=1, verbose_name="Số lượng")
    unit_price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Đơn giá")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Trạng thái bếp")
    note = models.TextField(blank=True, verbose_name="Ghi chú")

    class Meta:
        verbose_name = "Chi tiết đơn hàng"
        verbose_name_plural = "Chi tiết đơn hàng"

    def __str__(self):
        return f"{self.menu_item.name} x{self.quantity}"

    @property
    def subtotal(self):
        return self.quantity * self.unit_price
