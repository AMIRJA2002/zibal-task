from .base import NotificationSender

class SMSSender(NotificationSender):
    def send(self, recipient: str, message: str) -> bool:
        print(f"[SMS] به {recipient} با پیام: {message}")
        return True
