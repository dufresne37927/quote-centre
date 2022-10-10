from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from core.models import (Regular, User)

class RegularSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = False
        user.save()
        regular = Regular.objects.create(user=user)
        return user

class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        user.is_staff = True
        if commit:
            user.save()
        return user