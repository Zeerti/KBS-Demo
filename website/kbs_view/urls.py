from django.conf.urls import url, include
from kbs_view import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^documents/$', views.DocumentListView.as_view(), name='documents'),
	url(r'^document/(?P<pk>\d+)$', views.DocumentDetailView.as_view(), name='document-detail'),
]
		