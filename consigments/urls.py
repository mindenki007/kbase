from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cons_list/$', views.cons_list, name='cons_list'),
    url(r'^(P?<order>)\w+/$', views.cons_list, name='cons_list'),
    url(r'^(P?<filters>)\w+/$', views.cons_list, name='cons_list'),
    url(r'^(P?<filters>)\w+&(P?<order>)\w+/$', views.cons_list, name='cons_list'),
    url(r'^consigments/new/$', views.add_cons, name='add_cons'),
    url(r'^consigments/(?P<pk>\d+)/edit/$', views.edit_cons, name='edit_cons'),
]
