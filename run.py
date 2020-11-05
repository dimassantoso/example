import pymongo
from datetime import datetime
from config.config import Config
from connector import connect_mongo
from tasks.tasks import update_logs

if __name__ == "__main__":
    db = connect_mongo()
    source = db[Config.MONGO_COLLECTION]

    start = datetime.strptime("2020-10-20", "%Y-%m-%d")
    end = datetime.strptime("2020-11-01", "%Y-%m-%d")
    source = source.find({
        "module": "ORDER-TRACKING",
        "pack": {
            "$in": ["Barracuda", "Pyrosoma", "Marlin", "Unicornfish"]
        },
        "created": {
            "$gte": start, "$lt": end
        }
    }, sort=[('_id', pymongo.DESCENDING)])

    processed = 0
    to_queue = 0
    skipped = 0
    try:
        for i in source:
            id = str(i.get("id"))
            logs = i.get("logs", [])
            logs_date = next(filter(lambda obj: obj.get("field") == "Date", logs), {})

            if "+07:00" in logs_date.get("newValue"):
                continue

            logs_date["newValue"] = logs_date["newValue"].replace("Z", "+07:00")
            update_logs.delay(id, logs)
    except Exception as e:
        print(e)

    print("SELESAI CUK")
    print("processed:", processed)
    print("to_queue", to_queue)
    print("skipped", skipped)
