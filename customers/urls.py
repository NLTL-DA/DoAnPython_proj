from rest_framework.routers import DefaultRouter
from .views.customer_api import CustomerViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')

urlpatterns = router.urls
