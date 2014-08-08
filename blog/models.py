from django.db import models
from easy_thumbnails import signals
from easy_thumbnails import signal_handlers

# Defines Post data model
class Post(models.Model):
	NORMAL = 'NM'
	QUOTE = 'QT'
	LINK = 'LK'
	POST_TYPE = (
		(NORMAL, 'Normal'),
		(QUOTE, 'Quote'),
		(LINK, 'Link'),
	)
	title = models.CharField(max_length=30)
	date = models.DateField()
	blog_type = models.CharField(max_length=2, choices=POST_TYPE, default=NORMAL)
	image = models.ImageField(upload_to="blog/images/%Y/%m/%d", blank=True)
	content = models.TextField(blank=True)
	preview = models.TextField(blank=True)
	author_name = models.CharField(max_length=20, blank=True)
	link_address = models.CharField(max_length=255, blank=True)

	# Provide customized validation
	""" waiting for django 1.7
	def clean(self):
		print "I'm here"
		# Normal blog type requires valid image, content and preview
		if self.blog_type == self.NORMAL and (self.image == None or self.content == None or self.preview == None):
			raise ValidationError('Normal blog must contains valid image, content and preview')
		# Quote blog type requires valid content and author_name
		if self.blog_type == self.QUOTE and (self.content == None or self.author_name == None):
			raise ValidationError('Quote blog must contains valid content and author_name')
		# Link blog type requires valid link_address
		if self.blog_type == self.LINK and self.link_address == None:
			raise ValidationError('Link blog must contains valid link_address')
	"""

# Register easy_thumbnails.signal_handlers.generate_aliases to easy_thumbnails.signals.saved_file
signals.saved_file.connect(signal_handlers.generate_aliases)