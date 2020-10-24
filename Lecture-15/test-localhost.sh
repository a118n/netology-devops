#!/usr/bin/env bash

while :; do
    curl https://localhost:4757
    if [[ $? != 0 ]]; then
        date >>curl.log
    else
        break
    fi
done
