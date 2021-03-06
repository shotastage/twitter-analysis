#!/usr/bin/env python
# -*- encoding:utf-8 -*-
#
#   build.py
#   tweetgetter
#
#   Copyright (c) 2018 Shota Shimazu. All rights reserved.
#

from os import system
from sys import argv

if __name__ == "__main__":
    args = argv

    try:
        opt = args[1]
    except:
        opt = "none"

    system("python setup.py check")
    system("python setup.py sdist")

    if opt == "--update":
        system("pip uninstall tweetgetter")

    system("pip install dist/tweetgetter-0.0.1.tar.gz")
