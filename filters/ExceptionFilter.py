# -*- coding: utf-8 -*-

"""
***************************************************************************
    ExceptionFilter:  test filter for QgsMapServiceException
    ---------------------
    Date                 : August 2014
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
from __future__ import print_function


# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.server import *


class ExceptionFilter(QgsServerFilter):

    def __init__(self, serverIface):
        super(ExceptionFilter, self).__init__(serverIface)

    def responseComplete(self):
        request = self.serverInterface().requestHandler()
        params = request.parameterMap()
        if params.get('SERVICE', '').upper() == 'EXCEPTION':
            QgsMessageLog.logMessage("ExceptionFilter.responseComplete exception raised!")
            # Not very "pythonic" way to raise exceptions but this allows for
            # a different path for wanted and unwanted exceptions:
            # * QgsMapServiceException will show in the service output as a ServiceExceptionReport XML document
            # * unhandled unwanted exceptions will only show up in the server logs
            request.setServiceException(QgsMapServiceException('ExceptionFilter', 'Test exception raised from ExceptionFilter'))

