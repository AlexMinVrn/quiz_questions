from django.contrib import admin

from .models import Questions


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'id_question', 'text_question', 'text_answer')
