from celery import shared_task
from .factory.factory import NotificationFactory

@shared_task
def send_notification_task(medium: str, recipient: str, message: str,):
    medium_class = NotificationFactory.get_sender(medium)
    instance = medium_class()
    instance.send(recipient, message)

