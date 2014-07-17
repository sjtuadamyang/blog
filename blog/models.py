from django.db import models
from easy_thumbnails import signals
from easy_thumbnails import signal_handlers

# Defines Post data model
class Post(models.Model):
	title = models.CharField(max_length=30)
	date = models.DateField()
	image = models.ImageField(upload_to="blog/images/%Y/%m/%d", blank=True)
	content = models.TextField()
	preview = models.TextField()

# Register easy_thumbnails.signal_handlers.generate_aliases to easy_thumbnails.signals.saved_file
signals.saved_file.connect(signal_handlers.generate_aliases)