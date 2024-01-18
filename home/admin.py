from django.contrib import admin
from .models import *

class WordAdmin(admin.ModelAdmin):
    list_display = ('word',)

class TextAdmin(admin.ModelAdmin):
    list_display = ('word',)


admin.site.register(Word, WordAdmin)
admin.site.register(Text, TextAdmin)
