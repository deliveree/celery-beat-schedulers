from celery import Celery

app = Celery('tasks')

app.conf.update(
    redbeat_redis_url="redis://localhost:6379/1",
    broker_url="amqp://@localhost:5672"
)

@app.task
def print_content(text):
    print(text)

app.conf.beat_schedule = {
    "print_content": {
        "task": 'update_task_redbeat.print_content',
        "schedule": 1,
        "args": ("Hello",)
    }
}
