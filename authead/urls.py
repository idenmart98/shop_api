from authead.serializers import EmailRegistrationSerializer
from sys import version
from django.urls import path
from . import views


urlpatterns = [
    path('email/' ,views.EmailRegistrationView.as_view())
]