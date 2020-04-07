#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """ Generate a .tgz archive from the contents of the web_static folder """
    time = datetime.now()
    name = 'web_static_{}{}{}{}{}{}.tgz'.format(str(time.year),
                                                str(time.month),
                                                str(time.day),
                                                str(time.hour),
                                                str(time.minute),
                                                str(time.second)
                                               )
    local('mkdir -p versions')
    archive = local('tar -cvzf versions/{} web_static'.format(name))
    if archive.failed:
        return None
    return 'versions/{}'.format(name)
