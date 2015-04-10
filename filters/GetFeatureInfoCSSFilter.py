
# -*- coding: utf-8 -*-

"""
***************************************************************************
    QGIS Server Plugin Filters: this test filter adds a CSS to HTML
    get feature info response.
    ---------------------
    Date                 : April 2015
    Copyright            : (C) 2015 by Alessandro Pasotti
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

import os

from qgis.server import *
from qgis.core import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class GetFeatureInfoCSSFilter(QgsServerFilter):

    def __init__(self, serverIface):
        super(GetFeatureInfoCSSFilter, self).__init__(serverIface)

    def requestReady(self):
        """Nothing to do here, but it would be the ideal point
        to alter request **before** it gets processed, for example
        you could set INFO_FORMAT to text/xml to get XML instead of
        HTML in responseComplete"""
        pass

    def responseComplete(self):
        request = self.serverInterface().requestHandler()
        params = request.parameterMap( )
        if (params.get('SERVICE').upper() == 'WMS' \
                and params.get('REQUEST', '').upper() == 'GETFEATUREINFO' \
                and params.get('INFO_FORMAT', '').upper() == 'TEXT/HTML' \
                and not request.exceptionRaised() ):
            body = request.body()
            body.replace('<BODY>', """<BODY><STYLE type="text/css">* {font-family: arial, sans-serif; color: blue;}</STYLE>""")
            # Set the body
            request.clearBody()
            request.appendBody(body)
