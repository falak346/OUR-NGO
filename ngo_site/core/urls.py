from django.urls import path
from .views import home, about, contact

#13/11
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    #13/11
    path('login/', RedirectView.as_view(url='/accounts/login/')),

]
