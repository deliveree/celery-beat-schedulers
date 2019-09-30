
## PersistentScheduler
celery beat -A main

## redisbeat
celery beat -A main -S redisbeat.RedisScheduler -l INFO

## redbeat
celery beat -A main -S redbeat.RedBeatScheduler -l INFO