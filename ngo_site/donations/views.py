from django.shortcuts import render, redirect
from .forms import DonationForm

def donate(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("donation_thanks")
    else:
        form = DonationForm()
    return render(request, "donations/donate.html", {"form": form})

def thanks(request):
    return render(request, "donations/thanks.html")
