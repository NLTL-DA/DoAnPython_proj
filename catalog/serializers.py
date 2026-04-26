from rest_framework import serializers
from .models import Category, Ingredient, MenuItem, Inventory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'quantity', 'unit', 'created_at', 'last_updated']


class MenuItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'category', 'category_name', 'description', 
                'price', 'status', 'is_featured', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class InventorySerializer(serializers.ModelSerializer):
    menu_item_name = serializers.CharField(source='menu_item.name', read_only=True)
    ingredient_name = serializers.CharField(source='ingredient.name', read_only=True)

    class Meta:
        model = Inventory
        fields = ['id', 'menu_item', 'menu_item_name', 'ingredient', 
                'ingredient_name', 'quantity_needed', 'created_at']
