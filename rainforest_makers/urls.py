from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rainforest_makers.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('spirit.urls', namespace="spirit", app_name="spirit")),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
