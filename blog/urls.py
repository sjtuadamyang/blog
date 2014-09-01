from django.conf.urls import patterns, url

from blog import views

urlpatterns = [
	url(r'^$', views.simplev, name='index'),
	url(r'^article/(?P<id>\d+)$', views.article_svc, name='article'),
	url(r'^_contact$', views.base, name='version_with_contact'),
	url(r'^(?P<index>\d+)$', views.page_svc, name='page'),
]