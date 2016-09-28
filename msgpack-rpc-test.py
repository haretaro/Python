#coding: utf-8
#ref: http://qiita.com/miyox/items/1416f3126c2196c71138
import msgpackrpc

class TestServer(object):
    def hello(self, message):
        print(message)
        return ("Hello, " + message.decode()).encode()

    def add(self, a, b):
        return a + b

server = msgpackrpc.Server(TestServer())
server.listen(msgpackrpc.Address('localhost', 1985))
server.start()
