# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'navigator.ui'
#
# Created: Fri Nov  4 08:30:57 2016
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
        self.widget_3 = QtGui.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.searchBox = QtGui.QLineEdit(self.widget_3)
        self.searchBox.setObjectName("searchBox")
        self.horizontalLayout_2.addWidget(self.searchBox)
        self.homeButton = QtGui.QPushButton(self.widget_3)
        self.homeButton.setIconSize(QtCore.QSize(32, 32))
        self.homeButton.setObjectName("homeButton")
        self.horizontalLayout_2.addWidget(self.homeButton)
        self.verticalLayout.addWidget(self.widget_3)
        self.queryTable = QtGui.QTableView(self.widget)
        self.queryTable.setMaximumSize(QtCore.QSize(16777215, 200))
        self.queryTable.setObjectName("queryTable")
        self.queryTable.horizontalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.queryTable)
        self.graphicsView = QtGui.QGraphicsView(self.widget)
        self.graphicsView.setMaximumSize(QtCore.QSize(300, 10000))
        self.graphicsView.setMouseTracking(False)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
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
        self.gridLayout.addWidget(self.resourceTable, 2, 0, 1, 1)
        self.resourceLabel = QtGui.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.resourceLabel.setFont(font)
        self.resourceLabel.setObjectName("resourceLabel")
        self.gridLayout.addWidget(self.resourceLabel, 1, 0, 1, 1)
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
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Dedalus Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Search:", None, QtGui.QApplication.UnicodeUTF8))
        self.homeButton.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.resourceLabel.setText(QtGui.QApplication.translate("MainWindow", "Resurces", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
