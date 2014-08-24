from django.conf.urls import patterns, url

from blog import views

urlpatterns = [
	url(r'^$', views.base, name='index'),
	url(r'^article/(?P<id>\d+)$', views.article_svc, name='article'),
	url(r'^frame$', views.frame, name='frame'),
	url(r'^base$', views.base, name='base'),
	url(r'^(?P<index>\d+)$', views.page_svc, name='page'),
]