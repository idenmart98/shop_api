from django.conf import settings
from django.core.mail import send_mail

def send_verify_url(text,email):
    send_mail('shop api', text, settings.EMAIL_FROM, [email,],fail_silently=True)




