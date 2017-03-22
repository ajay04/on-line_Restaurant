from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^recipes/$', views.index, name='index'),
    url(r'^recipes/create/$', views.createRecipe, name='create'),
    url(r'^recipes/search.*', views.search, name='search'),
    url(r'^recipes/(?P<cuisine>\w+)/$',views.cuisine,name='cuisine'),
    url(r'^recipes/(?P<cuisine>\w+)/(?P<food>\w+)/$', views.recipe, name='recipe'),
]
