from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.manager_dash, name='manager_dash'),
]
