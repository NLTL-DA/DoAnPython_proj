from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Tên khách hàng")
    phone = models.CharField(max_length=20, unique=True, verbose_name="Số điện thoại")
    email = models.EmailField(blank=True, verbose_name="Email")
    address = models.TextField(blank=True, verbose_name="Địa chỉ")
    points = models.IntegerField(default=0, verbose_name="Điểm tích lũy")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Khách hàng"
        verbose_name_plural = "Khách hàng"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.phone})"
    