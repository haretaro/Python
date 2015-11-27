import socket

host = '127.0.0.1'
port = 8080
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host,port))
serversocket.listen(5)

clientsocket, address = serversocket.accept()





