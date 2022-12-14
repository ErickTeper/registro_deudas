'''Esta es la vista, la cual se relaciona unicamente con
el controlador, aquí unicamente desarrollamos la interfaz mediante PyQT.
De este modo garantizamos menor acoplamiento, haciendo al sistema más escalable
a la hora de añadir nuevas funcionalidades'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vista.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(747, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_base = QtWidgets.QFrame(self.centralwidget)
        self.frame_base.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_base.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_base.setObjectName("frame_base")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_base)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_superior = QtWidgets.QFrame(self.frame_base)
        self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_superior.setStyleSheet("QFrame{\n"
"    background-color: rgb(94, 150, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"background-color: #A9C8FC;\n"
"font-family:Trebuchet MS;\n"
"font-size: 24px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(94, 150, 255);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #A9C8FC;\n"
"border-radius: 5px;\n"
"}")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.boton_guardar = QtWidgets.QPushButton(self.frame_superior)
        self.boton_guardar.setMinimumSize(QtCore.QSize(30, 30))
        self.boton_guardar.setMaximumSize(QtCore.QSize(40, 40))
        self.boton_guardar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_guardar.setStyleSheet("")
        self.boton_guardar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./imagenes/disquete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_guardar.setIcon(icon)
        self.boton_guardar.setIconSize(QtCore.QSize(20, 20))
        self.boton_guardar.setObjectName("boton_guardar")
        self.horizontalLayout.addWidget(self.boton_guardar)
        self.boton_importar = QtWidgets.QPushButton(self.frame_superior)
        self.boton_importar.setMinimumSize(QtCore.QSize(35, 35))
        self.boton_importar.setMaximumSize(QtCore.QSize(40, 40))
        self.boton_importar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_importar.setStyleSheet("")
        self.boton_importar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./imagenes/importar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_importar.setIcon(icon1)
        self.boton_importar.setIconSize(QtCore.QSize(24, 24))
        self.boton_importar.setObjectName("boton_importar")
        self.horizontalLayout.addWidget(self.boton_importar)
        self.boton_info = QtWidgets.QPushButton(self.frame_superior)
        self.boton_info.setMinimumSize(QtCore.QSize(35, 35))
        self.boton_info.setMaximumSize(QtCore.QSize(40, 40))
        self.boton_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_info.setStyleSheet("")
        self.boton_info.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./imagenes/informacion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_info.setIcon(icon2)
        self.boton_info.setIconSize(QtCore.QSize(25, 25))
        self.boton_info.setObjectName("boton_info")
        self.horizontalLayout.addWidget(self.boton_info)
        self.label = QtWidgets.QLabel(self.frame_superior)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 6)
        self.verticalLayout_2.addWidget(self.frame_superior)
        self.frame_inferior = QtWidgets.QFrame(self.frame_base)
        self.frame_inferior.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_inferior.setStyleSheet("background-color: rgb(94, 150, 255);")
        self.frame_inferior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inferior.setObjectName("frame_inferior")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_inferior)
        self.horizontalLayout_2.setContentsMargins(3, 0, 3, 3)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_izq = QtWidgets.QFrame(self.frame_inferior)
        self.frame_izq.setStyleSheet("QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.494, y2:0, stop:0 rgba(106, 161, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;\n"
"}")
        self.frame_izq.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_izq.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_izq.setObjectName("frame_izq")
        self.frame_3 = QtWidgets.QFrame(self.frame_izq)
        self.frame_3.setGeometry(QtCore.QRect(30, 90, 141, 241))
        self.frame_3.setStyleSheet("QFrame{\n"
"background-color: RBGA(0,0,0,0)\n"
"}\n"
"\n"
"QLabel{\n"
"background-color: qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.494, y2:0, stop:0 rgba(106, 161, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font-family:Trebuchet MS;\n"
"font-size: 17px;\n"
"border-radius: 10px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_nombre = QtWidgets.QLabel(self.frame_3)
        self.label_nombre.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nombre.setObjectName("label_nombre")
        self.verticalLayout_3.addWidget(self.label_nombre)
        self.label_apellido = QtWidgets.QLabel(self.frame_3)
        self.label_apellido.setAlignment(QtCore.Qt.AlignCenter)
        self.label_apellido.setObjectName("label_apellido")
        self.verticalLayout_3.addWidget(self.label_apellido)
        self.label_concepto = QtWidgets.QLabel(self.frame_3)
        self.label_concepto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_concepto.setObjectName("label_concepto")
        self.verticalLayout_3.addWidget(self.label_concepto)
        self.label_monto = QtWidgets.QLabel(self.frame_3)
        self.label_monto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_monto.setObjectName("label_monto")
        self.verticalLayout_3.addWidget(self.label_monto)
        self.label_fecha = QtWidgets.QLabel(self.frame_3)
        self.label_fecha.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fecha.setObjectName("label_fecha")
        self.verticalLayout_3.addWidget(self.label_fecha)
        self.label_vencimiento = QtWidgets.QLabel(self.frame_3)
        self.label_vencimiento.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vencimiento.setObjectName("label_vencimiento")
        self.verticalLayout_3.addWidget(self.label_vencimiento)
        self.frame_4 = QtWidgets.QFrame(self.frame_izq)
        self.frame_4.setGeometry(QtCore.QRect(170, 90, 171, 241))
        self.frame_4.setStyleSheet("QFrame{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: #A9C8FC;\n"
"border-radius: 10px;\n"
"border: 1px solid;\n"
"border-color: rgb(57, 104, 193);\n"
"}\n"
"QLineEdit:hover{\n"
"background-color: #A9C8FC;\n"
"border-radius: 10px;\n"
"border: 1px solid;\n"
"border-color: rgb(203, 219, 255);\n"
"}\n"
"\n"
"QDateEdit{\n"
"background-color: #A9C8FC;\n"
"border: 1px solid;\n"
"border-color: rgb(57, 104, 193);\n"
"}\n"
"\n"
"QDateEdit:hover{\n"
"background-color: #A9C8FC;\n"
"border: 1px solid;\n"
"border-color: rgb(203, 219, 255);\n"
"}\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.input_nombre = QtWidgets.QLineEdit(self.frame_4)
        self.input_nombre.setMinimumSize(QtCore.QSize(0, 40))
        self.input_nombre.setObjectName("input_nombre")
        self.verticalLayout_4.addWidget(self.input_nombre)
        self.input_apellido = QtWidgets.QLineEdit(self.frame_4)
        self.input_apellido.setMinimumSize(QtCore.QSize(0, 40))
        self.input_apellido.setObjectName("input_apellido")
        self.verticalLayout_4.addWidget(self.input_apellido)
        self.input_concepto = QtWidgets.QLineEdit(self.frame_4)
        self.input_concepto.setMinimumSize(QtCore.QSize(0, 40))
        self.input_concepto.setObjectName("input_concepto")
        self.verticalLayout_4.addWidget(self.input_concepto)
        self.input_monto = QtWidgets.QLineEdit(self.frame_4)
        self.input_monto.setMinimumSize(QtCore.QSize(0, 40))
        self.input_monto.setObjectName("input_monto")
        self.verticalLayout_4.addWidget(self.input_monto)
        self.input_fecha = QtWidgets.QDateEdit(self.frame_4)
        self.input_fecha.setMinimumSize(QtCore.QSize(0, 40))
        self.input_fecha.setObjectName("input_fecha")
        self.verticalLayout_4.addWidget(self.input_fecha)
        self.input_vencimiento = QtWidgets.QDateEdit(self.frame_4)
        self.input_vencimiento.setMinimumSize(QtCore.QSize(0, 40))
        self.input_vencimiento.setObjectName("input_vencimiento")
        self.verticalLayout_4.addWidget(self.input_vencimiento)
        self.label_8 = QtWidgets.QLabel(self.frame_izq)
        self.label_8.setGeometry(QtCore.QRect(30, 40, 301, 31))
        self.label_8.setStyleSheet("\n"
"QLabel{\n"
"background-color: RBGA(0,0,0,0);\n"
"font-family:Trebuchet MS;\n"
"font-size: 20px;\n"
"}")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.boton_cargar = QtWidgets.QPushButton(self.frame_izq)
        self.boton_cargar.setGeometry(QtCore.QRect(90, 350, 181, 41))
        self.boton_cargar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_cargar.setStyleSheet("QPushButton{\n"
"font-size:16px;\n"
"border-radius: 10px;\n"
"border: 1px solid;\n"
"border-color: rgb(57, 104, 193);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(66, 100, 194);\n"
"border-color: rgb(212, 220, 255);\n"
"}\n"
"\n"
"")
        self.boton_cargar.setObjectName("boton_cargar")
        self.horizontalLayout_2.addWidget(self.frame_izq)
        self.frame_2 = QtWidgets.QFrame(self.frame_inferior)
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.494, y2:0, stop:0 rgba(106, 161, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.boton_eliminar = QtWidgets.QPushButton(self.frame_2)
        self.boton_eliminar.setGeometry(QtCore.QRect(190, 350, 151, 41))
        self.boton_eliminar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_eliminar.setStyleSheet("QPushButton{\n"
"font-size:16px;\n"
"border-radius: 10px;\n"
"border: 1px solid;\n"
"border-color: rgb(57, 104, 193);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(66, 100, 194);\n"
"border-color: rgb(212, 220, 255);\n"
"}\n"
"\n"
"")
        self.boton_eliminar.setObjectName("boton_eliminar")
        self.boton_pagado = QtWidgets.QPushButton(self.frame_2)
        self.boton_pagado.setGeometry(QtCore.QRect(40, 350, 141, 41))
        self.boton_pagado.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_pagado.setStyleSheet("QPushButton{\n"
"font-size:16px;\n"
"border-radius: 10px;\n"
"border: 1px solid;\n"
"border-color: rgb(57, 104, 193);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(66, 100, 194);\n"
"border-color: rgb(212, 220, 255);\n"
"}\n"
"\n"
"")
        self.boton_pagado.setObjectName("boton_pagado")
        self.tree_deudores = QtWidgets.QTreeWidget(self.frame_2)
        self.tree_deudores.setGeometry(QtCore.QRect(40, 40, 291, 291))
        self.tree_deudores.setStyleSheet("QTreeWidget{\n"
"border: 1px solid;\n"
"border-color: rgb(57, 104, 193);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QHeaderView{\n"
"background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: #A9C8FC;\n"
"border-right: 1px solid rgb(139, 176, 255);\n"
"border-bottom: 1px solid rgb(66, 96, 166);\n"
"border-radius:5px;\n"
"font-family:Trebuchet MS;\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
" background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QScrollBar::handle{\n"
"background-color:#A9C8FC;\n"
"border-radius:5px;\n"
"}\n"
"")
        self.tree_deudores.setObjectName("tree_deudores")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.frame_inferior)
        self.verticalLayout.addWidget(self.frame_base)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grupo10"))
        self.label.setText(_translate("MainWindow", "SISTEMA DE GESTION DE DEUDAS"))
        self.label_nombre.setText(_translate("MainWindow", "NOMBRE"))
        self.label_apellido.setText(_translate("MainWindow", "APELLIDO"))
        self.label_concepto.setText(_translate("MainWindow", "CONCEPTO"))
        self.label_monto.setText(_translate("MainWindow", "MONTO"))
        self.label_fecha.setText(_translate("MainWindow", "FECHA"))
        self.label_vencimiento.setText(_translate("MainWindow", "VENCIMIENTO"))
        self.label_8.setText(_translate("MainWindow", "CARGAR DEUDA"))
        self.boton_cargar.setText(_translate("MainWindow", "CARGAR"))
        self.boton_eliminar.setText(_translate("MainWindow", "ELIMINAR"))
        self.boton_pagado.setText(_translate("MainWindow", "PAGADO"))
        self.tree_deudores.headerItem().setText(0, _translate("MainWindow", "id"))
        self.tree_deudores.headerItem().setText(1, _translate("MainWindow", "nombre"))
        self.tree_deudores.headerItem().setText(2, _translate("MainWindow", "apellido"))
        self.tree_deudores.headerItem().setText(3, _translate("MainWindow", "concepto"))
        self.tree_deudores.headerItem().setText(4, _translate("MainWindow", "monto"))
        self.tree_deudores.headerItem().setText(5, _translate("MainWindow", "fecha"))
        self.tree_deudores.headerItem().setText(6, _translate("MainWindow", "vencimiento"))
        self.tree_deudores.headerItem().setText(7, _translate("MainWindow", "pagado"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
