#!/usr/bin/env python3

import json
from socket import gethostbyname

filename = 'services.json'

with open(filename) as f:
    data = json.load(f)

for service in data['services']:
    hostname = service['hostname']
    ip = service['ip']
    ip_new = gethostbyname(hostname)
    if ip != ip_new:
        print(f'[ERROR] {hostname} IP mismatch: {ip} {ip_new}.')
    print(f'{hostname} - {ip_new}')
    service['ip'] = ip_new

with open(filename, 'w') as f:
    json.dump(data, f, indent=4)
