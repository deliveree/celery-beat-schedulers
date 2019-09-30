from celery import Celery

app = Celery('tasks')

@app.task
def task_1():
    print("task_1")

@app.task
def run():
    print("Hello")

app.conf.update(
    redbeat_redis_url = "redis://localhost:6379/1"
    # CELERY_REDIS_SCHEDULER_URL = 'redis://localhost:6379/1'
)

app.conf.beat_schedule = {}
for num in range(50):
    task_name = "task_" + str(num)
    app.conf.beat_schedule[task_name] = {
        "task": 'main.run',
        "schedule": 1
    }
