from django.forms import ModelForm

from .models import Surveyor

class SurveyorForm(ModelForm):
    class Meta:
        model = Surveyor
        # fields = "__all__"
        exclude = ["slug"]
        labels = {
            "name": "Name",
            "sales_region": "Sales Region",
            "telephone_no": "Telephone No.",
            "mobile_no": "Mobile No.",
            "alt_telephone_no": "Alternate Telephone No.",
            "email_address": "eMail Address",
        }
        error_messages = {
            "name": {
                "required": "Please enter a surveyor name",
                "max_length": "Please enter a shorter surveyor name"
            }
        }