from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from gordian_knot.models import Question, Profile
from django.core.context_processors import csrf
from django.contrib import messages
def index(request):
	check = 0
	getstarted = Profile.objects.filter(user=request.user.id)
	if len(getstarted) == 0:
		check = 0
	else:
		check = 1
	keys = { 'user':request.user,'check':check,'range1':range(1,11),'range2':range(11,21) }
	return render(request, 'gordian_knot/index.html', keys)


@login_required(login_url='/buzz/portal/accounts/login/')
def score_value(request):
	return 100

@login_required(login_url='/buzz/portal/accounts/login/')
def get_started(request):
	if request.user.username:
		check = 0
		getstarted = Profile.objects.filter(user=request.user.id)
		if len(getstarted) == 0:
			check = 0
		else:
			check = 1
		if check == 0:
			profile=Profile(user=request.user,score=0,tries=0,level=1)
			profile.save()
			return HttpResponseRedirect('/buzz/portal/gordian-knot/ques/1/')
		else:
			return HttpResponse("You have already started. Go back and do contest !")

@login_required(login_url='/buzz/portal/accounts/login/')   #if conditions can be removed by usign decorators
def ques(request, ques_num):
	if int(ques_num) <= request.user.profile.level:
		user = request.user
		my_ques =  get_object_or_404(Question, pk = int(ques_num))
		keys={}
		keys.update(csrf(request))
		keys.update( {'user':request.user, 'my_ques':my_ques, 'question_no':ques_num } )
		if request.method == 'POST':
			if int(ques_num) == request.user.profile.level:
				user.profile.tries += 1
				user.profile.save()
				answer=request.POST.get('answer','')
				print answer
				print my_ques.correct_answer
				if my_ques.correct_answer == answer :
					print answer
					user.profile.score += score_value(request)
					user.profile.level += 1
					user.profile.tries = 0
					user.profile.save()
				return HttpResponseRedirect('/buzz/portal/gordian-knot/ques/'+ str(user.profile.level) + '/')
			else:
				return HttpResponse("You have already completed this problem !")
		else:
			return render_to_response('gordian_knot/question.html',keys)
	else:
		return HttpResponse("You are not eligible for this access !")
def leaderboard(request):
	user_list = Profile.objects.all().order_by('score')[::-1]
	return render(request, 'gordian_knot/leader.html', {'user_list' : user_list})
