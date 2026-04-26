from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.don_hang_view, name='home_don_hang'),
    path('home/', views.don_hang_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('don-hang/', views.don_hang_view, name='don_hang'),
]