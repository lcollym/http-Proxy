# Importamos la biblioteca de sockets, que permite la comunicación en red.
import socket

# Creamos un socket de servidor usando IPv4 (AF_INET) y TCP (SOCK_STREAM).
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asignamos una dirección IP y un puerto al socket del servidor.
# "127.0.0.1" es la dirección de localhost (el propio equipo), y 8888 es el puerto.
server_socket.bind(("127.0.0.1", 8888))

# Ponemos el servidor en modo de escucha, permitiendo que acepte conexiones entrantes.
# El argumento "1" indica que se puede poner en cola una conexión.
server_socket.listen(1)

# Mensaje para indicar que el servidor está listo y escuchando conexiones.
print("Listening on port 8888...")

# Bucle infinito para aceptar múltiples conexiones de clientes.
while True:
    # Espera una conexión de un cliente. Cuando un cliente se conecta, devuelve un socket
    # para comunicarse con el cliente y su dirección.
    client_socket, address = server_socket.accept()

    # Muestra la dirección IP y puerto del cliente conectado.
    print(f"Connection from {address}")

    # Recibe datos del cliente. Aquí recibe hasta 1024 bytes.
    data = client_socket.recv(1024)

    # Decodifica los datos recibidos (de bytes a texto) y los imprime en la consola.
    print(data.decode())

    # Cierra la conexión con el cliente después de procesar la solicitud.
    client_socket.close()
