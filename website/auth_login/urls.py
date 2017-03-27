from django.conf.urls import patterns, url
from auth_login import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'))