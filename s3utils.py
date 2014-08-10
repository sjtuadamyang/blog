from storages.backends.s3boto import S3BotoStorage

class FixedS3BotoStorage(S3BotoStorage):
	def url(self, name):
		url = super(FixedS3BotoStorage, self).url(name)
		if name.endswith('/') and not url.endswith('/'):
			url += '/'
		return url

StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
MediaRootS3BotoStorage  = lambda: S3BotoStorage(location='media')