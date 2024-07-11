#!/usr/bin/python3
"""This module defines a Fabric function that packs current files."""
from fabric.api import local
import os
from datetime import datetime


def do_pack():
    """Function that creates .tgz archive from current directory contents. """

    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{current_time}.tgz"  # Buid filename
    archive_path = f"versions/{archive_name}"  # Build path

    # Create versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Create the archive
    result = local(f"tar -cvzf {archive_path} web_static")

    if result.succeeded:
        size = os.path.getsize(archive_path)
        print(f"web_static packed: {archive_path} -> {size}Bytes")
        return archive_path
    return None
