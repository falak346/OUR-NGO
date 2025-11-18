from django.shortcuts import render
from blog.models import Post
from events.models import Event

def home(request):
    latest_posts = Post.objects.order_by("-published_at")[:5]
    upcoming_events = Event.objects.order_by("start_date")[:5]
    return render(request, "home.html", {"latest_posts": latest_posts, "upcoming_events": upcoming_events})

def about(request):
    return render(request, "about.html")

def contact(request):
    sent = False
    if request.method == "POST":
        # For MVP we just show a 'sent' message. Configure email in settings to actually send.
        sent = True
    return render(request, "contact.html", {"sent": sent})
