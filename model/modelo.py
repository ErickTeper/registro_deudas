import sqlite3


class BaseDeDatos:

    def conexion(self):

        # Crea la conexion (y base de datos y tabla en caso de no existir)
        self.con = sqlite3.connect("base_deudas_v3_0.db")
        self.cursor = self.con.cursor()
        self.sql = "CREATE TABLE IF NOT EXISTS deudas (id integer PRIMARY KEY AUTOINCREMENT,\
                    nombre varchar(20) NOT NULL, apellido varchar(30) NOT NULL,\
                    concepto varchar(20) NOT NULL, monto real NOT NULL, \
                    fecha text, vencimiento text, pagado BOOLEAN)"
        self.cursor.execute(self.sql)
        self.con.commit()

        return self.con  # retorna la conexion, se utiliza en los demas métodos

    def alta(self, datos_deuda):
        print("ejecutando: modelo.BaseDeDatos.alta()")
        con = self.conexion()
        cursor = con.cursor()
        tupla_datos = tuple([None] + datos_deuda + [False])
        sql = "INSERT INTO deudas(id, nombre, apellido, concepto, monto, fecha,\
               vencimiento, pagado) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(sql, tupla_datos)
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

    def eliminar_elemento(self, id_seleccionado):
        print("estoy en eliminar_elemento, el id_obtenido es: " + id_seleccionado)
        con = self.conexion()
        cursor = con.cursor()
        id_seleccionado = int(id_seleccionado)
        sql = "DELETE FROM deudas where id = ?;"
        data = (id_seleccionado,)
        cursor.execute(sql, data)
        con.commit()
        con.close()

    def modificar_elemento(self, id_seleccionado):
        print("estoy en modificar_elemento, el id_obtenido es: " + id_seleccionado)
        con = self.conexion()
        cursor = con.cursor()
        id_seleccionado = int(id_seleccionado)
        sql = "UPDATE deudas SET pagado = TRUE where id = ?;"
        data = (id_seleccionado,)
        cursor.execute(sql, data)
        con.commit()
        con.close()
