from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Question(models.Model):
    question_text=models.CharField(max_length=100)
    question_option1=models.CharField(max_length=100)
    question_option2=models.CharField(max_length=100)
    question_option3=models.CharField(max_length=100)
    question_option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)

class Profile(models.Model):                                                                                                                    
    user=models.OneToOneField(User,related_name='sytycc_user', unique = True)
    score=models.IntegerField(default=0)
    time_started=models.DateTimeField(default=timezone.now)
    answers=models.CharField(max_length=1000)


# Create your models here.
