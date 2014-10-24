# -*- coding: utf-8 -*-

"""
***************************************************************************
    QGIS Server Plugin Filters - test filters. This init file will load
    all filter modules (matching *Filter.py in the current folder)
    ---------------------
    Date                 : October 2014
    Copyright            : (C) 2014 by Alessandro Pasotti
    Email                : apasotti at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__all__ = ['FilterTestBase']

import pkgutil
import inspect
import os
import glob

modules = glob.glob(os.path.dirname(__file__)+"/*Filter.py")
local_modules = [ os.path.basename(f)[:-3] for f in modules]


for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)

    for name, value in inspect.getmembers(module):
        if not name in local_modules:
            continue
        globals()[name] = value
        __all__.append(name)
