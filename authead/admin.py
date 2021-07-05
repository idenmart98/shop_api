from django.contrib import admin
from .models import MainUser, ConfirmationCode

# Register your models here.
admin.site.register(MainUser)
admin.site.register(ConfirmationCode)
