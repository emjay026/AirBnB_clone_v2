#!/usr/bin/python3
"""This module defines a Fabric function that deploys files to remote servers.

Execution: fab -f 2-do_deploy_web_static.py
            do_deploy:archive_path=versions/web_static_20240503191301.tgz
            -i ~/.ssh/id_rsa -u ubuntu
"""
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['54.160.110.197', '100.26.227.7']


def do_deploy(archive_path):
    """Dispatches deployment based on remote execution."""

    if not exists(archive_path):
        return False

    try:
        archive_file = archive_path.split("/")[-1]
        file_name = archive_file.split(".")[0]
        path = "/data/web_static/releases/"

        # Upload the archive to the remote host(s)
        put(archive_path, '/tmp/')

        # Extract the archive
        run(f'mkdir -p {path}{file_name}/')
        run(f'tar -xzf /tmp/{archive_file} -C {path}{file_name}/')

        # Move files to the desired location
        run(f'mv {path}{file_name}/web_static/* {path}{file_name}/')

        # Remove unnecessary files
        run(f'rm -rf {path}{file_name}/web_static')
        run(f'rm -rf /data/web_static/current')

        # Update the symbolic link
        run(f'ln -s {path}{file_name}/ /data/web_static/current')

        return True
    except Exception as e:
        return False
