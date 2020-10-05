#!/usr/bin/env bash

commit_regex='^\[[A-Z]{2,}-[0-9]{1,}\].{3,31}$'
error_msg="Aborting commit. Your commit message doesn't fit the reqired format, e.g. [ABC-12345] Fix some typo"

if [[ ! $1 =~ $commit_regex ]]; then
    echo "$error_msg" >&2
    exit 1
fi
