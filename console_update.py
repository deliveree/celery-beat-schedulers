# Demonstrate how to update data in redis beat so worker can pickup updated data without restarting the beat
# Run those command first:
# celery beat -A update_task_redbeat -S redbeat.RedBeatScheduler -l INFO
# celery -A update_task_redbeat worker -l INFO --concurrency=2

# Then in python console, use these to update

from datetime import timedelta
import update_task_redbeat
from redbeat import RedBeatSchedulerEntry as Entry
from celery.schedules import schedule

app = update_task_redbeat.app
e = Entry.from_key('redbeat:task_259',  app=app)

# Update schedule to 5 seconds
e.schedule = schedule(5)
e.save()

# Update metadata to print Goodbye instead of Hello
# We simply change the args passed to the task
e.args = ["Goodbye"]
e.save()

# Delete task
e.delete()