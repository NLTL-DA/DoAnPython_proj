from django.urls import path
from staff.views.auth_page import login_page

urlpatterns = [
    # HTML
    path('login/', login_page, name='login'),
]