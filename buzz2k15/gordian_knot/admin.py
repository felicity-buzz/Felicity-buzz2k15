from django.contrib import admin

# Register your models here.
from gordian_knot.models import Question, Answer, Score
from django.contrib.auth.models import User

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('sequence_number', 'level', 'question_text')
	list_filter = ['level']

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('question', 'answer', 'user', 'correct')
	list_filter = ['question', 'correct', 'user']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Score)
