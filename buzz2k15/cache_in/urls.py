from django.conf.urls import url
from . import views
urlpatterns= [
        url(r'^$',views.index,name='index'),
        url(r'^getstarted/$',views.getstarted,name="getstarted"),
        url(r'^ques/(?P<ques_num>[0-9]+)/$',views.ques,name="ques"),
        url(r'^leaderboard/$',views.leaderboard,name="leaderboard"),
        ]

