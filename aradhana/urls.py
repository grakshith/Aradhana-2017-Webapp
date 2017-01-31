from django.conf.urls import include, url
import django.contrib.staticfiles.views
from django.contrib import admin
from . import views
urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^events/(?P<eventID>[0-9]+)',views.events,name='events'),
	url(r'^static/(?P<path>.*)$', django.contrib.staticfiles.views.serve),
	#url(r'^events/$',views.events,name='events').
]