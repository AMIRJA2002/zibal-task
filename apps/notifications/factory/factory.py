from .email import EmailSender
from .sms import SMSSender
from .telegram import TelegramSender
from .base import NotificationSender

class NotificationFactory:
    @staticmethod
    def get_sender(medium: str) -> NotificationSender:

        mediums = {
            'email': EmailSender,
            'sms': SMSSender,
            'telegram': TelegramSender,
        }
        medium = medium.lower()

        try:
            return mediums[medium]()
        except ValueError as e:
            raise f"Unsupported medium: {medium}, {e}"
