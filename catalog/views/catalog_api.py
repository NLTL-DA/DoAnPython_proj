from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Category, Ingredient, MenuItem, Inventory
from ..serializers import CategorySerializer, IngredientSerializer, MenuItemSerializer, InventorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['name']
    @action(detail=True, methods=['get'])
    def menu_items(self, request, pk=None):
        category = self.get_object()
        menu_items = MenuItem.objects.filter(category=category)
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    search_fields = ['name']
    @action(detail=True, methods=['get'])
    def menu_items(self, request, pk=None):
        ingredient = self.get_object()
        menu_items = MenuItem.objects.filter(ingredients=ingredient)
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    search_fields = ['name', 'description']
    filterset_fields = ['category', 'status']
    @action(detail=True, methods=['get'])
    def inventory(self, request, pk=None):
        item = self.get_object()
        inventory = Inventory.objects.filter(menu_item=item).first()
        if inventory:
            serializer = InventorySerializer(inventory)
            return Response(serializer.data)
        else:
            return Response({'detail': 'Inventory not found'}, status=404)


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        low_stock_items = Inventory.objects.filter(quantity__lte=5)
        serializer = self.get_serializer(low_stock_items, many=True)
        return Response(serializer.data)


