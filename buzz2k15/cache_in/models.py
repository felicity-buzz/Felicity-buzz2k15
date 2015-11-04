from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
	question_image1=models.ImageField(upload_to='cache_in_images')
	answer=models.CharField(max_length=1000)
	q_num=models.IntegerField()
	def __unicode__(self):
		return unicode(self.q_num)

class Profile(models.Model):
	user=models.OneToOneField(User,related_name='CacheIn_user', unique = True)
	score=models.IntegerField(default=0)
	question_number=models.IntegerField(default=0)
	time_completed=models.DateTimeField(default=timezone.now)
	solved = models.CharField(max_length = 300, default = '0,', blank = True)
	def __unicode__(self):
		return unicode(self.user)







# Create your models here.
