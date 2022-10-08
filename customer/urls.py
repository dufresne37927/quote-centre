from django.urls import path


from . import views

urlpatterns = [
    path("customer/", views.CustomerListView.as_view(), name="customer-list"),
    path("customer/add", views.CustomerAddView.as_view(), name="customer-add"),
    path("customer/<int:pk>", views.CustomerDetailView.as_view(), name="customer-detail"),
    path("customer/<int:pk>/delete", views.CustomerDeleteView.as_view(), name="customer-delete"),
    path("customer/<int:pk>/update", views.CustomerUpdateView.as_view(), name="customer-update"),
    path("customer/<int:pk>/addquote", views.CustomerAddQuoteView.as_view(), name="customer-add-quote"),
]
