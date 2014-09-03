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

__author__ = 'Alessandro Pasotti'
__date__ = 'August 2014'
__copyright__ = '(C) 2014, Alessandro Pasotti'

import pickle
import os

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from HelloServerDialog import HelloServerDialog

DEFAULT_CODE = 'print "Just a testing server plugin!"'


class HelloServer:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = iface.mapCanvas()

    def initGui(self):
        # Create action that will start plugin
        self.action = QAction(QIcon(":/plugins/"), "&HelloServer", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("activated()"), self.config)

        # Add toolbar button and menu item
        self.iface.addPluginToMenu("HelloServer", self.action)

    # change settings
    def config(self):
        # create and show the dialog
        dlg = HelloServerDialog()
        # Get settings
        settings = HelloServer.getSettings()
        dlg.mimeComboBox.setCurrentIndex(dlg.MIMES.index(settings['mime']))
        dlg.code.setPlainText(settings['code'])
        # show the dialog
        dlg.show()
        result = dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # save settings
            HelloServer.storeSettings({
                'mime': dlg.mimeComboBox.currentText(),
                'code': dlg.code.toPlainText(),
            })


    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("HelloServer",self.action)


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
        # Store configuration locallyoutput
        try:
            output = open(HelloServer._getSettingsPath(), 'rb')
            # Pickle dictionary using protocol 0.
            settings = pickle.load(output)
            output.close()
        except:
            settings = {
                'mime' : 'text/plain',
                'code' : DEFAULT_CODE
            }
        return settings

    @staticmethod
    def GetCapabilities(project_path, parameters):
        print '<ul><li><b>GetOutput</b>: run arbitrary Python code, configure it from QGIS plugin interface. Project path is: %s</li>' % project_path
        print '<li><b>RemoteConsole</b>: run arbitrary Python code in web shell. This is highly insecure and for testing only: do not use on production servers.</li></ul>'
        return 'text/html'

    @staticmethod
    def GetOutput(project_path, parameters):
        """Run arbitrary Python code, configure it from QGIS plugin interface"""
        settings = HelloServer.getSettings()
        try:
            exec(settings['code'], globals(), locals())
        except Exception, e:
            print "Error: %s" % e
            return 'text/plain'
        return settings['mime']


    @staticmethod
    def SayHello(project_path, parameters):
        """Just say a sentence"""
        print "HelloServer"
        return 'text/plain'


    @staticmethod
    def RemoteConsole(project_path, parameters):
        """Run arbitrary Python code from CODE parameter, sends back the output"""
        # Instanciate a locals buffer
        try:
            HelloServer._local_buffer
        except:
            HelloServer._local_buffer = locals()
        if not 'CODE' in parameters:
            with open( os.path.dirname(os.path.realpath(__file__)) + '/RemoteConsole.html') as f:
                print ''.join(f.readlines())
                # Clear the buffer
                HelloServer._local_buffer = locals()
                return 'text/html'
        else:
            try:
                code = parameters['CODE'] + '\nHelloServer._local_buffer = locals()'
                exec(code, globals(), HelloServer._local_buffer)
            except Exception, e:
                print "Error: %s" % e
        return 'text/plain'


if __name__ == "__main__":
    pass
