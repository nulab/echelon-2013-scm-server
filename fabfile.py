#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Echelon Ignite 2013 Thailand
# http://e27.co/ignite/
#
# Service Configuration Management for Rapid Growth Workshop Demo
#
__author__ = 'Takashi Someda <someda@nulab-inc.com>'

from fabric.api import *
from fabric.colors import *

from fabric.contrib.project import rsync_project
from fabric.contrib.files import exists

import os, sys

env.use_ssh_config = True
env.ssh_config_path = 'ssh.config'

@task
def stop():
    sudo('supervisorctl stop todo')
    sudo('supervisorctl status todo')

@task
def start():
    sudo('supervisorctl start todo')
    sudo('supervisorctl status todo')    

@task
def deploy(localdir):
    if not os.path.exists(localdir) or not os.path.isdir(localdir) :
        print red('No such directory %s' % localdir)
        sys.exit(1)

    localdir = adjust_path(localdir)

    rsync_project(
        local_dir=localdir,
        remote_dir=app_dir(),
        delete=True,
        exclude=['*.pyc']
    )
    with cd(app_dir()):
        sudo('pip install todo.pybundle')
        if not exists('todo.db') :
            run('sqlite3 todo.db < etc/schema.sql')

def app_dir():
    return '/home/%s/app' % env.user

def adjust_path(path):
    """
    Adjust path value for rsync
    """
    ret = path
    if not path.endswith('/'):
        ret = path + '/'

    if path.find(' ') != -1:
        ret = '"' + ret + '"'
    return ret

