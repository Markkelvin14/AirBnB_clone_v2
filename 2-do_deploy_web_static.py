#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["34.203.33.205", "54.210.127.27"]
env.user = "ubuntu"


def do_pack():
    """
        return the archive path if archive has generated correctly.
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_name = "versions/web_static_{}.tgz".format(date)
    gzip_archive = local("tar -cvzf {} web_static".format(archived_name))

    if gzip_archive.succeeded:
        return archived_name
    else:
        return None


def do_deploy(archive_path):
    """
        Distribute archive.
    """
    if os.path.exists(archive_path):
        arch_name = archive_path[9:]
        new_version = "/data/web_static/releases/" + arch_name[:-4]
        arch_name = "/tmp/" + arch_name
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_version))
        run("sudo tar -xzf {} -C {}/".format(arch_name,
                                             new_version))
        run("sudo rm {}".format(arch_name))
        run("sudo mv {}/web_static/* {}".format(new_version,
                                                new_version))
        run("sudo rm -rf {}/web_static".format(new_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(new_version))

        print("New version deployed!")
        return True

    return False
