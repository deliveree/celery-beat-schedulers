# The file is to test the speed of 2 schedulers by running 1000 tasks, which are scheduled to run every 1 second.

from celery import Celery
from time import sleep

app = Celery('tasks')


@app.task
def task_1():
    print("task_1")

# Uncomment this to use redbeat as scheduler instead of PersistentScheduler
# app.conf.update(
#     redbeat_redis_url="redis://localhost:6379/1",
# )

app.conf.beat_schedule = {}
for num in range(1000):
    task_name = "task_" + str(num)
    app.conf.beat_schedule[task_name] = {
        "task": 'main.run',
        "schedule": 1
    }
