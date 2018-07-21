#author_by zhuxiaoliang
#2018-07-21 上午8:02
#单线程实现
'''
from socket import *

client = socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))

while True:
    msg = input('>>>:').strip()
    if not  msg:continue

    client.send(msg.encode('utf-8'))
    msg= client.recv(1024)
    print(msg)
'''

#多线程实现

from  threading import Thread
from socket import *
import threading

def client(server_ip,port):
    c = socket(AF_INET,SOCK_STREAM)
    c.connect((server_ip,port))

    count = 0
    while True:
        c.send(('%s say hello %s' %(threading.current_thread().getName(),count)).encode('utf-8'))
        msg = c.recv(1024)
        print(msg.decode('utf-8'))
        count+=1

if __name__ =='__main__':
    for i in range(20):
        t = Thread(target=client,args=('127.0.0.1',8080))
        t.start()
        t.join()