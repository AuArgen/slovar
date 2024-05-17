from django.contrib import admin

from teachers.models import Teacher, News


# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'email', 'language')
    search_fields = ('id', 'email', 'language')
    list_filter = ('language',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description')
    list_filter = ('title',)
