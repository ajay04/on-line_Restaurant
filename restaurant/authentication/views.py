from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse
from authentication.models import UserProfile, User
from authentication.forms import UserForm, UserProfileForm
from django.contrib.auth import logout
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from recipes.models import Recipe




# Create your views here.

def index(request):
	context = { 'recipes' : Recipe.objects.all()}
	return render(request, 'index.html', context)

@csrf_exempt
def signup(request):
	context = RequestContext(request)


#registration status to display THankyou message
	registered = False
	
#save the forms if valid
	if request.method =='POST':
		user_form = UserForm(request.POST)
		userProfile_form = UserProfileForm(request.POST)
	#save the forms if valid
		if user_form.is_valid() and userProfile_form.is_valid() and  user_form.cleaned_data['password'] == user_form.cleaned_data['confirm_password']:
			user = user_form.save()
			user.set_password(user.password)
			user.is_active = False

			user.save()

			profile = userProfile_form.save(commit=False)
			profile.user = user
			user.is_active = False

			profile.save()

			registered = True
		elif user_form.data['password'] != user_form.data['confirm_password']:
			user_form.add_error('confirm_password', 'Password did not match')
		else:
			print (user_form.errors, userProfile_form.errors)
	else:
		user_form = UserForm()
		userProfile_form = UserProfileForm()
	return render_to_response("register.html", {"user_form": user_form,
			"userProfile_form" : userProfile_form, "registered": registered}, context)

@csrf_exempt

def user_login(request):
	context = RequestContext(request)
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username = username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse("Inactive Account")
		else:
			return HttpResponse ("Invalid Login Information")
	else:
		return render_to_response('loginPage.html')



def user_logout(request):
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/index')


def home(request):

	return render_to_response('home.html', {
		'user' : request.user
		})