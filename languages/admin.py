from django.contrib import admin
from .models import Language
# Register your models here.

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'key')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
