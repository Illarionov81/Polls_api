from django.contrib import admin

from api_polls.models import Polls, Questions


class QuestionsInline(admin.TabularInline):
    model = Questions
    fields = ['poll', 'text', 'questions_type']


class PollsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'start_date', 'finish_date']
    list_filter = ['name']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'start_date']
    fields = ['name', 'finish_date', 'description']
    inlines = [QuestionsInline]


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'poll', 'text', 'questions_type']
    list_display_links = ['id', 'poll', 'text']
    list_filter = ['id']
    search_fields = ['id', 'poll']
    fields = ['poll', 'text', 'questions_type']


admin.site.register(Polls, PollsAdmin)
admin.site.register(Questions, QuestionsAdmin)
