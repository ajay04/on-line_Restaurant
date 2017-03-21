from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import MyRegistrationSupplement
import datetime



#from .models import Profile
#from supplementtut.forms import RegistrationForm, UserForm
# Create your views here.

def index(request):
	return render_to_response('index.html')

@login_required
def homepage(request):
	user_info = MyRegistrationSupplement.objects.all()
	user_info2 = MyRegistrationSupplement.objects.filter(user_type = 'user_type')
	print (user_info)
	'''context = {
							'user_info ': user_info2
							}
					'''
	now = datetime.datetime.now()				
	context = {
	'user_info' : user_info,
	'now' : now
	}
	print (now)

	#return render_to_response('homepage.html')
	return render(request, 'homepage.html', context)

def logout_page(request):
	logout(request)
	return render_to_response('logout.html')
