from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from blog import models

def index(request):
	posts = models.Post.objects.all()

	template = loader.get_template('blog/index.html')
	context = RequestContext(request, {'posts': posts})
	return HttpResponse(template.render(context))

def article(request):
	post_0 = models.Post.objects.all()[0]
	print post_0.image.url
	template = loader.get_template('blog/article.html')
	context = RequestContext(request, {'image': post_0.image,
									   'content': 'crap'})
	return HttpResponse(template.render(context))
