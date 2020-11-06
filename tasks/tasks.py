import requests

from config.config import Config
from run_celery import CELERY


@CELERY.task(bind=True, max_retries=5)
def update_logs(self, id, logs):
    max_retries = self.max_retries
    try:
        payload = {
            "logs": logs
        }
        r = requests.put(
            Config.ACTIVITY_HOST + "/v2/logs/{}".format(id),
            json=payload,
            headers=Config.HEADER,
            timeout=10
        )

        if r.status_code == 200:
            return r.json()["message"]
        raise Exception(r.json())

    except Exception as e:
        retries = self.request.retries
        delay = 2.0 if retries < 6 else 2.0 ** retries
        self.retry(exc=e, countdown=delay, max_retries=max_retries)
