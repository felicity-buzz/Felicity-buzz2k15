from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import Http404
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json


def index(request):
	keywords = {}
	if request.user.username:
		keywords.update({ 'user':request.user })
	return render_to_response('home/index.html',keywords)
	