from mongoengine import DoesNotExist

from .factory.factory import NotificationFactory
from celery.result import AsyncResult
from zibal.celery import app
from celery import shared_task

from .models import StatusEnum, NotificationLog, MediumEnum


@shared_task
def send_notification_task(medium: str, recipient: str, message: str, ):
    medium_class = NotificationFactory.get_sender(medium)
    instance = medium_class()
    instance.send(recipient, message)


@shared_task
def save_notification_log(task_id: str, medium: str, recipient: str, message: str):
    result = AsyncResult(task_id, app=app)

    status_map = {
        'PENDING': StatusEnum.PENDING,
        'STARTED': StatusEnum.STARTED,
        'SUCCESS': StatusEnum.SUCCESS,
        'FAILURE': StatusEnum.FAILED,
    }

    status = status_map.get(str(result.status), StatusEnum.PENDING)

    try:
        log = NotificationLog.objects.get(task_id=task_id)
        log.update(
            status=status,
            message=message,
            recipient=recipient,
            medium=MediumEnum(medium)
        )
    except DoesNotExist:
        NotificationLog(
            task_id=task_id,
            medium=MediumEnum(medium),
            status=status,
            message=message,
            recipient=recipient
        ).save()
