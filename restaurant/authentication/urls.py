from django.conf.urls import url, include
from django.contrib import admin
from . import views
from menu.views import index
from django.urls import reverse


urlpatterns = [
    # url(r'^$', reverse('menu:index') ),
    url(r'^register/$', views.signup, name='register/signup'),
    url(r'^login/$', views.user_login, name="login"),
    url(r'^logout/$', views.user_logout, name = 'logout'),
    url(r'^home/$', views.home, name="home"),

]
