from django.urls import path

from . import views

urlpatterns = [
    path("quote/", views.QuoteListView.as_view(), name="quote-list"),
    path("quote/add", views.QuoteAddView.as_view(), name="quote-add"),
    path("quote/<int:pk>", views.QuoteDetailView.as_view(), name="quote-detail"),
    path("quote/<int:pk>/delete", views.QuoteDeleteView.as_view(), name="quote-delete"),
    path("quote/<int:pk>/update", views.QuoteUpdateView.as_view(), name="quote-update"),
]