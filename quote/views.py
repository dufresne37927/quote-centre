from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class WelcomeView(TemplateView):
    template_name = "quote/welcome.html"