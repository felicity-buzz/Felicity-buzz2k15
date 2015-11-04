from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cache_in.models import Question, Profile
from django.core.context_processors import csrf
from django.utils import timezone

from .forms import AnswerForm
def index(request):
	check = 0
	getstarted = Profile.objects.filter(user=request.user.id)
	if len(getstarted) == 0:
		check = 0
	else:
		check = 1
	keys = { 'user':request.user,'check':check,'range1':range(1,11),'range2':range(11,16) }
	return render(request, 'cache_in/index.html', keys)

@login_required(login_url='/buzz/portal/accounts/login/')
def getstarted(request):
	if request.user.username:
		check = 0
		getstarted = Profile.objects.filter(user=request.user.id)
		if len(getstarted) == 0:
			check = 0
		else:
			check = 1
		if check == 0:
			profile=Profile(user=request.user,score=0, question_number = 0)
			profile.save()
			return HttpResponseRedirect('/buzz/portal/cache-in/ques/1/')
		else:
			return HttpResponse("You have already started. Go back and do contest !")

@login_required(login_url='/buzz/portal/accounts/login/')
def ques(request, ques_num):

	if int(ques_num) > len(Question.objects.all()):
		return HttpResponse("question doesn't exist.")
	question = Question.objects.get(q_num = ques_num)
	my_user = Profile.objects.get(user = request.user)
	solved_list = my_user.solved.split(',')[0:-1]
	if str(ques_num) in solved_list or int(ques_num) - my_user.question_number > 2:
		return HttpResponseRedirect ('/buzz/portal/cache-in/ques/'+ str(my_user.question_number + 1) + '/')
	#	return HttpResponse('not eligible to solve this.')
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			obj = request.POST.get('q_answer')
			flag = 0
			answer_list = question.answer.split(',')
			if obj in answer_list:
				my_user.score += 100
				if int(ques_num) > my_user.question_number:
					my_user.question_number = ques_num
				my_user.time_completed = timezone.now()
				my_user.solved += str(ques_num) + ','
				my_user.save()
				message = 'your answer is correct.'
				if int(ques_num) + 1 <= Question.objects.all().count():
					return HttpResponseRedirect('/buzz/portal/cache-in/ques/'+ str(int(ques_num) + 1) + '/')
				else:
					return HttpResponse('there are no further questions.')
	#			return HttpResponseRedirect('/buzz/portal/cache-in/ques/'+ str(int(ques_num) + 1) + '/')
			else:
				message = 'incorrect answer.'
				return HttpResponseRedirect('/buzz/portal/cache-in/ques/'+ str(ques_num) + '/')



	ione = question.question_image1
	images_list = [ione]
	form = AnswerForm()
	context = {'question' : question, 'images_list' : images_list, 'form' : form, 'user' : request.user}
	return render(request, 'cache_in/question.html', context)

def leaderboard(request):
    leaders = Profile.objects.all().order_by('-score','time_completed')
    return render(request, 'cache_in/leader.html', {'leaders' : leaders,'i':0})
# Create your views here.
