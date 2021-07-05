from main.celery import app
from django.conf import settings
from django.core.mail import send_mail
from .models import ConfirmationCode, MainUser

@app.task()
def send_verify_url(text,email):
    send_mail('shop api', text, settings.EMAIL_FROM, [email,],fail_silently=True)


@app.task()
def code_expired(code_id: int):
    ConfirmationCode.objects.get(id=code_id).delete()


@app.task()
def user_expired(user_id: int):
    user = MainUser.objects.get(id = user_id)
    if user.active == False:
        user.delete()
    
