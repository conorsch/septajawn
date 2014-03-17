from django.views.generic import TemplateView
from django.contrib.gis.utils import GeoIP

class MapView(TemplateView):
    template_name = "map.html"

    def __init__(self, sth):
        pass

     def get(self, request):
         # <view logic>
        g = GeoIP()
        ip = request.META.get('REMOTE_ADDR', None)
        if ip:
            city = g.city(ip)['city']
        else:
            city = 'Rome' # default city
         return HttpResponse("You are in the fair city of: " + city)

class HomeView(TemplateView):
    template_name = "home.html"
    def __init__(self, sth):
        pass

