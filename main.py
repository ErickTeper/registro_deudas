from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QTreeWidgetItem
from PyQt5 import QtCore, QtWidgets
from PyQt5 import uic
from model.modelo import BaseDeDatos
from vista.view import Ui_MainWindow
from multiprocessing import Process
import time

class MainWin(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.eventos()
        self.conexion_bd = BaseDeDatos()
        #self.proceso_eventos = Process(target=self.eventos)

        self.show()

    def eventos(self):
        
        self.ui.boton_cargar.clicked.connect(self.cargar_deuda)
        self.ui.boton_importar.clicked.connect(self.importar_tabla)
        
        self.ui.boton_pagado.clicked.connect(
            lambda: self.conexion_bd.modificar_elemento(
                self.ui.tree_deudores.currentItem().text(0)))

        self.ui.boton_pagado.clicked.connect(
            lambda: self.conexion_bd.eliminar_elemento(
                self.ui.tree_deudores.currentItem().text(0)))
        

    def cargar_deuda(self):
        print('ejecutando: main.MainWin.cargar_deuda()')
        nombre = self.ui.input_nombre.text()
        apellido = self.ui.input_apellido.text()
        concepto = self.ui.input_concepto.text()
        monto = self.ui.input_monto.text()
        fecha = self.ui.input_fecha.text()
        vencimiento = self.ui.input_vencimiento.text()
        datos_deuda = [nombre, apellido, concepto, monto, fecha, vencimiento]
        print('enviando a BaseDeDatos.alta(): ')
        print(datos_deuda)
        self.conexion_bd.alta(datos_deuda)

    def importar_tabla(self):
        print('ejecutando: importar tabla')
        self.ui.tree_deudores.clear()
        #consulta = BaseDeDatos()
        datos_tabla = self.conexion_bd.obtener_tabla()
        #print(datos_tabla)
        for datos in datos_tabla:
            lista = []
            for dato in datos:
                lista.append(str(dato))           
            print(lista)
            self.ui.tree_deudores.insertTopLevelItems(dato, [QTreeWidgetItem(self.ui.tree_deudores, lista)])


if __name__ == "__main__":
    app = QApplication([])
    window = MainWin()
    app.exec_()
