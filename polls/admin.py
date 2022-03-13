from django.contrib import admin
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    list_display = ['question_text', 'pub_date']


class ChoiceAdmin(admin.ModelAdmin):
    list_filter = ['question']
    list_display = ['choice_text', 'votes', 'question']
    list_editable = ['votes', 'question']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
