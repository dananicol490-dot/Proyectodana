# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(800, 600)
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.LbApellido = QLabel(self.centralwidget)
        self.LbApellido.setObjectName(u"LbApellido")
        self.LbApellido.setGeometry(QRect(130, 180, 71, 16))
        self.LbCedula = QLabel(self.centralwidget)
        self.LbCedula.setObjectName(u"LbCedula")
        self.LbCedula.setGeometry(QRect(130, 220, 47, 13))
        self.LbSexo = QLabel(self.centralwidget)
        self.LbSexo.setObjectName(u"LbSexo")
        self.LbSexo.setGeometry(QRect(130, 250, 47, 13))
        self.LbEmail = QLabel(self.centralwidget)
        self.LbEmail.setObjectName(u"LbEmail")
        self.LbEmail.setGeometry(QRect(130, 290, 47, 13))
        self.LbNombre = QLabel(self.centralwidget)
        self.LbNombre.setObjectName(u"LbNombre")
        self.LbNombre.setGeometry(QRect(130, 130, 71, 20))
        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(190, 130, 113, 20))
        self.txtNombre.setMaxLength(20)
        self.txtNombre.setFrame(True)
        self.txtApellidos = QLineEdit(self.centralwidget)
        self.txtApellidos.setObjectName(u"txtApellidos")
        self.txtApellidos.setGeometry(QRect(190, 180, 113, 20))
        self.txtApellidos.setMaxLength(20)
        self.txtEmail = QLineEdit(self.centralwidget)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(170, 290, 113, 20))
        self.txtEmail.setMaxLength(20)
        self.txtCedula = QLineEdit(self.centralwidget)
        self.txtCedula.setObjectName(u"txtCedula")
        self.txtCedula.setGeometry(QRect(180, 220, 113, 20))
        self.txtCedula.setMaxLength(10)
        self.cbSexo = QComboBox(self.centralwidget)
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.setObjectName(u"cbSexo")
        self.cbSexo.setGeometry(QRect(180, 250, 69, 22))
        self.btGuardar = QPushButton(self.centralwidget)
        self.btGuardar.setObjectName(u"btGuardar")
        self.btGuardar.setGeometry(QRect(190, 350, 75, 23))
        self.btLimpiar = QPushButton(self.centralwidget)
        self.btLimpiar.setObjectName(u"btLimpiar")
        self.btLimpiar.setGeometry(QRect(320, 350, 75, 23))
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"MainWindow", None))
        self.LbApellido.setText(QCoreApplication.translate("vtnPrincipal", u"APELLIDOS :", None))
        self.LbCedula.setText(QCoreApplication.translate("vtnPrincipal", u"CEDULA :", None))
        self.LbSexo.setText(QCoreApplication.translate("vtnPrincipal", u"SEXO :", None))
        self.LbEmail.setText(QCoreApplication.translate("vtnPrincipal", u"EMAIL:", None))
        self.LbNombre.setText(QCoreApplication.translate("vtnPrincipal", u"NOMBRES :", None))
        self.cbSexo.setItemText(0, QCoreApplication.translate("vtnPrincipal", u"Seleccionar", None))
        self.cbSexo.setItemText(1, QCoreApplication.translate("vtnPrincipal", u"Masculino", None))
        self.cbSexo.setItemText(2, QCoreApplication.translate("vtnPrincipal", u"Femenino", None))
        self.cbSexo.setItemText(3, QCoreApplication.translate("vtnPrincipal", u"Prefiero no decir", None))

        self.btGuardar.setText(QCoreApplication.translate("vtnPrincipal", u"GUARDAR", None))
        self.btLimpiar.setText(QCoreApplication.translate("vtnPrincipal", u"LIMPIAR ", None))
    # retranslateUi

