from django.conf.urls import url, include
from django.contrib import admin
from authentication import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^register/$', views.signup, name='register/signup'),
    url(r'^login/$', views.user_login, name="login"),
    url(r'^logout/$', views.user_logout, name = 'logout'),
    url(r'^home/$', views.home, name="home"),
    #url(r'^order_history/$', view.order_history, name=order_history),

]