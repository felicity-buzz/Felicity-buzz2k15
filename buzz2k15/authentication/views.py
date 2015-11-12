from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from forms import *
from models import *
from django.template import RequestContext
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone
from django.template import RequestContext, loader
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
def register_user(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        args['form'] = form
        if form.is_valid():
            form.save()  # save user to database if form is valid

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            activation_key = hashlib.sha1(salt+email).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            #Get user by username
            user=User.objects.get(username=username)

            # Create and save user profile
            new_profile = UserProfile(user=user, activation_key=activation_key,
                key_expires=key_expires)
            new_profile.save()

            # Send email with activation key
            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/accounts/confirm/%s" % (username, activation_key)

            send_mail(email_subject, email_body, 'sganshuliiith@gmail.com',
                [email], fail_silently=False)

            return HttpResponseRedirect('/accounts/register_success')
    else:
        args['form'] = RegistrationForm()

    return render_to_response('authentication/register.html', args, context_instance=RequestContext(request))


def register_confirm(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('/home')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('authentication/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.user
    user.is_active = True
    user.save()
    return render_to_response('authentication/confirm.html')


def register_success(request):
    return HttpResponse("Email has been send to your entered email address. Confirm It first to get started! ")

def login(request):
    if request.user.username:
        return HttpResponseRedirect('/buzz/events.html')
    else:
        if request.method == 'POST':
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            user=auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request,user)
                    return HttpResponseRedirect('/buzz/events.html')
                else:
                    return HttpResponse("Confirm you email first")
            else:
                return HttpResponseRedirect('/buzz/portal/accounts/invalid/')
        else:
            c={}
            c.update(csrf(request))
            return render_to_response('authentication/login.html',c)
def logout(request):
	auth.logout(request)
	return redirect('authentication.views.login')
