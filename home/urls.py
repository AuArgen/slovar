from django.urls import path
from . import views

urlpatterns = [
    # ... your existing URLs
    path('', views.home, name='home'),
    path('add-word/', views.add_word, name='add-word'),
    path('delete-word/<int:pk>/', views.delete_word, name='delete-word'),
]
