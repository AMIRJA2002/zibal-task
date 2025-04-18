from apps.notifications.factory.factory import NotificationFactory
from .tasks import send_notification_task, save_notification_log
from celery.result import AsyncResult


def send_notification(medium: list, recipient: str, message: str) -> None:
    """
        Available Mediums [email, telegram, sms]
    """
    for med in medium:
        task = send_notification_task.delay(med, recipient, message)
        save_notification_log.delay(task.id, med, recipient, message)
