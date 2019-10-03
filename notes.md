Logs within 5 mins running beat

## PersistentScheduler:

### Logs
[2019-10-01 17:08:50,567: INFO/MainProcess] Scheduler: Sending due task task_190 (main.run)
[2019-10-01 17:08:50,573: INFO/MainProcess] Scheduler: Sending due task task_982 (main.run)
[2019-10-01 17:08:50,579: INFO/MainProcess] Scheduler: Sending due task task_825 (main.run)
[2019-10-01 17:08:50,585: INFO/MainProcess] Scheduler: Sending due task task_182 (main.run)
[2019-10-01 17:08:50,591: INFO/MainProcess] Scheduler: Sending due task task_707 (main.run)
[2019-10-01 17:08:50,598: INFO/MainProcess] Scheduler: Sending due task task_425 (main.run)
[2019-10-01 17:08:50,604: INFO/MainProcess] Scheduler: Sending due task task_275 (main.run)
[2019-10-01 17:08:50,611: INFO/MainProcess] Scheduler: Sending due task task_716 (main.run)
[2019-10-01 17:08:50,617: INFO/MainProcess] Scheduler: Sending due task task_230 (main.run)
[2019-10-01 17:08:50,625: INFO/MainProcess] Scheduler: Sending due task task_815 (main.run)
[2019-10-01 17:08:50,632: INFO/MainProcess] Scheduler: Sending due task task_106 (main.run)
[2019-10-01 17:08:50,637: INFO/MainProcess] Scheduler: Sending due task task_237 (main.run)
[2019-10-01 17:08:50,644: INFO/MainProcess] Scheduler: Sending due task task_564 (main.run)
[2019-10-01 17:08:50,650: INFO/MainProcess] Scheduler: Sending due task task_618 (main.run)
[2019-10-01 17:08:50,655: INFO/MainProcess] Scheduler: Sending due task task_845 (main.run)
[2019-10-01 17:08:50,662: INFO/MainProcess] Scheduler: Sending due task task_94 (main.run)
[2019-10-01 17:08:50,667: INFO/MainProcess] Scheduler: Sending due task task_877 (main.run)
[2019-10-01 17:08:50,674: INFO/MainProcess] Scheduler: Sending due task task_180 (main.run)
[2019-10-01 17:08:50,680: INFO/MainProcess] Scheduler: Sending due task task_570 (main.run)
[2019-10-01 17:08:50,687: INFO/MainProcess] Scheduler: Sending due task task_499 (main.run)
[2019-10-01 17:08:50,693: INFO/MainProcess] Scheduler: Sending due task task_173 (main.run)
[2019-10-01 17:08:50,700: INFO/MainProcess] Scheduler: Sending due task task_291 (main.run)
[2019-10-01 17:08:50,705: INFO/MainProcess] Scheduler: Sending due task task_84 (main.run)
[2019-10-01 17:08:50,713: INFO/MainProcess] Scheduler: Sending due task task_806 (main.run)
[2019-10-01 17:08:50,718: INFO/MainProcess] Scheduler: Sending due task task_309 (main.run)
[2019-10-01 17:08:50,724: INFO/MainProcess] Scheduler: Sending due task task_471 (main.run)
[2019-10-01 17:08:50,730: INFO/MainProcess] Scheduler: Sending due task task_874 (main.run)

Avg: 5 - 7 ms


## RedBeat:

#### Retrieve from redis
```
redis-cli -n 1

# List all keys from
keys redbeat*
=>
32) "redbeat:task_37"
33) "redbeat:task_42"
34) "redbeat:task_13"
35) "redbeat:task_25"

# Get a value
hgetall redbeat:task_16
```

### Logs
[2019-10-01 17:32:07,795: INFO/MainProcess] add task entry: task_848 to publisher
[2019-10-01 17:32:07,799: INFO/MainProcess] add task entry: task_849 to publisher
[2019-10-01 17:32:07,802: INFO/MainProcess] add task entry: task_85 to publisher
[2019-10-01 17:32:07,808: INFO/MainProcess] add task entry: task_850 to publisher
[2019-10-01 17:32:07,811: INFO/MainProcess] add task entry: task_851 to publisher
[2019-10-01 17:32:07,815: INFO/MainProcess] add task entry: task_852 to publisher
[2019-10-01 17:32:07,818: INFO/MainProcess] add task entry: task_853 to publisher
[2019-10-01 17:32:07,824: INFO/MainProcess] add task entry: task_854 to publisher
[2019-10-01 17:32:07,826: INFO/MainProcess] add task entry: task_855 to publisher
[2019-10-01 17:32:07,830: INFO/MainProcess] add task entry: task_856 to publisher
[2019-10-01 17:32:07,834: INFO/MainProcess] add task entry: task_857 to publisher
[2019-10-01 17:32:07,838: INFO/MainProcess] add task entry: task_858 to publisher
[2019-10-01 17:32:07,842: INFO/MainProcess] add task entry: task_859 to publisher
[2019-10-01 17:32:07,847: INFO/MainProcess] add task entry: task_86 to publisher
[2019-10-01 17:32:07,850: INFO/MainProcess] add task entry: task_860 to publisher
[2019-10-01 17:32:07,856: INFO/MainProcess] add task entry: task_861 to publisher
[2019-10-01 17:32:07,858: INFO/MainProcess] add task entry: task_862 to publisher
[2019-10-01 17:32:07,864: INFO/MainProcess] add task entry: task_863 to publisher
[2019-10-01 17:32:07,867: INFO/MainProcess] add task entry: task_864 to publisher
[2019-10-01 17:32:07,872: INFO/MainProcess] add task entry: task_865 to publisher
[2019-10-01 17:32:07,875: INFO/MainProcess] add task entry: task_866 to publisher
[2019-10-01 17:32:07,878: INFO/MainProcess] add task entry: task_867 to publisher
[2019-10-01 17:32:07,882: INFO/MainProcess] add task entry: task_868 to publisher
[2019-10-01 17:32:07,885: INFO/MainProcess] add task entry: task_869 to publisher
[2019-10-01 17:32:07,890: INFO/MainProcess] add task entry: task_87 to publisher

Avg: 4 - 7 ms