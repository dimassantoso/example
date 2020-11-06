import requests

from config.config import Config
from tasks.tasks import update_logs

if __name__ == "__main__":
    total_data = 0
    count_update = 0
    try:
        for page in range(1, Config.PAGE+1):
            r = requests.get(Config.ACTIVITY_HOST +
                             "/v2/logs?limit={}&page={}&phrase[module]={}&dateFrom={}&dateTo={}"
                             .format(Config.LIMIT, page, Config.MODULE, Config.START_DATE, Config.END_DATE),
                             headers=Config.HEADER,
                             timeout=100)

            data = r.json()["data"]
            total_data += len(data)

            if total_data == 0:
                print("SELESAI")
                break

            for i in data:
                id = str(i.get("_id"))
                logs = i.get("logs", [])
                logs_date = next(filter(lambda obj: obj.get("field") == "Date", logs), {})

                if "+07:00" in logs_date.get("newValue") or logs_date.get("newValue") == "":
                    continue

                logs_date["newValue"] = logs_date["newValue"].replace("Z", "+07:00")
                update_logs.delay(id, logs)
                count_update += 1
    except Exception as e:
        print(e)

    print("SELESAI CUK")
    print("Total Data : {}".format(total_data))
    print("Total Update : {}".format(count_update))
