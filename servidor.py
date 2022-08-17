import socket as sk

mi_socket = sk.socket()  #crea objeto 
mi_socket.bind(('localhost', 8000)) # establece conexion
mi_socket.listen(5) # cantidad de peticiones en cola

while True: 
    conexion, direccion = mi_socket.accept() # acepta conexiones, retorna 2 valores
    print("Nueva conexion establecida")
    print(direccion)
    conexion.send("Servidor activo".encode())
    peticion = conexion.recv(1024)
    print(peticion)
    conexion.close()
