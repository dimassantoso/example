import pymongo
from datetime import datetime
from config.config import Config
from connector import connect_mongo
from tasks.tasks import update_logs

if __name__ == "__main__":
    db = connect_mongo()
    source = db[Config.MONGO_COLLECTION]

    start = datetime.strptime(Config.START_DATE, "%Y-%m-%d")
    end = datetime.strptime(Config.END_DATE, "%Y-%m-%d")
    source = source.find({
        "module": Config.MODULE,
        "pack": {
            "$in": Config.PACK
        },
        "created": {
            "$gte": start, "$lt": end
        }
    }, sort=[('_id', pymongo.DESCENDING)])

    count_update = 0
    try:
        for i in source:
            id = str(i.get("id"))
            logs = i.get("logs", [])
            logs_date = next(filter(lambda obj: obj.get("field") == "Date", logs), {})

            if "+07:00" in logs_date.get("newValue") or logs_date.get("newValue")=="":
                continue

            count_update += 1
            logs_date["newValue"] = logs_date["newValue"].replace("Z", "+07:00")
            update_logs.delay(id, logs)
    except Exception as e:
        print(e)

    print("SELESAI CUK")
    print("Total Update : {}".format(count_update))