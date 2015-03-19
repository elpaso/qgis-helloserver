# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_HelloServer.ui'
#
# Created: Thu Mar 19 09:39:08 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HelloServer(object):
    def setupUi(self, HelloServer):
        HelloServer.setObjectName(_fromUtf8("HelloServer"))
        HelloServer.resize(1208, 680)
        self.gridLayout_4 = QtGui.QGridLayout(HelloServer)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.Config = QtGui.QTabWidget(HelloServer)
        self.Config.setObjectName(_fromUtf8("Config"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(10)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.Config.addTab(self.tab, _fromUtf8(""))
        self.config = QtGui.QWidget()
        self.config.setObjectName(_fromUtf8("config"))
        self.gridLayout_2 = QtGui.QGridLayout(self.config)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.config)
        self.label_3.setWordWrap(True)
        self.label_3.setMargin(5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addressLabel = QtGui.QLabel(self.config)
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        self.horizontalLayout.addWidget(self.addressLabel)
        self.userid = QtGui.QLineEdit(self.config)
        self.userid.setObjectName(_fromUtf8("userid"))
        self.horizontalLayout.addWidget(self.userid)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.config)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.password = QtGui.QLineEdit(self.config)
        self.password.setObjectName(_fromUtf8("password"))
        self.horizontalLayout_3.addWidget(self.password)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(self.config)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.remote_addr = QtGui.QLineEdit(self.config)
        self.remote_addr.setObjectName(_fromUtf8("remote_addr"))
        self.horizontalLayout_4.addWidget(self.remote_addr)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.Config.addTab(self.config, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setWordWrap(True)
        self.label_5.setMargin(10)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.label_5)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.Config.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.Config, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.buttonBox = QtGui.QDialogButtonBox(HelloServer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(HelloServer)
        self.Config.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), HelloServer.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), HelloServer.reject)
        QtCore.QMetaObject.connectSlotsByName(HelloServer)

    def retranslateUi(self, HelloServer):
        HelloServer.setWindowTitle(_translate("HelloServer", "HelloServer", None))
        self.label_4.setText(_translate("HelloServer", "<html><head/><body><p>This is a test example plugin for QGIS server.</p><p>The plugin implements a few <span style=\" font-weight:600;\">QgsServerFilter</span> that provide examples for common use cases:</p>\n"
"<ul>\n"
"<li>RemoteConsoleFilter: (see config) an HTML remote python console, also implements HTTP BASIC Authentication</li>\n"
"<li>ParamsFilter: do nothing but logging the result of QUERY STRING manipulation tests</li>\n"
"<li>HelloFilter: say HelloServer! and write some lines in the logs</li>\n"
"<li>WaterMarkFilter: adds a watermark image on top of all WMS GetImage requests.</li>\n"
"<li>ExceptionFilter: raise and exception, catched in main loop.</li>\n"
"</ul>\n"
"<p>For further informations, please see <a target=\"_blank\"  href=\"http://www.itopen.it/qgis/\">QGIS server plugins</a>\n"
"</body></html>", None))
        self.Config.setTabText(self.Config.indexOf(self.tab), _translate("HelloServer", "Info", None))
        self.label_3.setText(_translate("HelloServer", "<html><head/><body><p>Access control for <span style=\" font-weight:600;\">remote console</span> test plugin filter.</p><p><span style=\" font-weight:600;\">HTTP basic authentication</span> will prompt the user for the userid and password specified below.</p><p>A <span style=\" font-weight:600;\">403 Forbidden</span> header will be issued if the remote address does not match the address entered below.</p><p><span style=\" font-weight:600;\">Plugin\'s settings are stored in the current project.</span></p></body></html>", None))
        self.addressLabel.setText(_translate("HelloServer", "Username", None))
        self.label.setText(_translate("HelloServer", "Password", None))
        self.label_2.setText(_translate("HelloServer", "Remote IP address", None))
        self.Config.setTabText(self.Config.indexOf(self.config), _translate("HelloServer", "Config", None))
        self.label_5.setText(_translate("HelloServer", "<html><head/><body><p>Some of the example filters provided by this plugins can be tested opening the following URLs, if you are not on <span style=\" font-weight:600;\">localhost</span> or have different deployment address, please change the URLs accordingly.</p><p>\n"
"<ul>\n"
"<li>RemoteConsoleFilter: <a href=\"http://localhost/cgi-bin/qgis_mapserv.fcgi?SERVICE=remoteconsole\">http://localhost/cgi-bin/qgis_mapserv.fcgi?SERVICE=remoteconsole</a</li>\n"
"<li>HelloFilter<a href=\"http://localhost/cgi-bin/qgis_mapserv.fcgi?SERVICE=HELLO\">http://localhost/cgi-bin/qgis_mapserv.fcgi?SERVICE=HELLO</a</li>\n"
"<li>ExceptionFilter<a href=\"http://localhost/cgi-bin/qgis_mapserv.fcgi?SERVICE=EXCEPTION\">http://localhost/cgi-bin/qgis_mapserv.fcgi?SERVICE=EXCEPTION</a</li>\n"
"</ul>\n"
"</p></body></html>", None))
        self.Config.setTabText(self.Config.indexOf(self.tab_2), _translate("HelloServer", "Test URLs", None))

