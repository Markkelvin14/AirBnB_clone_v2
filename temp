#!/usr/bin/python3
''' contains the function do_deploy '''
from fabric.api import env, sudo, run, put
from os.path import exists
env.hosts = ['34.203.33.205', '54.210.127.27']
env.user = 'ubuntu'


def do_deploy(archive_path):
    ''' distributes an archive to web servers '''
    if exists(archive_path) is False:
        return False
    arch_name = archive_path.split('/')[-1]
    new = '/data/web_static/release/' + \
          "{}".format(arch_name.split('.')[0])
    current = 'data/web_static/current'
    try:
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}/'.format(new))
        run('sudo tar -xzf {} -C {}/'.format(tmp, new))
        run('sudo rm /tmp/{}'.format(arch_name))
        run('sudo mv {}/web_static {}/'.format(new))
        run('sudo rm -rf {}'.format(current))
        run('sudo ln -s {}/ {}'.format(new, current))
        print("New version deployed!")
        return True
    except:
        return False
