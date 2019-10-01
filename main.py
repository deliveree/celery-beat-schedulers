from celery import Celery
from time import sleep

app = Celery('tasks')

@app.task
def task_1():
    print("task_1")

app.conf.update(
    redbeat_redis_url="redis://localhost:6379/1",
    broker_url="amqp://@localhost:5672",
    # CELERY_REDIS_SCHEDULER_URL = 'redis://localhost:6379/1',
    # CELERY_REDIS_SCHEDULER_KEY_PREFIX = 'tasks:meta:'
)

app.conf.beat_schedule = {}
for num in range(1000):
    task_name = "task_" + str(num)
    app.conf.beat_schedule[task_name] = {
        "task": 'main.run',
        "schedule": 1
    }
