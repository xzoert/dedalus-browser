# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'navigator.ui'
#
# Created: Thu Nov  3 11:36:42 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 696)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/dedalus/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtGui.QGraphicsView(self.widget)
        self.graphicsView.setMaximumSize(QtCore.QSize(300, 10000))
        self.graphicsView.setMouseTracking(False)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.queryTable = QtGui.QTableView(self.widget)
        self.queryTable.setObjectName("queryTable")
        self.queryTable.horizontalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.queryTable)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtGui.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.resourceTable = QtGui.QTableWidget(self.widget_2)
        self.resourceTable.setStyleSheet("")
        self.resourceTable.setAlternatingRowColors(False)
        self.resourceTable.setObjectName("resourceTable")
        self.resourceTable.setColumnCount(0)
        self.resourceTable.setRowCount(0)
        self.resourceTable.horizontalHeader().setVisible(False)
        self.resourceTable.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.resourceTable, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Dedalus browser", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
