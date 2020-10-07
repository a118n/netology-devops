#!/usr/bin/env python3

import json
import yaml
from socket import gethostbyname

json_file = 'services.json'
yaml_file = 'services.yml'

with open(json_file) as f:
    data = json.load(f)

for service in data['services']:
    hostname = service['hostname']
    ip = service['ip']
    ip_new = gethostbyname(hostname)
    if ip != ip_new:
        print(f'[ERROR] {hostname} IP mismatch: {ip} {ip_new}.')
    print(f'{hostname} - {ip_new}')
    service['ip'] = ip_new

with open(json_file, 'w') as f:
    json.dump(data, f, indent=4)

with open(yaml_file, 'w') as f:
    yaml.dump(data, f)
