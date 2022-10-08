from django.urls import path

from . import views

urlpatterns = [
    path("surveyor/", views.SurveyorListView.as_view(), name="surveyor-list"),
    path("surveyor/add", views.SurveyorAddView.as_view(), name="surveyor-add"),
    path("surveyor/<slug:slug>", views.SurveyorDetailView.as_view(), name="surveyor-detail"),
    path("surveyor/<slug:slug>/delete", views.SurveyorDeleteView.as_view(), name="surveyor-delete"),
    path("surveyor/<slug:slug>/update", views.SurveyorUpdateView.as_view(), name="surveyor-update"),
    path("surveyor/<slug:slug>/addquote", views.SurveyorAddQuoteView.as_view(), name="surveyor-add-quote"),
]