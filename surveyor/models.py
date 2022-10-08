from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from core.utils import unique_slug_generator

# Create your models here.

class Surveyor(models.Model):
    slug = models.SlugField(null = False, unique = True)
    name = models.CharField(max_length=100)
    class SalesRegion(models.TextChoices):
        SCOTLAND = "SC", _("Scotland")
        NORTHERN_IRELAND = "NI", _("Northern Ireland")
        NORTH_EAST = "NE", _("North East")
        NORTH_WEST = "NW", _("North West")
        EAST_MIDLANDS = "EM", _("East Midlands")
        WEST_MIDLANDS = "WM", _("West Midlands")
        WALES = "WA", _("Wales")
        SOUTH_WEST = "SW", _("South West")
        SOUTH_EAST = "SE", _("South East")
        GREATER_LONDON = "GL", _("Greater London")
    sales_region = models.CharField(
        max_length = 2,
        choices = SalesRegion.choices,
        default = SalesRegion.GREATER_LONDON,
    )
    telephone_no = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=20, blank=True)
    alt_telephone_no = models.CharField(max_length=20, blank=True)
    email_address = models.EmailField(max_length=254, blank=True)

    def get_absolute_url(self):
        return reverse("surveyor-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return "%s (id: %s)" %(self.name, self.slug,)
        

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Surveyor)