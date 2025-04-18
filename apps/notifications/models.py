from mongoengine import Document, StringField, EnumField
import enum


class MediumEnum(enum.Enum):
    EMAIL = "email"
    TELEGRAM = "telegram"
    SMS = "sms"


class StatusEnum(enum.Enum):
    PENDING = "pending"
    FAILED = "failed"
    SUCCESS = "success"
    STARTED = "started"


class NotificationLog(Document):
    task_id = StringField(required=True, unique=True)
    medium = EnumField(MediumEnum, required=True)
    status = EnumField(StatusEnum, required=True, default=StatusEnum.PENDING)
    message = StringField(required=True)
    recipient = StringField(required=True)

    meta = {
        'collection': 'notification_logs',
        'indexes': ['task_id', 'status']
    }
