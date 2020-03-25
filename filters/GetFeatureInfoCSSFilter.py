
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


from qgis.server import *

class GetFeatureInfoFilter(QgsServerFilter):

    def __init__(self, serverIface):
        super(GetFeatureInfoFilter, self).__init__(serverIface)

    def responseComplete(self):
        handler = self.serverInterface().requestHandler()
        params = handler.parameterMap( )

        if (params.get('SERVICE', '').upper() == 'WMS' \
                and params.get('REQUEST', '').upper() == 'GETFEATUREINFO' \
                and params.get('INFO_FORMAT', '').upper() == 'TEXT/HTML' \
                and not handler.exceptionRaised() ):
            body = handler.body()
            body.replace(b'<BODY>', b"""<BODY><STYLE type="text/css">* {font-family: arial, sans-serif; color: #09095e;} table { border-collapse:collapse; } td, tr { border: solid 1px grey; }</STYLE>""")
            handler.clearBody()
            handler.appendBody(body)


