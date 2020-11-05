from decouple import config


class Config:
    MONGO_HOST = config("MONGO_HOST")
    MONGO_DB = config("MONGO_DB")
    MONGO_COLLECTION = config("MONGO_COLLECTION")
    CELERY_BROKER = config("CELERY_BROKER")
    CELERY_BACKEND = config("CELERY_BACKEND")
    CELERY_RESULT_EXPIRED = config("CELERY_RESULT_EXPIRED")
    ACTIVITY_HOST = config("ACTIVITY_HOST")
    ACTIVITY_TOKEN = config("ACTIVITY_TOKEN")
