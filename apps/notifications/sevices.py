from apps.notifications.factory.factory import NotificationFactory
from .tasks import send_notification_task
from celery.result import AsyncResult


def send_notification(medium: list, recipient: str, message: str) -> None:
    """
        Available Mediums [email, telegram, sms]
    """
    for med in medium:
        send_notification_task.delay(med, recipient, message)
