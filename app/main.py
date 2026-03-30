import uuid

@app.post("/add-task")
def add_task(data: str):
    task_id = str(uuid.uuid4())

    task = {
        "id": task_id,
        "data": data,
        "status": "pending"
    }

    r.lpush("task_queue", json.dumps(task))
    r.set(task_id, json.dumps(task))

    return {"task_id": task_id}
@app.get("/task-status/{task_id}")
def get_status(task_id: str):
    task = r.get(task_id)
    return json.loads(task) if task else {"error": "Not found"}
    
