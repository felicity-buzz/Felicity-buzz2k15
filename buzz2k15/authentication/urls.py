from django.conf.urls import url
from . import views
urlpatterns = [
		url(r'^register_success/$', views.register_success, name='register'),
		url(r'^confirm/(?P<activation_key>\w+)/$', views.register_confirm, name='confirm'),
        url(r'^sign_up/$', views.register_user, name='sign_up'),
        url(r'^login/$', views.login, name='sign_up'),
        url(r'^logout/$', views.logout, name='logout'),
	]
