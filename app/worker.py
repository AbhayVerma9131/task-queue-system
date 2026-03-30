import redis
import json
from tasks import process_task

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

print("Worker started...")

while True:
    task = r.brpop("task_queue")
    if task:
        _, task_data = task
        task_json = json.loads(task_data)

        result = process_task(task_json["data"])
        print("Processed:", result).
