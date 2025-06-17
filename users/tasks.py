from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.core.exceptions import ImproperlyConfigured
@shared_task
def send_custom_mail(user_mail,username,password):
        from_email = settings.EMAIL_HOST_USER
        subject = "Account Successfully created"
        message = message = (
    f"Dear User,\n\n"
    f"Congratulations! You have successfully registered on our website.\n\n"
    f"Here are your login credentials:\n"
    f"  - Username: {username}\n"
    f"  - Password: {password}\n"
    f"  - Email: {user_mail}\n\n"
    f"You can now log in and start using our services.\n"
    f"If you did not register for this account, please ignore this message.\n\n"
)

        if not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD:
            raise ImproperyConfigured("Email host user/password not configured.")
        recipient_list = [user_mail]
        return send_mail(
            subject=subject,
            message=message,
            from_email = from_email,
            recipient_list = recipient_list,
            fail_silently = False
        )
