from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from .forms import SurveyorForm
from .models import Surveyor
from quote.forms import QuoteAddFromSurveyorForm
from quote.models import Quote
from core.decorators import admin_required

# Create your views here.

class SurveyorListView(LoginRequiredMixin, ListView):
    template_name = "surveyor/surveyor-list.html"
    model = Surveyor
    context_object_name = "surveyors"

class SurveyorDetailView(LoginRequiredMixin, DetailView):
    template_name = "surveyor/surveyor-detail.html"
    model = Surveyor
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

class SurveyorAddView(LoginRequiredMixin, CreateView):
    model = Surveyor
    form_class = SurveyorForm
    template_name = "surveyor/surveyor-add.html"
    success_url = "/surveyor"

@method_decorator([admin_required], name='dispatch')
class SurveyorDeleteView(LoginRequiredMixin, DeleteView):
    model = Surveyor
    template_name = "surveyor/surveyor-delete.html"
    success_url = "/surveyor"
    
class SurveyorUpdateView(LoginRequiredMixin, UpdateView):
    model = Surveyor
    form_class = SurveyorForm
    template_name = "surveyor/surveyor-add.html"
    success_url = "/surveyor"

class SurveyorAddQuoteView(LoginRequiredMixin, CreateView):
    model = Quote
    form_class = QuoteAddFromSurveyorForm
    template_name = "quote/quote-add-from-surveyor.html"
    success_url = "/surveyor"
    

    def get_success_url(self):
        surveyor_slug=self.kwargs['slug']
        return reverse_lazy('surveyor-detail', kwargs={'slug': surveyor_slug})

    def form_valid(self, form):
        form.instance.surveyor_slug = self.kwargs["slug"]
        return super().form_valid(form)