from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# Custom user class with is_admin flag
# See reference in readme for acknowledgement
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Regular(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username