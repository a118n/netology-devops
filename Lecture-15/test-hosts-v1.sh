#!/usr/bin/env bash

tries_count=5
ip_list=(192.168.0.1 173.194.222.113 87.250.250.242)

for ((i = 0; i < tries_count; i++)); do
    for ip in "${ip_list[@]}"; do
        echo -n "${ip}: " >>log.txt
        timeout 3s curl -sf http://${ip} >/dev/null
        if [ $? != 0 ]; then
            echo "OFFLINE" >>log.txt
        else
            echo "ONLINE" >>log.txt
        fi
    done
done
