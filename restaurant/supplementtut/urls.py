from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from django.contrib import admin
from supplementtut import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^signup/$', views.signUp, name='signUp'),
    #url(r'^signup/successful/$', views.signup_successful, name = 'signup successful'),
	url(r'^accounts/login/$', auth_views.login, name = 'login'),
    url(r'^accounts/profile/$', views.homepage, name = 'login_Home'),
    url(r'^logout/$' , views.logout_page, name ='logout'),
	#url(r'^email/send/$', views.sendmail),
	#url(r'^registration/register/$', views.signup, name = "register"),


   ]	