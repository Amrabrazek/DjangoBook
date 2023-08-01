from django.urls import path
from .views import HomePageVIew, AboutPageVIew

urlpatterns = [
    path("", HomePageVIew.as_view(), name="home"),
    path("about/", AboutPageVIew.as_view(), name="about"),
]
