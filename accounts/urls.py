# accounts/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]
