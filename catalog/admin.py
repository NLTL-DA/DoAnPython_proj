from django.contrib import admin
from .models import Category, Ingredient, MenuItem, Inventory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'unit', 'last_updated']
    search_fields = ['name']
    list_filter = ['unit']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'status', 'is_featured']
    list_filter = ['status', 'category', 'is_featured']
    search_fields = ['name', 'description']


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['menu_item', 'ingredient', 'quantity_needed']
    list_filter = ['menu_item', 'ingredient']
    search_fields = ['menu_item__name', 'ingredient__name']

