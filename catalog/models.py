from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên danh mục")
    description = models.TextField(blank=True, verbose_name="Mô tả")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Danh mục"
        verbose_name_plural = "Danh mục món ăn"
        ordering = ['name']

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên nguyên liệu")
    quantity = models.FloatField(default=0, verbose_name="Số lượng tồn kho")
    unit = models.CharField(max_length=20, verbose_name="Đơn vị")
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        verbose_name = "Nguyên liệu"
        verbose_name_plural = "Nguyên liệu"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"


class MenuItem(models.Model):
    STATUS_CHOICES = [
        ('available', 'Còn hàng'),
        ('unavailable', 'Hết hàng'),
        ('seasonal', 'Theo mùa'),
    ]
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='items', verbose_name="Danh mục")
    name = models.CharField(max_length=200, verbose_name="Tên món")
    description = models.TextField(blank=True, verbose_name="Mô tả")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Giá (VNĐ)")
    image = models.ImageField(upload_to='menu/', blank=True, null=True, verbose_name="Hình ảnh")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name="Trạng thái")
    is_featured = models.BooleanField(default=False, verbose_name="Món nổi bật")
    ingredients = models.ManyToManyField('Ingredient', through='Inventory', related_name='menu_items', verbose_name="Nguyên liệu")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Món ăn"
        verbose_name_plural = "Thực đơn"
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} - {self.price:,}đ"

    @property
    def formatted_price(self):
        return f"{int(self.price):,}đ"


class Inventory(models.Model):
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE, verbose_name="Món ăn")
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE, verbose_name="Nguyên liệu")
    quantity_needed = models.FloatField(default=1, verbose_name="Số lượng cần")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Tồn kho"
        verbose_name_plural = "Tồn kho"
        unique_together = ('menu_item', 'ingredient')

    def __str__(self):
        return f"{self.menu_item.name} - {self.ingredient.name}"
