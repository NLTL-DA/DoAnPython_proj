from django.contrib.auth import authenticate

def login_user(request, username, password):
    return authenticate(request, username=username, password=password)