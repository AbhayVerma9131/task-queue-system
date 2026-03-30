from fastapi import FastAPI
import redis
import json

app = FastAPI()

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

@app.post("/add-task")
def add_task(data: str):
    task = {"data": data}
    r.lpush("task_queue", json.dumps(task))
    return {"status": "Task added to queue"}
