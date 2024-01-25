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
    path('update-word/<int:pk>/', views.update_word, name='update-word'),
    path('update-text/<int:pk>/', views.update_text, name='update-text'),
    path('learned-word/<int:pk>/', views.learned_word, name='learned-word'),
    path('learned-text/<int:pk>/', views.learned_text, name='learned-text'),
    path('show-learned-text/', views.learned_show_text, name='learned-show-text'),
    path('delete-learned-text/<int:pk>/', views.learned_delete_text, name='learned-delete-text'),
    path('show-learned-word/', views.learned_show_word, name='learned-show-word'),
    path('delete-learned-word/<int:pk>/', views.learned_delete_word, name='learned-delete-word'),
]
