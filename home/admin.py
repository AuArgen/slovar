from django.contrib import admin
from .models import *


class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'user_id')


class LearnedWordAdmin(admin.ModelAdmin):
    list_display = ('word', 'user_id')


class TextAdmin(admin.ModelAdmin):
    list_display = ('word', 'user_id')


class LearnedTextAdmin(admin.ModelAdmin):
    list_display = ('word', 'user_id')


admin.site.register(Word, WordAdmin)
admin.site.register(LearnedWord, WordAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(LearnedText, TextAdmin)
