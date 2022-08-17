'''el patrón observador se encarga de realizar un conteo de la cantidad de
modificaciones que se ejecutan en la base de datos, y las envia al servidor
mediante la clase Cliente'''
import socket as sk


class Sujeto:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self, *args):
        print("notificado")
        for observador in self.observadores:
            print("observadores: ")
            print(self.observadores)
            observador.update(args)


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)
        self.modificaciones = 0
        self.conexion_servidor = Cliente()

    def update(self, *args):
        self.modificaciones += 1

        print("cantidad de modificaciones: ", self.modificaciones)
        self.conexion_servidor.envio_servidor(self.modificaciones)


class Cliente:

    def envio_servidor(self, info):
        mi_socket = sk.socket()
        # direccion a la que nos necesitamos conectar:
        mi_socket.connect(('localhost', 8000))
        mi_socket.send("cantidad de modificaciones: ".encode())
        mi_socket.send(str(info).encode())
        # buffer 1024 bytes:
        respuesta = mi_socket.recv(1024)
        print(respuesta)
        mi_socket.close()
