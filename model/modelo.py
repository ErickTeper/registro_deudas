import sqlite3
from observador import Sujeto


class BaseDeDatos(Sujeto):

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

    def confirmacion(arg):
        def interna(self, *args): 
            arg(self, *args)
            print("modificacion efectuada")
        return interna

    def alta(self, datos_deuda):
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

    def obtener_tabla(self):
        print('ejecutando: obtener datos tabla')
        con = self.conexion()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM deudas")
        datos_tabla = cursor.fetchall()
        con.commit()
        con.close()
        return datos_tabla

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