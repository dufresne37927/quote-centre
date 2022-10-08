from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class WelcomeView(LoginRequiredMixin, TemplateView):
    template_name = "core/welcome.html"

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('welcome')
        else:
            return redirect('welcome')
    return render(request, 'core/home.html')