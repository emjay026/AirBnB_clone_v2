#!/usr/bin/python3
"""Deletes the most recent n number of archives"""
import os
from fabric.api import env, local, run, lcd, cd

env.hosts = ['54.160.110.197', '100.26.227.7']


def do_clean(number=1):
    """Delete out-of-date archives."""
    number = max(int(number), 1)  # Ensure number is at least 1

    with lcd("versions"):
        archives = sorted(os.listdir("."))
        for archive in archives[:-number]:
            local(f"rm ./{archive}")

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if a.startswith("web_static_")]
        for archive in archives[:-number]:
            run(f"rm -rf ./{archive}")
