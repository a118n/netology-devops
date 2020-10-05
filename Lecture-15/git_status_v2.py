#!/usr/bin/env python3

from os import popen, getcwd, path
from sys import argv
from subprocess import run


def is_git_repo(path):
    return run(f'cd {path} && git rev-parse --is-inside-work-tree >/dev/null 2>&1', shell=True).returncode == 0


def check_modified(path):
    output = popen(f'git status {path}').read().split('\n')
    for item in output:
        if item.find('modified') != -1:
            result = item.replace('\tmodified:   ', '')
            print(getcwd() + '/' + result)


path = argv[1] if len(argv) >= 2 else getcwd()

if path.isdir(path) and is_git_repo(path):
    check_modified(path)
else:
    print(f"{path} is not a git repo, or directory doesn't exist!")
