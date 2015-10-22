from django.conf.urls import url
from . import views
urlpatterns = [
		url(r'^ques/(?P<ques_num>[0-9]+)/$', views.ques, name='ques'),
	]
		
