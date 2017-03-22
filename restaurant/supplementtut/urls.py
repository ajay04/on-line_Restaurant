from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from django.contrib import admin
from supplementtut import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
<<<<<<< HEAD:restaurant/authentication/urls.py
    url(r'^signup/$', views.signUp, name='signUp'),
    url(r'^signup/successful/$', views.signup_successful, name = 'signup successful'),
	url(r'^login/$', auth_views.login, name = 'login'),
    url(r'^homepage/$', views.homepage, name = 'login_Home'),
=======
    #url(r'^signup/$', views.signUp, name='signUp'),
    #url(r'^signup/successful/$', views.signup_successful, name = 'signup successful'),
	url(r'^accounts/login/$', auth_views.login, name = 'login'),
    url(r'^accounts/profile/$', views.homepage, name = 'login_Home'),
>>>>>>> 34db759a88706b2875c95dc8881a07adaf8dfdc8:restaurant/supplementtut/urls.py
    url(r'^logout/$' , views.logout_page, name ='logout'),
	#url(r'^email/send/$', views.sendmail),
	url(r'^registration/activate/complete/$', views.activation_complete, name = "complete"),


<<<<<<< HEAD:restaurant/authentication/urls.py
   ]
=======
   ]	
>>>>>>> 34db759a88706b2875c95dc8881a07adaf8dfdc8:restaurant/supplementtut/urls.py
