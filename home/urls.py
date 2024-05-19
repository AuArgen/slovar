from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lang/<int:id>/', views.lang_in, name='lang_in'),
    path('lesson/<int:id>/', views.lesson, name='lesson'),
    path('lesson_in/<int:id2>/', views.lesson_in, name='lesson_in'),
    path('test/<int:id>/', views.test_start, name='test'),
    path('teacher/<int:id>/', views.teacher, name='teacher'),
    path('news/<int:id>/', views.news, name='news'),
]
