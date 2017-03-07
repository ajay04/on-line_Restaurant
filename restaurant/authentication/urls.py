from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from django.contrib import admin
from authentication import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signUp, name='signUp'),
    url(r'^signup/successful/$', views.signup_successful, name = 'signup successful'),
   ]