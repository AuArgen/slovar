# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin2024/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('home.urls')),  # Добавьте эту строку для главной страницы
]
