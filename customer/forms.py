from django.forms import ModelForm

from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        labels = {
            "name": "Customer Name",
            "address1": "Address Line 1",
            "address2": "Address Line 2",
            "address3": "Address Line 3",
            "town": "Town",
            "county": "County",
            "post_code": "Post Code",
            "contact_name": "Contact Name",
            "email_address": "eMail Address",
            "telephone_no": "Telephone No.",
            "mobile_no": "Mobile No.",
            "alt_telephone_no": "Alternate Telephone No.",
        }
        error_messages = {
            "name": {
                "required": "A customer name is required",
                "max_length": "Please enter a shorter customer name"
            }
        }