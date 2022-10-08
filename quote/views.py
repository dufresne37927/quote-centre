from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import QuoteForm
from .models import Quote

# Create your views here.

class QuoteListView(LoginRequiredMixin, ListView):
    template_name = "quote/quote-list.html"
    model = Quote
    context_object_name = "quotes"

class QuoteDetailView(LoginRequiredMixin, DetailView):
    template_name = "quote/quote-detail.html"
    model = Quote

class QuoteAddView(LoginRequiredMixin, CreateView):
    model = Quote
    form_class = QuoteForm
    template_name = "quote/quote-add.html"
    success_url = "/quote"

class QuoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Quote
    template_name = "quote/quote-delete.html"
    success_url = "/quote"
    
class QuoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Quote
    form_class = QuoteForm
    template_name = "quote/quote-add.html"
    success_url = "/quote"