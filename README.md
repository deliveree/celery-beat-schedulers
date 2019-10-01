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
