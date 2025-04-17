from .base import NotificationSender

class TelegramSender(NotificationSender):
    def send(self, recipient: str, message: str) -> bool:
        print(f"[TELEGRAM] به {recipient} با پیام: {message}")
        return True
