#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2017 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os
import os.path
import sys


def loader(initpath, baseclass, target):
    basepath = os.path.dirname(initpath)

    for f in os.listdir(basepath):
        if not f.endswith('.py') or f == '__init__.py':
            continue

        mod, error = loadmodule(os.path.join(basepath, f))
        if error is not None:
            continue

        for name in dir(mod):
            if name.startswith('__'):
                continue

            attr = getattr(mod, name)
            try:
                if issubclass(attr, (baseclass,)):
                    setattr(target, name, attr)
            except:
                pass


def loadmodule(modpath, modname=''):

    if not modpath.endswith('.py'):
        modpath += '.py'

    # generate a random name for the module
    if not modname:
        modpathbase = os.path.basename(modpath)
        modname, _ = os.path.splitext(modpathbase)

    version = (sys.version_info[0], sys.version_info[1])

    if version < (3, 3):
        return loadmodule2(modpath, modname)

    return loadmodule3(modpath, modname)


def loadmodule2(modpath, modname):
    import imp

    try:
        mod = imp.load_source(modname, modpath)
    except Exception as e:
        return (None, e)

    return (mod, None)


def loadmodule3(modpath, modname):
    import importlib.machinery

    try:
        loader = importlib.machinery.SourceFileLoader(modname, modpath)
        mod = loader.load_module()
    except Exception as e:
        return (None, e)

    return (mod, None)
