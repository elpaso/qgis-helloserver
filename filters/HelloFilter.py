# -*- coding: utf-8 -*-

"""
***************************************************************************
    QGIS Server Plugin Filters: say hello test filter, just logs calls and
    prints HelloServer! on plain text response
    ---------------------
    Date                 : October 2014
    Copyright            : (C) 2014-2015 by Alessandro Pasotti
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

from qgis.server import *
from qgis.core import *
from HelloServer.HelloServer import HelloServer

class HelloFilter(QgsServerFilter):

    def __init__(self, serverIface):
        super(HelloFilter, self).__init__(serverIface)

    def requestReady(self):
        QgsMessageLog.logMessage("HelloFilter.requestReady")

    def sendResponse(self):
        QgsMessageLog.logMessage("HelloFilter.sendResponse")

    def responseComplete(self):
        QgsMessageLog.logMessage("HelloFilter.responseComplete")
        request = self.serverInterface().requestHandler()
        params = request.parameterMap()
        if params.get('SERVICE', '').upper() == 'HELLO':
            request.clearHeaders()
            request.setHeader('Content-type', 'text/plain')
            request.clearBody()
            request.appendBody('HelloServer!')
