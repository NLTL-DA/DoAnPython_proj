from django.urls import path, include
from .views.views import operations_page, table_page

urlpatterns = [
    path('', operations_page, name='operations_page'),
    path('table/', table_page, name='table_page'),
]