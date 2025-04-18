from .base import NotificationSender
from django.core.mail import send_mail


class EmailSender(NotificationSender):
    def send(self, recipient: str, message: str) -> bool:
        print(f"[EMAIL] به {recipient} با پیام: {message}", 400 * '*')
        send_mail(
            'تست ارسال',
            message,
            'amirjas8177@gmail.com',
            [recipient,],
            fail_silently=False,
        )
        return True
