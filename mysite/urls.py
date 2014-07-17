from django.conf.urls import patterns, include, url

from django.contrib import admin
import blog
admin.autodiscover()

urlpatterns = [
	url(r'^$', include(blog.urls)),
	url(r'^blog/', include(blog.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
