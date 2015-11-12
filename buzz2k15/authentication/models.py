from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())

    def __unicode__(self):                #python 2 if python3 user __str__
        return self.user.username

    class Meta:
        verbose_name_plural=u'User profiles'
