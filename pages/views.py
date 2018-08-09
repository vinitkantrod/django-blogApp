from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView): 
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = "about.html"
    
def homePageView(request):
    return HttpResponse('Hello, World!')