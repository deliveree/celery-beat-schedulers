## Run redis server
redis-server --daemonize yes

## Run rabbit-mpq
rabbitmq-server -detached

## PersistentScheduler
celery beat -A main -l INFO

## redisbeat
celery beat -A main -S redisbeat.RedisScheduler -l INFO

## redbeat
celery beat -A main -S redbeat.RedBeatScheduler -l INFO

### Run update task example
celery beat -A update_task_redbeat -S redbeat.RedBeatScheduler -l INFO
celery -A update_task_redbeat worker -l INFO --concurrency=2