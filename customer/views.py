from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import CustomerForm
from .models import Customer
from quote.forms import QuoteAddFromCustomerForm
from quote.models import Quote

# Create your views here.

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

class CustomerAddQuoteView(LoginRequiredMixin, CreateView):
    model = Quote
    form_class = QuoteAddFromCustomerForm
    template_name = "quote/quote-add-from-customer.html"
    success_url = "/customer"
    

    def get_success_url(self):
        customer_id=self.kwargs['pk']
        return reverse_lazy('customer-detail', kwargs={'pk': customer_id})

    def form_valid(self, form):
        form.instance.customer_id = self.kwargs["pk"]
        return super().form_valid(form)