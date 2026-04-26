from django.urls import path, include
from .views import views

urlpatterns = [
    path('', views.catalog_page, name='catalog_page'),
    path('api/', include('catalog.api_urls')),  # → /catalog/api/
]