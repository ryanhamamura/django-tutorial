from django.contrib import admin

from .models import Choice, Question 

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

    # Choose what columns to display in question form
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # Add filters
    list_filter = ['pub_date']

    # Add search fields
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
