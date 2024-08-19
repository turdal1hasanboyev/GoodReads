from django.core.mail import EmailMessage

from celery import shared_task


@shared_task
def send_email(subject, message, to_email):
    email = EmailMessage(to=[to_email], subject=subject, body=message)
    email.send()
    