from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ["name", "email", "amount", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
        }
