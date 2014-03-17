# Create your views here.
from django.contrib.gis.geoip import GeoIP

def getLocation(request):
    g = GeoIP()
    ip = request.META.get('REMOTE_ADDR', None)
    if ip:
        city = g.city(ip)['city']
    else:
        city = 'Rome' # default city
    return HttpResponse("You are in the fair city of: " + city)
