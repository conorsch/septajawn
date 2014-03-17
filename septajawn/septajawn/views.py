from django.views.generic import TemplateView

class MapView(TemplateView):
    template_name = "map.html"

    def __init__(self, sth):
        pass

class HomeView(TemplateView):
    template_name = "home.html"
    def __init__(self, sth):
        pass

