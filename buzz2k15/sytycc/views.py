from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
def index(request):
    return HttpResponse("welcome to index")

def getstarted(request):
    current_user=Profile.objects.filter(user=request.user)
    if current_user:
        return HttpResponse("you have already participated")
    current_user=Profile(user=request.user)
    current_user.save()
    return HttpResponseRedirect('/buzz/portal/so-you-think/ques/1')
def ques(request,ques_num):
    
def leaderboard(request):
    return HttpResponse("welcome to leaderboard")

# Create your views here.
