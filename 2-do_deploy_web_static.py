#!/usr/bin/python3
''' Contains a fabric script that distributes an archive to my web servers '''

import os
from fabric.api import env, put, run


env.hosts = ["34.73.37.244", "35.243.137.210"]
env.user = "ubuntu"


def do_deploy(archive_path):
    ''' Distributes archive to servers '''
    if archive_path is None or not os.path.isfile(archive_path):
        print("Please enter a path to an existing file")
        return False

    arc_full = os.path.basename(archive_path)
    arc_short = arc_full.split(".")[0]

    put(local_path=archive_path, remote_path="/tmp/")
    run("mkdir -p /data/web_static/releases/{}".format(arc_short))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(arc_full,
                                                                  arc_short))
    run("rm /tmp/{}".format(arc_full))
    run("rm -rf /data/web_static/current")
    run("ln -fs /data/web_static/releases/{}/ \
        /data/web_static/current".format(arc_short))
    run("mv /data/web_static/current/web_static/* /data/web_static/current/")
    run("rm -rf /data/web_static/curren/web_static")

    return True
