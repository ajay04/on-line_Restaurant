from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.createFood, name='create'),
    url(r'^search.*', views.search, name='search'),
    url(r'^(?P<cuisine>\w+)/$',views.cuisine,name='cuisine'),
    url(r'^(?P<cuisine>\w+)/(?P<food>\w+)/$', views.food, name='food'),
]
