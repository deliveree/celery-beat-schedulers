# Demonstrate how to update data in redis beat so worker can pickup updated data without restarting the beat
# Run those command first:
# celery beat -A update_task_redbeat -S redbeat.RedBeatScheduler -l INFO
# celery -A update_task_redbeat worker -l INFO --concurrency=2

# Then in python console, use these to update

import update_task_redbeat
from redbeat import RedBeatSchedulerEntry as Entry
from celery.schedules import crontab

app = update_task_redbeat.app
e = Entry.from_key('redbeat:task_259',  app=app)

# Update schedule
e.schedule = crontab(minute=1)
e.save()

# Update metadata
e.content = "Goodbye"
e.save()

# Delete task
e.delete()