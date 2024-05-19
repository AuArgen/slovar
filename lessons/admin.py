from django.contrib import admin
from lessons.models import Lesson, EventTest, Tests, Game


# Register your models here.
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'language')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    list_filter = ('language',)


@admin.register(EventTest)
class EventTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'language', 'lesson')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    list_filter = ('language', 'lesson')


@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'eventTest', 'question',)
    list_display_links = ('id', 'eventTest',)
    search_fields = ('id', 'question', '')
    list_filter = ('eventTest', 'question')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'lesson')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    list_filter = ('lesson',)