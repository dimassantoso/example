import requests

from config.config import Config
from tasks.tasks import update_logs

if __name__ == "__main__":
    r = requests.get(Config.ACTIVITY_HOST +
                     "/v2/logs?orderBy=created&sort=desc&limit={}&phrase[module]={}&dateFrom={}&dateTo={}"
                     .format(Config.LIMIT, Config.MODULE, Config.START_DATE, Config.END_DATE),
                     headers=Config.HEADER,
                     timeout=5)

    data = r.json()["data"]

    count_update = 0
    total_data = 0
    try:
        for i in data:
            total_data += 1
            id = str(i.get("_id"))
            logs = i.get("logs", [])
            logs_date = next(filter(lambda obj: obj.get("field") == "Date", logs), {})

            if "+07:00" in logs_date.get("newValue") or logs_date.get("newValue") == "":
                continue

            logs_date["newValue"] = logs_date["newValue"].replace("Z", "+07:00")
            update_logs.delay(id, logs)
    except Exception as e:
        print(e)

    print("SELESAI CUK")
    print("Total Data : {}".format(total_data))
    print("Total Update : {}".format(count_update))
