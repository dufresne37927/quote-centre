from django.db import models
from django.db.models import Sum
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from customer.models import Customer
from surveyor.models import Surveyor

# Create your models here.

class Quote(models.Model):
    reference = models.CharField(max_length=50)
    class SystemType(models.TextChoices):
        INTRUDER_ALARM = "IA", _("Intruder Alarm")
        FIRE_ALARM = "FA", _("Fire Alarm")
        ACCESS_CONTROL = "AC", _("Access Control")
        CCTV = "CC", _("CCTV System")
        FIRE_EXTINGUISHERS = "FE", _("Fire Extinguishers")
        OTHER = "OT", _("Other")
    system_type = models.CharField(
        max_length = 2,
        choices = SystemType.choices,
        default = SystemType.INTRUDER_ALARM,
    )
    description = models.TextField(blank=True)
    class PremisesType(models.TextChoices):
        DOMESTIC = "DO", _("Domestic System")
        COMMERCIAL = "CO", _("Commercial System")
        OTHER = "OT", _("Other")
    premises_type = models.CharField(
        max_length = 2,
        choices = PremisesType.choices,
        default = PremisesType.COMMERCIAL,
    )
    class Status(models.TextChoices):
        OPEN = "OP", _("Open")
        CLOSED = "CL", _("Closed")
        CONVERTED = "CO", _("Converted")
    quote_status = models.CharField(
        max_length = 2,
        choices = Status.choices,
        default = Status.OPEN,
    )
    remarks = models.CharField(max_length=320, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    quotation_date = models.DateField()
    valid_until = models.DateField()
    last_modified = models.DateField(auto_now=True)
    quote_sale_value = models.DecimalField(
        max_digits = 19,
        decimal_places = 2,
        validators = [MinValueValidator(0.00)]
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="quotes")
    surveyor = models.ForeignKey(Surveyor, null=True, on_delete=models.SET_NULL, related_name="quotes")
    
    def get_absolute_url(self):
        return reverse("quote-detail", args=[self.id])

    def __str__(self):
        return "%s (id: %s, customer: %s)" %(self.reference, self.id, self.customer.name,)