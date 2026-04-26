from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Staff(models.Model):
    ROLE_CHOICES = [
        ('manager', 'Quản lý'),
        ('waiter', 'Phục vụ'),
        ('chef', 'Bếp trưởng'),
        ('cashier', 'Thu ngân'),
        ('bartender', 'Pha chế'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile', verbose_name="Tài khoản")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name="Chức vụ")
    phone = models.CharField(max_length=20, verbose_name="Số điện thoại")
    address = models.TextField(blank=True, verbose_name="Địa chỉ")
    salary = models.DecimalField(max_digits=12, decimal_places=0, default=0, verbose_name="Lương (VNĐ)")
    hire_date = models.DateField(default=timezone.now, verbose_name="Ngày vào làm")
    is_active = models.BooleanField(default=True, verbose_name="Đang làm việc")

    class Meta:
        verbose_name = "Nhân viên"
        verbose_name_plural = "Nhân viên"

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {self.get_role_display()}"
