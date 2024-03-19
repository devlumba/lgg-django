from django.forms import forms
from .models import FeedbackPost


class FeedbackForm(forms.Form):
    class Meta:
        model = FeedbackPost
        fields = ["name", "email", "content"]
