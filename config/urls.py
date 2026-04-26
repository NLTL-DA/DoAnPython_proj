# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def root_redirect(request):
    return redirect('/staff/login/')  # send to HTML login page

urlpatterns = [
    path('', root_redirect),
    path('admin/', admin.site.urls),

    # HTML pages
    path('', include('home.urls')),         # → /home/, /dashboard/, /catalog/, /operations/, /table/
    path('staff/', include('staff.urls')),        # → /staff/login/ 
    path('operations/', include('operations.urls')),  # → /operations/
    path('catalog/', include('catalog.urls')),    # → /catalog/
    path('customers/', include('customers.urls')),  # → /customers/
    # APIs
    path('api/staff/', include('staff.api_urls')),       # → /api/staff/login/
    path('api/catalog/', include('catalog.urls')),
    path('api/operations/', include('operations.api_urls')),
    path('api/customers/', include('customers.urls')),
]