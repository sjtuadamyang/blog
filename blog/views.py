from django.http import HttpResponse
from django.template import RequestContext, loader
from blog import models
from django import shortcuts

def index(request):
	posts = models.Post.objects.all()
	context = {'posts': posts}
	return shortcuts.render(request, 'blog/index.html', context)

def article(request):
	article_id = int(request.GET.get('article_id'))
	post = models.Post.objects.get(id=article_id)
	context = {'post': post}
	return shortcuts.render(request, 'blog/article_partial.html', context)

def frame(request):
	posts = models.Post.objects.all()
	context = {'posts': posts}
	return shortcuts.render(request, 'blog/frame.html', context)
