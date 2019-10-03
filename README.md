## Run redis server
redis-server --daemonize yes

## Run rabbitmpq
rabbitmq-server -detached

## Update data in Redis stored by RedBeat
Make sure redis and rabbitmpq are running.
Run beat and worker from update_task_redbeat.py

```
celery beat -A update_task_redbeat -S redbeat.RedBeatScheduler -l INFO
celery -A update_task_redbeat worker -l INFO --concurrency=2
```

Please check metadata_redbeat_update.py  on how to update meta data, scheduler and delete existing task.
