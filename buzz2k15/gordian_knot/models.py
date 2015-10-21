from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	level_list = [(1, 1), (2, 2), (3, 3), (4, 4)]
	question_text = models.TextField ('Question', max_length = 1000)
	level = models.IntegerField (choices = level_list, default = 1)
	correct_answer = models.IntegerField ()
	sequence_number = models.IntegerField()

class Answer(models.Model):
	user = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	answer = models.IntegerField()
	time_submitted = models.DateTimeField('time submitted', default = timezone.now)
	correct = models.BooleanField(default = 0)

class AnswerForm(ModelForm):
	class Meta:
		model = Answer
		fields = ['answer']
