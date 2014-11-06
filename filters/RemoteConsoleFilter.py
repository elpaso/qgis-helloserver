# -*- coding: utf-8 -*-
"""
***************************************************************************
    RemoteConsoleFilter: test filter for a persistent remote console
    ---------------------
    Date                 : Octopber 2014
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


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# WARNING: THIS IS A TEST FILTER - HIGHLY INSECURE CODE, DO NOT USE
#          IN PRODUCTION
#
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from qgis.server import *
from qgis.core import *

import sys
import os
from StringIO import StringIO
import base64

from HelloServer.HelloServer import HelloServer

def check_auth(userid, password):
    return userid == HelloServer.getSettings().get('userid', HelloServer.DEFAULT_USERID) \
        and password == HelloServer.getSettings().get('password', HelloServer.DEFAULT_PASSWORD)

class RemoteConsoleFilter(QgsServerFilter):

    def __init__(self, serverIface):
        super(RemoteConsoleFilter, self).__init__(serverIface)

    def run(self, request, parameters):
        """Run arbitrary Python code from CODE parameter, sends back the output.
        The single user session is maintained in a local buffer"""
        try:
            RemoteConsoleFilter._local_buffer
        except:
            RemoteConsoleFilter._local_buffer = locals()

        request.clearHeaders()
        request.clearBody()
        if not 'CODE' in parameters:
            with open( os.path.dirname(os.path.realpath(__file__)) + '/media/RemoteConsole.html') as f:
                request.appendBody(''.join(f.readlines()))
                request.setInfoFormat('text/html')
                # Clear the buffer
                RemoteConsoleFilter._local_buffer = locals()

        else:
            try:
                code = parameters['CODE'] + '\nRemoteConsoleFilter._local_buffer = locals()'
                buffer = StringIO()
                sys.stdout = buffer
                exec(code, globals(), RemoteConsoleFilter._local_buffer)
                value = buffer.getvalue()
                QgsMessageLog.logMessage("RemoteConsoleFilter.run %s" % value, 'plugin', QgsMessageLog.INFO)
                if not value:
                    value = "\n"
                request.appendBody(value)
            except Exception, e:
                request.appendBody( "Error: %s" % e )
            request.setInfoFormat('text/plain')

        sys.stdout = sys.__stdout__


    def responseComplete(self):
        QgsMessageLog.logMessage("RemoteConsoleFilter.responseComplete", 'plugin', QgsMessageLog.INFO)
        request = self.serverInterface().requestHandler()
        params = request.parameterMap( )
        if ( params.get('SERVICE', '').lower() == 'remoteconsole'):
            if self.serverInterface().getEnv('REMOTE_ADDR') != HelloServer.getSettings().get('REMOTE_ADDR', HelloServer.DEFAULT_REMOTE_ADDR):
                request.clearHeaders()
                request.setHeader('Status', '403 Forbidden')
                request.clearBody()
                request.appendBody('<h1>Forbidden!</h1>')
            else:
                if self.serverInterface().getEnv('HTTP_AUTHORIZATION'):
                    userid, password = base64.b64decode(self.serverInterface().getEnv('HTTP_AUTHORIZATION')[6:]).split(':')
                    if ( check_auth(userid, password) ):
                        self.run(request, params)
                        return
                # No auth ...
                request.clearHeaders()
                request.setHeader('Status', '401 Authorization required')
                request.setHeader('WWW-Authenticate', 'Basic realm="QGIS Remote Console"')
                request.clearBody()
                request.appendBody('<h1>Authorization required</h1>')
