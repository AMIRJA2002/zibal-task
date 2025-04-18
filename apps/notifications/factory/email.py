from .base import NotificationSender

class EmailSender(NotificationSender):
    def send(self, recipient: str, message: str) -> bool:
        print(f"[EMAIL] به {recipient} با پیام: {message}", 400 * '*')
        return True
