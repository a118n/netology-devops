#!/usr/bin/env python3

from os import popen, getcwd, path
from sys import argv, exit
from subprocess import run


def is_git_repo(repo_path):
    return run(f'cd {repo_path} && git rev-parse --is-inside-work-tree >/dev/null 2>&1', shell=True).returncode == 0


def check_modified(repo_path):
    output = popen(f'git status {repo_path}').read().split('\n')
    for item in output:
        if item.find('modified') != -1:
            result = item.replace('\tmodified:   ', '')
            print(getcwd() + '/' + result)


repo_path = argv[1] if len(argv) >= 2 else getcwd()

if not path.isdir(repo_path) or not is_git_repo(repo_path):
    print(f"{repo_path} is not a git repo or directory doesn't exist!")
else:
    check_modified(repo_path)
