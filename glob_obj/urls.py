from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^glob_list/$', views.globlist, name='glob_list'),
    url(r'^results/$', views.search, name='search'),
]
