'''El controlodador se encarga de inicializar el sistema y permite
establecer una interacción entre el modelo y la vista (main) '''

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QTreeWidgetItem
from PyQt5 import QtCore, QtWidgets
from PyQt5 import uic
from model.modelo import BaseDeDatos
from vista.main import Ui_MainWindow
from vista.informacion import Ui_informacion
import observador

def actualizar(arg, *args,):
    def interna(self):
        arg(self)
        MainWin.importar_tabla(self)
    return interna


class MainWin(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.eventos()
        print("error")
        self.conexion_bd = BaseDeDatos()
        # patron observador
        self.el_observador = observador.ConcreteObserverA(self.conexion_bd) 
        self.show()

    '''El método eventos ejecuta las acciones de cada boton que
    clickee el usuario'''
    def eventos(self):

        self.ui.boton_cargar.clicked.connect(self.cargar_deuda)
        self.ui.boton_importar.clicked.connect(self.importar_tabla)
        self.ui.boton_info.clicked.connect(self.mostrar_ventana)

        self.ui.boton_pagado.clicked.connect(    
            lambda: self.conexion_bd.modificar_elemento(
                self.ui.tree_deudores.currentItem().text(0)))

        self.ui.boton_eliminar.clicked.connect(
            lambda: self.conexion_bd.eliminar_elemento(
                self.ui.tree_deudores.currentItem().text(0)))

    '''El método cargar_deuda() envía los datos cargados en el formulario
    al modelo mediente un objeto de de la clase BaseDeDatos'''
    @actualizar
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

    '''El método importar_tabla() muestra los datos de la tabla de la base de datos
    y los muerta en el TreeWidget de la vista'''
    def importar_tabla(self):
        print('ejecutando: importar tabla')
        self.ui.tree_deudores.clear()
        datos_tabla = self.conexion_bd.obtener_tabla()
        for datos in datos_tabla:
            lista = []
            for dato in datos:
                lista.append(str(dato))
            # print(lista)
            self.ui.tree_deudores.insertTopLevelItems(dato, [QTreeWidgetItem(self.ui.tree_deudores, lista)])

    '''corrobora si desea salir'''
    def closeEvent(self, event):
        self.pregunta = QMessageBox.question(self, "Sistema de gestion",
                        "seguro que desea salir?", QMessageBox.Yes |
                        QMessageBox.No)

        if self.pregunta == QMessageBox.Yes: event.accept()
        else:
            event.ignore()
    
    '''Muestra ventana con informacion'''
    def mostrar_ventana(self):
        self.ventana = informacion_sistema()
        self.info = Ui_informacion()
        self.info.setupUi(self.ventana)
        self.ventana.show()
        self.ventana.exec_()
    

    '''clase para crear una ventana con informacion'''
class informacion_sistema(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("vista/informacion.ui")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWin()
    app.exec_()
