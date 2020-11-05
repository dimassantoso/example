from celery import Celery
from config.celery_config import CeleryQueueConfig
from config.config import Config

CELERY = Celery("activity-log-migration",
                broker=Config.CELERY_BROKER,
                backend=Config.CELERY_BACKEND)

CELERY.conf.task_queues = CeleryQueueConfig.QUEUES
CELERY.conf.task_routes = CeleryQueueConfig.ROUTES
CELERY.conf.result_expires = Config.CELERY_RESULT_EXPIRED

CELERY.autodiscover_tasks(packages=['tasks.tasks'], force=True)

CELERY.conf.timezone = "Asia/Jakarta"
CELERY.conf.enable_utc = False