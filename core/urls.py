from django.urls import include, path

from . import views
from core.views import core, admin, regular

urlpatterns = [
    path("", core.home, name="home"),
    path("", core.WelcomeView.as_view(), name="welcome"),
    path("welcome", core.WelcomeView.as_view(), name="welcome"),
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/signup", core.SignUpView.as_view(), name="signup"),
    path("accounts/signup/admin", admin.AdminSignUpView.as_view(), name="admin-signup"),
    path("accounts/signup/regular", regular.RegularSignUpView.as_view(), name="regular-signup"),
]