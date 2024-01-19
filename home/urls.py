from django.urls import path
from . import views

urlpatterns = [
    # ... your existing URLs
    path('', views.home, name='home'),
    path('add-word/', views.add_word, name='add-word'),
    path('add-text/', views.add_text, name='add-text'),
    path('text/', views.text, name='text'),
    path('game-text/', views.game_text, name='game_text'),
    path('game-word/', views.game_word, name='game_word'),
    path('delete-word/<int:pk>/', views.delete_word, name='delete-word'),
    path('delete-text/<int:pk>/', views.delete_text, name='delete-text'),
]
