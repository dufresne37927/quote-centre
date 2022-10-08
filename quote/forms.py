from django.forms import ModelForm
from django import forms

from .models import Quote
from .widgets import DatePickerInput

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = "__all__"
        labels = {
            "customer": "Customer",
            "reference": "Quote Reference No.",
            "system_type": "System Type",
            "description": "System Description",
            "premises_type": "Premises Type",
            "surveyor": "Surveyor",
            "quote_status": "Quote Status",
            "remarks": "Remarks",
            "creation_date": "Creation Date",
            "quotation_date": "Quotation Date",
            "valid_until": "Valid Until Date",
            "last_modified": "Last Modified Date",
            "quote_sale_value": "Sale Value",
        }
        error_messages = {
            "customer": {
                "required": "Please select a customer",
            },
            "reference": {
                "required": "Please enter a customer reference no.",
                "max_length": "Please enter a shorter customer reference no."
            }
        }
        widgets = {
            "quotation_date" : DatePickerInput(),
            "valid_until" : DatePickerInput(),
        }

class QuoteAddFromCustomerForm(QuoteForm):
    class Meta(QuoteForm.Meta):
        exclude = ["customer",]

class QuoteAddFromSurveyorForm(QuoteForm):
    class Meta(QuoteForm.Meta):
        exclude = ["surveyor",]