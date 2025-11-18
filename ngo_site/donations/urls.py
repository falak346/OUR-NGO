from django.urls import path
from .views import donate, thanks

urlpatterns = [
    path("", donate, name="donate"),
    path("thanks/", thanks, name="donation_thanks"),
]
