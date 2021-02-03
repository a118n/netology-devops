#!/usr/bin/env python3

import psutil
import json
import time
import datetime

date = datetime.datetime.now()
log_path = f"/var/log/{date.year}-{date.month}-{date.day}-awesome-monitoring.log"

metrics = {}
metrics["timestamp"] = int(time.time())
metrics["metric_1"] = psutil.cpu_times()
metrics["metric_2"] = psutil.getloadavg()
metrics["metric_3"] = psutil.virtual_memory()
metrics["metric_4"] = psutil.swap_memory()
metrics["metric_5"] = psutil.disk_usage('/')

with open(log_path, "a") as f:
    json.dump(metrics, f, indent=4)
