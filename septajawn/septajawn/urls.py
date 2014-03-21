from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
import septajawn.findme.views
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^whereami-server/', septajawn.findme.views.getLocation),
    url(r'^whereami-js/', TemplateView.as_view(template_name='map.html')),
    url(r'^whereami-gmaps/', TemplateView.as_view(template_name='gmaps.html')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
