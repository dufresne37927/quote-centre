from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomerForm
from .models import Customer

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('welcome')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class WelcomeView(LoginRequiredMixin, TemplateView):
    template_name = "customer/welcome.html"

class CustomerListView(LoginRequiredMixin, ListView):
    template_name = "customer/customer-list.html"
    model = Customer
    context_object_name = "customers"

class CustomerDetailView(LoginRequiredMixin, DetailView):
    template_name = "customer/customer-detail.html"
    model = Customer

class CustomerAddView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer/customer-add.html"
    success_url = "/customer"

class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = "customer/customer-delete.html"
    success_url = "/customer"
    
class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer/customer-add.html"
    success_url = "/customer"