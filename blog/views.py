from django.http import HttpResponse
from django.template import RequestContext, loader
from blog import models
from django import shortcuts

def index(request):
	posts = models.Post.objects.all()
	context = {'posts': posts}
	return shortcuts.render(request, 'blog/index.html', context)

def article_svc(request, id):
	post = models.Post.objects.get(id=id)
	context = {'post': post}
	return shortcuts.render(request, 'blog/article.html', context)

def page_svc(request, index):
	context = {}
	template = ''
	if index == '0':
		template = 'blog/profile.html'
		print template
	if index == '1':
		template = 'blog/resume.html'
	if index == '2':
		template = 'blog/blog.html'
		posts = models.Post.objects.all()
		context['posts'] = posts
	if index == '3':
		template = 'blog/contact.html'

	return shortcuts.render(request, template, context)


def frame(request):
	posts = models.Post.objects.all()
	context = {'posts': posts}
	return shortcuts.render(request, 'blog/frame.html', context)

def base(request):
	return shortcuts.render(request, 'blog/base.html', {})

