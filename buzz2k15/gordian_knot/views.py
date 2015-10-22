from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from gordian_knot.models import Question, Answer, Score
from gordian_knot.models import AnswerForm

# Create your views here.

def ques(request, ques_num):

	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			my_answer = form.save(commit = False)
			my_ques = get_object_or_404(Question, sequence_number = ques_num)
			my_answer.question = my_ques
			my_answer.user = request.user
			if my_ques.correct_answer == my_answer.answer:
				my_answer.correct = 1
				message = 'Congrats, your answer is correct.'
				my_user = Score.objects.filter(user = request.user)
				if my_user:
					my_user.score += 10
					my_user.save()
				else:
					my_user = Score.objects.create(user = request.user, score = 0)
					my_user.score += 10
					my_user.save()
			#	my_ques = get_object_or_404(Question, sequence_number = int(ques_num) + 1)
			else:
				my_answer.correct = 0
				message = 'Your answer is incorrect.'
#			my_comment.verified = 0
			my_answer.save()
			form = AnswerForm()
			context = {'my_ques' : my_ques, 'form' : form, 'user' : request.user, 'message' : message}
			return render (request, 'gordian_knot/ques.html', context)
	else:
		my_ques =  get_object_or_404(Question, sequence_number = ques_num)
		form = AnswerForm()
		context = {'my_ques' : my_ques, 'form' : form, 'user' : request.user}
		return render (request, 'gordian_knot/ques.html', context)

def leaderboard(request):
	user_list = Score.objects.all().order_by('score')[::-1]
	return render(request, 'gordian_knot/leader.html', {'user_list' : user_list})
