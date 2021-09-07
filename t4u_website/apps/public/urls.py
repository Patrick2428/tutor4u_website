from django.urls import path

# local directory
from . import views

app_name = "public"
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("service", views.service, name="service"),
]
