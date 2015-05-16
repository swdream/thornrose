#!/usr/bin/python
# -*- coding: utf-8 -*-
# Sat May 16 10:38:38 ICT 2015

import os
import datetime


__version__ = '1.0'

def datadir():
    path = os.path.expanduser('~/.thornrose')
    if not os.path.isdir(os.path.abspath(path)):
        os.mkdir(path)

    return path


def dbfile(name):
    """
    Name is the month you need to manage your
    money in that month.
    File name is
    """

