from rest_framework.routers import DefaultRouter
from .views.catalog_api import CategoryViewSet, IngredientViewSet, MenuItemViewSet, InventoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'ingredients', IngredientViewSet, basename='ingredient')
router.register(r'items', MenuItemViewSet, basename='menu-item')
router.register(r'inventory', InventoryViewSet, basename='inventory')

urlpatterns = router.urls
