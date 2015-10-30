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
    return HttpResponse('hello')

@login_required(login_url='/buzz/portal/accounts/login/')
def getstarted(request):
	if request.user.username:
		profile = Profile(user = request.user, score = 0, question_number = 0)
		profile.save()
		return HttpResponseRedirect('/buzz/portal/cache-in/ques/1/')
    

@login_required(login_url='/buzz/portal/accounts/login/')
def ques(request, ques_num):
	print len(Question.objects.all())
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
	itwo = question.question_image2
	ithree = question.question_image3
	ifour = question.question_image4
	images_list = [ione]
	if itwo:
		images_list.append(itwo)
	if ithree:
		images_list.append(ithree)
	if ifour:
		images_list.append(ifour)
	form = AnswerForm()
	context = {'question' : question, 'images_list' : images_list, 'form' : form, 'user' : request.user}
	return render(request, 'cache_in/ques.html', context)

def leaderboard(request):
    leaders = Profile.objects.all().order_by('-score','time_completed')
    return render(request, 'cache_in/leaderboard.html', {'leaders' : leaders})
# Create your views here.
