from rest_framework.routers import DefaultRouter
from operations.views.operations_api import TableViewSet, ReservationViewSet, OrderViewSet, OrderItemViewSet

router = DefaultRouter()
router.register(r'tables', TableViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)

urlpatterns = router.urls