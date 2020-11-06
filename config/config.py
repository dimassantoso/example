from decouple import config


class Config:
    CELERY_BROKER = config("CELERY_BROKER")
    CELERY_BACKEND = config("CELERY_BACKEND")
    CELERY_RESULT_EXPIRED = config("CELERY_RESULT_EXPIRED")
    ACTIVITY_HOST = config("ACTIVITY_HOST")
    ACTIVITY_TOKEN = config("ACTIVITY_TOKEN")
    START_DATE = config("START_DATE")
    END_DATE = config("END_DATE")
    PACK = config("PACK").split(",")
    MODULE = config("MODULE")
    LIMIT = config("LIMIT")
    HEADER = {
        "Content-Type": "application/json",
        'Authorization': "Bearer {}".format(ACTIVITY_TOKEN)
    }
