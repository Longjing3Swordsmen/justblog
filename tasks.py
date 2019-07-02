# -*- coding: utf-8 -*-
# @Author  : von
# @Email   : vonhng@qq.com
# @Time    : 2019/7/2 22:57
# @Func_spec : 

import os
from invoke import task
from datetime import datetime

root = os.path.dirname(os.path.abspath(__file__))
now_time = datetime.now().strftime("%Y%m%d")


@task
def clean(ctx):
    ctx.run('rm -rf build', echo=True)
    ctx.run("find . -name '*.pyc' -exec rm -f {} +", echo=True)
    ctx.run("find . -name '*.pyo' -exec rm -f {} +", echo=True)
    ctx.run("find . -name '*.log' -exec rm -f {} +", echo=True)
    ctx.run("find . -name '*.db' -exec rm -f {} +", echo=True)
    ctx.run("find . -name '__pycache__' -exec rm -rf {} +", echo=True)
    

@task(clean)
def client(ctx):
    name = "justblog"
    build_dir = os.path.join(root, 'build')
    dist_dir = os.path.join(build_dir, name)
    ctx.run('mkdir -p {dist_dir}'.format(dist_dir=dist_dir), echo=True)
    include_dir = [
        os.path.join(root, 'service'),
        os.path.join(root, 'bin'),

        os.path.join(root, 'run.py'),
        os.path.join(root, 'README.md')
    ]
    ctx.run('cp -r {dirs} {dist_dir}'.format(dirs=' '.join(include_dir),
                                             dist_dir=dist_dir), echo=True)
    ctx.run("cd {build_dir} && tar zcvf {name}.{time}.tar.gz {name} && rm -rf {name}".format(
        build_dir=build_dir, name=name, time=now_time))

