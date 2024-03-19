from django.shortcuts import render
from .forms import FeedbackForm
from .models import FeedbackPost
from django.views.generic import CreateView


def home(request):
    return render(request, template_name="wiki/base.html")


def about(request):
    return render(request, template_name="wiki/about.html")


def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, template_name="wiki/feedback_form.html")
    else:
        form = FeedbackForm


class FeedbackPostCreateView(CreateView):
    model = FeedbackPost
    fields = ['name', 'email', 'content']
    template_name = 'wiki/feedback_form.html'

    def form_valid(self, form):
        return super().form_valid(form)
#     feedback is not complete, should finish later
