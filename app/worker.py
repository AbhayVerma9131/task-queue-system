while True:
    task = r.brpop("task_queue")

    if task:
        _, task_data = task
        task_json = json.loads(task_data)

        task_json["status"] = "processing"
        r.set(task_json["id"], json.dumps(task_json))

        result = process_task(task_json["data"])

        task_json["status"] = "completed"
        task_json["result"] = result

        r.set(task_json["id"], json.dumps(task_json))

        print("Done:", result)
