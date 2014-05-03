from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
import septajawn.views
admin.autodiscover()
import requests

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='openmaps.html')),
    url(r'^whereami/?$', TemplateView.as_view(template_name='openmaps.html')),
    url(r'^route/(?P<route>\d{0,3})/nearest/stop', septajawn.views.getNearestStop),
    url(r'^route/(?P<route>\d{0,3})/nearest/vehicle', septajawn.views.getNearestTrolley),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
