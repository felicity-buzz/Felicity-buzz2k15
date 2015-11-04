from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import Http404
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import redirect
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json

def login(request):
	if request.user.username:
		return HttpResponseRedirect('/')
	else:
		if request.method == 'POST':
			username=request.POST.get('username','')
			password=request.POST.get('password','')
			user=auth.authenticate(username=username,password=password)
			if user is not None:
				auth.login(request,user)
				return HttpResponseRedirect('/buzz/events.html')
			else:
				return HttpResponseRedirect('/buzz/portal/accounts/invalid/')
		else:
			c={}
			c.update(csrf(request))
			return render_to_response('authentication/login.html',c)

def invalid(request):
	if request.user.username:
		return HttpResponseRedirect('/')
	else:
		c={}
		c.update(csrf(request))
		return render_to_response('authentication/invalid.html',c)

def register(request):
	if request.user.username:
		return HttpResponseRedirect('/')
	else:
		if request.method =='POST':
		    form = UserCreateForm(request.POST)
		    if form.is_valid():
				print form
				var = form.save()
				username=request.POST.get('username','')
				password=request.POST.get('password1','')
				print username
				user=auth.authenticate(username=username,password=password)
				if user is not None:
					auth.login(request,user)
					return HttpResponseRedirect('/buzz/events.html')
		else:
		    form = UserCreateForm()

		return render_to_response('authentication/register.html', {
		    'form': form,
		},context_instance=RequestContext(request))

@login_required(login_url='/buzz/portal/accounts/login/')
def logout(request):
	auth.logout(request)
	return redirect('authentication.views.login')
