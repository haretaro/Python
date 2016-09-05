#coding:utf-8
#プロセス間でパイプで通信するテスト
from multiprocessing import Process, Pipe
import time

def f(conn):
    counter = 0
    while True:
        conn.send([42, None, 'Hello', counter])
        counter += 1
        time.sleep(1)
    #conn.close()

parent_conn, child_conn = Pipe()
p = Process(target=f, args=(child_conn,))
p.start()
for _ in range(5):
    print(parent_conn.recv())
p.join(2)#ブロックする.引数はタイムアウト
p.terminate()
print('hoge')
