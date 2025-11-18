from django.contrib import admin
from django.urls import path, include
from core.views import home, about, contact

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("donate/", include("donations.urls")),
    path("blog/", include("blog.urls")),
    path("events/", include("events.urls")),
    #13/11
    path('accounts/', include('django.contrib.auth.urls')),
]
