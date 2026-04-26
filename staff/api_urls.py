from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.auth_api import LoginAPIView
from .views.staff_api import StaffViewSet
router = DefaultRouter()
router.register(r'staff', StaffViewSet, basename='staff')

urlpatterns = router.urls + [
    path('login/', LoginAPIView.as_view(), name='api_login'),
]