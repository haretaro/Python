import socket

host = socket.gethostname()
port = 8080
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host,port))
serversocket.listen(5)

clientsocket, address = serversocket.accept()

print('connected by ', address)

while True:
    data = clientsocket.recv(1024)
    if not data: break
    print(data)
    clientsocket.send(data)

clientsocket.close()

