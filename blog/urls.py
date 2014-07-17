from django.conf.urls import patterns, url

from blog import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^article$', views.article, name='article')
]