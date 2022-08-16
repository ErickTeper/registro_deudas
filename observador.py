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

    def update(self, *args):
        self.modificaciones += 1
        
        print("cantidad de modificaciones: ", self.modificaciones)
