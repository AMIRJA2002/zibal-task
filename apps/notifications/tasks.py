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


@shared_task
def check_pending_notifications():
    pending_logs = NotificationLog.objects(status=StatusEnum.PENDING)

    for log in pending_logs:
        result = AsyncResult(log.task_id, app=app)
        status_mapping = {
            'SUCCESS': StatusEnum.SUCCESS,
            'FAILURE': StatusEnum.FAILED,
            'PENDING': StatusEnum.PENDING,
        }

        if result.status == 'PENDING':
            continue

        new_status = status_mapping.get(str(result.status), StatusEnum.FAILED)
        log.status = new_status
        log.save()



@shared_task
def retry_failed_notifications():
    failed_logs = NotificationLog.objects(status=StatusEnum.FAILED)

    for log in failed_logs:
        try:
            send_notification_task.delay(log.medium.value, log.recipient, log.message)
            log.status = StatusEnum.PENDING
            log.save()

        except Exception as e:
            print(f"Error retrying notification for task {log.task_id}: {e}")
            log.status = StatusEnum.FAILED
            log.save()
