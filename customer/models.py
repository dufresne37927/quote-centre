from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True)
    address3 = models.CharField(max_length=100, blank=True)
    town = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    post_code = models.CharField(max_length=12)
    contact_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=254, blank=True)
    telephone_no = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=20, blank=True)
    alt_telephone_no = models.CharField(max_length=20, blank=True)

    def get_absolute_url(self):
        return reverse("customer-detail", args=[self.id])

    def __str__(self):
        return self.name