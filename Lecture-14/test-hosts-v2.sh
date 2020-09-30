#!/usr/bin/env bash

ip_list=(192.168.0.1 173.194.222.113 87.250.250.242)

while :; do
    for ip in "${ip_list[@]}"; do
        timeout 3s curl -sf http://${ip} >/dev/null
        if [ $? != 0 ]; then
            echo "${ip} is OFFLINE" >>error.txt
            break 2
        else
            echo "${ip} is ONLINE" >>log.txt
        fi
    done
done
