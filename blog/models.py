from django.db import models

# Defines Post data model
class Post(models.Model):
	title = models.CharField(max_length=30)
	date = models.DateField()
	image = models.ImageField(upload_to="blog/static/blog/media/images/%Y/%m/%d")
	thumbnail = models.ImageField(upload_to="blog/static/blog/media/thumbnails/%Y/%m/%d")
	content = models.TextField()
	preview = models.TextField()