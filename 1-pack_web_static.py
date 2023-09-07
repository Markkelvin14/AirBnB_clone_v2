#!/usr/bin/python3
''' generates a .tgz archive from contents of web_static folder '''
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates tgz ach"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    local("sudo mkdir -p versions")
    arch_name = "versions/web_static_{}.tgz".format(date)
    local("sudo tar -cvzf {} web_static".format(arch_name))
    return arch_name
