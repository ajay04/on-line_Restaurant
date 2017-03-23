from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from django.contrib import admin
from supplementtut import views

urlpatterns = [

    url(r'^signup/$', views.signup, name='signUp'),
    url(r'^signup/successful/$', views.signup_successful, name = 'signup successful'),

	url(r'^accounts/login/$', auth_views.login, name = 'login'),
    url(r'^accounts/profile/$', views.homepage, name = 'login_Home'),

    url(r'^logout/$' , views.logout_page, name ='logout'),

	url(r'^registration/activate/complete/$', views.activation_complete, name = "complete"),
]
