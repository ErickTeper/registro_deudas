'''Modelo posee la clase BaseDeDatos con la cual podemos establecer conexion
y hacer consultas y modificaciones a la base de datos, 
esta clase se relaciona con main y con observador'''

import sqlite3
from observador import Sujeto
import re
from PyQt5.QtWidgets import QErrorMessage

class BaseDeDatos(Sujeto):

    '''El método Conexión inicia y retorna una conexión con la
    base de datos'''
    def conexion(self):

        # Crea la conexion (y base de datos y tabla en caso de no existir)
        con = sqlite3.connect("base_deudas_v3_0.db")
        cursor = con.cursor()
        sql = "CREATE TABLE IF NOT EXISTS deudas (id integer PRIMARY KEY AUTOINCREMENT,\
                    nombre varchar(20) NOT NULL, apellido varchar(30) NOT NULL,\
                    concepto varchar(20) NOT NULL, monto real NOT NULL, \
                    fecha text, vencimiento text, pagado BOOLEAN)"
        cursor.execute(sql)
        con.commit()

        return con  # retorna la conexion, se utiliza en los demas métodos

    '''confirmacion es una funcion decoradora que corrobora la ejecucion
    de las modificaciones a la base de datos'''
    def confirmacion(arg):
        def interna(self, *args): 
            arg(self, *args)
            print("modificacion efectuada")
        return interna

    '''alta(arg) recibe como argumente una lista con datos y la carga en la
    base de datos agregando un término "None" para la asignacion del ID y
    al final un bolean "false" que indica una deuda no paga'''

    def alta(self, datos_deuda):
        patron = "[a-zA-Z\s]+(-[^\W\d_]+)?$"
        if re.match(patron, datos_deuda[0]):
            print("ejecutando: modelo.BaseDeDatos.alta()")
            con = self.conexion()
            cursor = con.cursor()
            tupla_datos = tuple([None] + datos_deuda + [False])
            sql = "INSERT INTO deudas(id, nombre, apellido, concepto, monto, fecha,\
                  vencimiento, pagado) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
            cursor.execute(sql, tupla_datos)
            self.notificar()
            con.commit()
            con.close()
        else:
            print("ATENCION! solo se aceptan letras en el campo de nombre")

    '''Obtener_tabla() genera una consulta de todas las deudas en la base de datos
    y retorna dichos datos'''

    def obtener_tabla(self):
        print('ejecutando: obtener datos tabla')
        con = self.conexion()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM deudas")
        datos_tabla = cursor.fetchall()
        con.commit()
        con.close()
        return datos_tabla

    '''eliminar_elemento(id_elemento) obtiene por parámetro un ID y elimina de
    la base de datos dicha fila'''

    @confirmacion
    def eliminar_elemento(self, id_seleccionado):
        print("estoy en eliminar_elemento, el id_obtenido es: " + id_seleccionado)
        con = self.conexion()
        cursor = con.cursor()
        id_seleccionado = int(id_seleccionado)
        sql = "DELETE FROM deudas where id = ?;"
        data = (id_seleccionado,)
        cursor.execute(sql, data)
        self.notificar()
        con.commit()
        con.close()

    '''modificar_elemento(id_elemento) obtiene por parámetro un ID y modifica de
    False a True el campo de "pagado" de la tabla de deudores en la fila 
    seleccionada mediante ID'''

    @confirmacion
    def modificar_elemento(self, id_seleccionado):
        print("estoy en modificar_elemento, el id_obtenido es: " + id_seleccionado)
        con = self.conexion()
        cursor = con.cursor()
        id_seleccionado = int(id_seleccionado)
        sql = "UPDATE deudas SET pagado = TRUE where id = ?;"
        data = (id_seleccionado,)
        cursor.execute(sql, data)
        self.notificar()
        con.commit()
        con.close()