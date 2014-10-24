# -*- coding: utf-8 -*-
"""
***************************************************************************
Name			 	 : HelloServer
Description          : HelloServer
Date                 : 11/Aug/2014
copyright            : (C) 2014 by ItOpen
email                : info@itopen.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4 import QtCore, QtGui
from Ui_HelloServer import Ui_HelloServer
# create the dialog

class HelloServerDialog(QtGui.QDialog, Ui_HelloServer ):

    MIMES = ['text/plain', 'text/html', 'application/xml']

    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)

