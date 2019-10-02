from celery import Celery

app = Celery('tasks')
app.config_from_object('confs.redbeat')


@app.task
def print_content(text):
    print(text)

# def update_task(content):

app.conf.beat_schedule = {
    "print_content": {
        "task": 'update_task_redbeat.print_content',
        "schedule": 1,
        "args": ("Hello",)
    }
}
