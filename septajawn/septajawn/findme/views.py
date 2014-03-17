# Create your views here.
from django.contrib.gis.geoip import GeoIP
from django.http import HttpResponse
import requests


def getLocation(request):
    g = GeoIP()

    ip = request.META.get('REMOTE_ADDR', None)

    # Since we're developing in a local vagrant environment, 
    # IP will be local and forwarded, so not useful to GeoIP.
    # Let's find the external IP of current connection and use that.
    r = requests.get('http://ifconfig.me/ip')
    ip = r.content.rstrip('\n')
    print "FOUND THIS IP: %s" % ip

    if ip:
        city = g.city(ip)['city']
    else:
        city = 'Rome' # default city
    return HttpResponse("You are in the fair city of: " + city)
