# -*- coding: utf-8 -*-

"""
***************************************************************************
    HelloServer.py
    ---------------------
    Date                 : August 2014
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
from __future__ import print_function

__author__ = 'Alessandro Pasotti'
__date__ = 'August 2014'
__copyright__ = '(C) 2014, Alessandro Pasotti - ItOpen'

import sys

import pickle
import os

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
try:
    from qgis.server import *
except:
    pass
from HelloServerDialog import HelloServerDialog

# Remote console filter auth defaults

# The filter will issue a 403 Forbidden if the following
# environment vars are not passed by FCGI:

DEFAULT_REMOTE_ADDR = '127.0.0.1'

"""
HTTP_AUTH BASIC
May need proper fcgid apache configuration:

    RewriteEngine On
    <IfModule mod_fcgid.c>
        RewriteCond %{HTTP:Authorization} .
        RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
    </IfModule>

"""

DEFAULT_USERID = 'test'
DEFAULT_PASSWORD = 'qgis'


def error_log(msg):
    """Print to stderr"""
    print("HelloServer: ", msg, file=sys.stderr)


class HelloServer:
    """Test plugin for QGIS server"""

    DEFAULT_PASSWORD = DEFAULT_PASSWORD
    DEFAULT_USERID = DEFAULT_USERID
    DEFAULT_REMOTE_ADDR = DEFAULT_REMOTE_ADDR

    def __init__(self, serverIface):
        # Save reference to the QGIS interface
        self.serverIface = serverIface
        self.canvas = serverIface.mapCanvas()

    def initGui(self):
        # Create action that will start plugin
        self.action = QAction(QIcon(":/plugins/"), "&HelloServer", self.serverIface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("activated()"), self.config)

        # Add toolbar button and menu item
        self.serverIface.addPluginToMenu("HelloServer", self.action)

    # change settings
    def config(self):
        # create and show the dialog
        dlg = HelloServerDialog()
        # Get settings
        settings = HelloServer.getSettings()
        dlg.userid.setText(settings['userid'])
        dlg.password.setText(settings['password'])
        dlg.remote_addr.setText(settings['remote_addr'])
        # show the dialog
        dlg.show()
        result = dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # save settings
            HelloServer.storeSettings({
                'userid':  dlg.userid.text(),
                'password': dlg.password.text(),
                'remote_addr': dlg.remote_addr.text(),
            })


    def unload(self):
        # Remove the plugin menu item and icon
        self.serverIface.removePluginMenu("HelloServer",self.action)


    @staticmethod
    def _getSettingsPath():
        dirname = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(dirname, 'helloserver.pkl')

    @staticmethod
    def storeSettings(settings):
        # Stores configuration locally
        output = open(HelloServer._getSettingsPath(), 'wb')
        config = pickle.dump(settings, output)
        output.close()


    @staticmethod
    def getSettings():
        try:
            in_file = open(HelloServer._getSettingsPath(), 'rb')
            # Pickle dictionary using protocol 0.
            HelloServer.settings = pickle.load(in_file)
            in_file.close()
        except Exception, e:
            HelloServer.settings = {
                'userid':  DEFAULT_USERID,
                'password': DEFAULT_PASSWORD,
                'remote_addr': DEFAULT_REMOTE_ADDR,
            }
        return HelloServer.settings


class HelloServerServer:
    """Test plugin for QGIS server
    this plugin loads all filters from the 'filters' directory and logs
    errors"""

    def __init__(self, serverIface):
        # Save reference to the QGIS server interface
        self.serverIface = serverIface
        import filters
        priority = 1
        for filter_name in filters.local_modules:
            QgsMessageLog.logMessage("HelloServerServer - loading filter %s" % filter_name, 'plugin', QgsMessageLog.INFO)
            try:
                serverIface.registerFilter( getattr(filters, filter_name)(serverIface), priority * 100 )
                priority += 1
            except Exception, e:
                QgsMessageLog.logMessage("HelloServerServer - Error loading filter %s : %s" % (filter_name, e), 'plugin', QgsMessageLog.CRITICAL)


if __name__ == "__main__":
    pass
