# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgLogin(object):
    def setupUi(self, dlgLogin):
        dlgLogin.setObjectName("dlgLogin")
        dlgLogin.setWindowModality(QtCore.Qt.NonModal)
        dlgLogin.resize(280, 160)
        dlgLogin.setMinimumSize(QtCore.QSize(280, 160))
        dlgLogin.setMaximumSize(QtCore.QSize(280, 140))
        dlgLogin.setSizeIncrement(QtCore.QSize(300, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons/chat1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlgLogin.setWindowIcon(icon)
        dlgLogin.setStyleSheet("")
        dlgLogin.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(dlgLogin)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblImage = QtWidgets.QLabel(dlgLogin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblImage.sizePolicy().hasHeightForWidth())
        self.lblImage.setSizePolicy(sizePolicy)
        self.lblImage.setMinimumSize(QtCore.QSize(80, 80))
        self.lblImage.setBaseSize(QtCore.QSize(80, 80))
        self.lblImage.setStyleSheet("")
        self.lblImage.setText("")
        self.lblImage.setPixmap(QtGui.QPixmap("images/icons/msg_icon.jpg"))
        self.lblImage.setScaledContents(True)
        self.lblImage.setObjectName("lblImage")
        self.horizontalLayout.addWidget(self.lblImage)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblLogin = QtWidgets.QLabel(dlgLogin)
        self.lblLogin.setObjectName("lblLogin")
        self.verticalLayout.addWidget(self.lblLogin)
        self.lnLogin = QtWidgets.QLineEdit(dlgLogin)
        self.lnLogin.setMinimumSize(QtCore.QSize(160, 20))
        self.lnLogin.setMaximumSize(QtCore.QSize(160, 20))
        self.lnLogin.setText("")
        self.lnLogin.setObjectName("lnLogin")
        self.verticalLayout.addWidget(self.lnLogin)
        self.lblPassword = QtWidgets.QLabel(dlgLogin)
        self.lblPassword.setEnabled(True)
        self.lblPassword.setObjectName("lblPassword")
        self.verticalLayout.addWidget(self.lblPassword)
        self.lnPassword = QtWidgets.QLineEdit(dlgLogin)
        self.lnPassword.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnPassword.sizePolicy().hasHeightForWidth())
        self.lnPassword.setSizePolicy(sizePolicy)
        self.lnPassword.setMinimumSize(QtCore.QSize(160, 20))
        self.lnPassword.setMaximumSize(QtCore.QSize(160, 20))
        self.lnPassword.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lnPassword.setObjectName("lnPassword")
        self.verticalLayout.addWidget(self.lnPassword)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlgLogin)
        self.buttonBox.setMinimumSize(QtCore.QSize(40, 20))
        self.buttonBox.setBaseSize(QtCore.QSize(40, 20))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(dlgLogin)
        self.buttonBox.accepted.connect(dlgLogin.accept)
        self.buttonBox.rejected.connect(dlgLogin.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgLogin)

    def retranslateUi(self, dlgLogin):
        _translate = QtCore.QCoreApplication.translate
        dlgLogin.setWindowTitle(_translate("dlgLogin", "TrueMessanger"))
        self.lblLogin.setText(_translate("dlgLogin", "Login:"))
        self.lblPassword.setText(_translate("dlgLogin", "Password:"))

import resources_rc
