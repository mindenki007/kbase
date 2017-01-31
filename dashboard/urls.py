from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tech_dash/$', views.tech_dash, name='tech_dash'),
    url(r'^$', views.manager_dash, name='manager_dash'),
    url(r'^Cir/(?P<pk>\d+)/$', views.cir_detail, name='cir_detail'),
    url(r'^Change/(?P<pk>\d+)/$', views.change_detail, name='change_detail'),
    url(r'^Changes/(?P<name>\w+)/$', views.your_changes, name='your_changes'),
]
