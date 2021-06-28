from authead.serializers import EmailRegistrationSerializer
from sys import version
from django.urls import path
from . import views


urlpatterns = [
    path('email/' ,views.EmailRegistrationView.as_view()),
    path('email_verify/<str:code>', views.confirm_email),
]