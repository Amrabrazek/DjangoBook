from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# def homePageView(request):
#     return HttpResponse("Hello, world!")

class HomePageVIew(TemplateView):
    template_name="home.html"
    
class AboutPageVIew(TemplateView):
    template_name="about.html"
# Create your views here.
