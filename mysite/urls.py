from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import blog

admin.autodiscover()

urlpatterns = [
	url(r'^$', include(blog.urls)),
	url(r'^blog/', include(blog.urls)),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
