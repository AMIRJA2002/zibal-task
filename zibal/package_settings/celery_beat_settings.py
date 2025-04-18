from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'check_pending_notifications_every_one_minutes': {
        'task': 'apps.notifications.tasks.check_pending_notifications',
        'schedule': crontab(minute='*'),
    },
    'retry_failed_notifications_every_one_minutes': {
        'task': 'apps.notifications.tasks.retry_failed_notifications',
        'schedule': crontab(minute='*'),
    },
}
