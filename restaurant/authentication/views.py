from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


#from .models import Profile
from authentication.forms import RegistrationForm, UserForm
# Create your views here.

def index(request):
	return render_to_response('authentication/index.html')


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
