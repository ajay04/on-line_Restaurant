from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import UserProfile


#from .models import Profile
from authentication.forms import RegistrationForm, UserForm
# Create your views here.

def index(request):
	return render_to_response('index.html')



def sendmail(request):
      if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
          firstname = form.cleaned_data['firstname']
          lastname = form.cleaned_data['lastname']
          email = form.cleaned_data['email']
          subject = form.cleaned_data['subject']
          botcheck = form.cleaned_data['botcheck'].lower()
          message = form.cleaned_data['message']
          if botcheck == 'yes':
            try:
              fullemail = firstname + " " + lastname + " " + "<" + email + ">"
              send_mail(subject, message, fullemail, ['SENDTOUSER@DOMAIN.COM'])
              return HttpResponseRedirect('/email/thankyou/')
            except:
              return HttpResponseRedirect('/email/')
        else:
          return HttpResponseRedirect('/email/')
      else:
        return HttpResponseRedirect('/email/')  


@csrf_exempt
def signUp(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
					username = form.cleaned_data['username'],
					password = form.cleaned_data['password1'],
					email = form.cleaned_data['email'],
					first_name = form.cleaned_data['first_name'],
					last_name = form.cleaned_data['last_name'])
			return HttpResponseRedirect('/signup/successful')
	else:
		form = RegistrationForm()
	variables = RequestContext(request, {'form': form})
	return render_to_response('signup.html', variables)

def signup_successful(request):
	return render_to_response('signup_successful.html')

@login_required
def homepage(request):
	user = UserProfile.objects.all()
	context = {
	'user':request.user,
	
	}
	#return render_to_response('homepage.html')
	return render_to_response('homepage.html', context)

def logout(request):
	return render_to_response('logout.html')