from django.contrib.auth.models import User
from authentication.models import UserProfile
from django import forms
from django.forms import ModelForm


#create form for base user profile
class UserForm(ModelForm):
	password = forms.CharField(
				widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput())

#meta class describes additional propertes about the class it belongs to
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

##form for our model
class UserProfileForm(ModelForm):

	class Meta:
	#model fields in meta reference back to the model
		model = UserProfile
		fields = ('name','user_type',)