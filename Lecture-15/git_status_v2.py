#!/usr/bin/env python3

import os
import sys


def is_git_repo(path):
    return True if os.system(f'cd {path} && git rev-parse --is-inside-work-tree >/dev/null 2>&1') == 0 else False


def check_modified(path):
    result_os = os.popen(f'git status {path}').read().split('\n')
    for result in result_os:
        if result.find('modified') != -1:
            prepare_result = result.replace('\tmodified:   ', '')
            print(os.getcwd() + '/' + prepare_result)


path = sys.argv[1] if len(sys.argv) >= 2 else os.getcwd()
if is_git_repo(path):
    check_modified(path)
else:
    print(f'{path} is not a git repo!')
