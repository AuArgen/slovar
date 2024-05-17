from django.contrib import admin

from teachers.models import Teacher


# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'email', 'language')
    search_fields = ('id', 'email', 'language')
    list_filter = ('language',)
