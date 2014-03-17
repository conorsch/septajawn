from django.views.generic import TemplateView
from django.contrib.gis.geoip import GeoIP

def getLocation(self, request):
    g = GeoIP()
    ip = request.META.get('REMOTE_ADDR', None)
    if ip:
        city = g.city(ip)['city']
    else:
        city = 'Rome' # default city
    return HttpResponse("You are in the fair city of: " + city)

class MapView(TemplateView):

    def __init__(self, sth):
        pass

#        template_name = "map.html"

    def get_context_data(self, **kwargs):
        # Get context from super for returning
        context = super(MapView, self).get_context_data(**kwargs)
        return context

class HomeView(TemplateView):
    def __init__(self, sth):
        pass
#        template_name = "home.html"


