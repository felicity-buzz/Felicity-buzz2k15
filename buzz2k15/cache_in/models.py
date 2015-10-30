from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
	question_image1=models.ImageField(upload_to='cache_in_images')
	question_image2=models.ImageField(upload_to='cache_in_images', blank = True)
	question_image3=models.ImageField(upload_to='cache_in_images', blank = True)
	question_image4=models.ImageField(upload_to='cache_in_images', blank = True)
	answer=models.CharField(max_length=1000)
	q_num=models.IntegerField()


class Profile(models.Model):
	user=models.OneToOneField(User,related_name='CacheIn_user', unique = True)
	score=models.IntegerField(default=0)
	question_number=models.IntegerField(default=0)
	time_completed=models.DateTimeField(default=timezone.now)
	
	
	
	




# Create your models here.
