#author_by zhuxiaoliang
#2018-07-21 上午7:50
#通过gevent实现的单线程下的socket并发
from gevent import monkey;monkey.patch_all()
from socket import *
import gevent


def server(server_ip,port):
    s = socket(AF_INET,SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind((server_ip,port))
    s.listen(5)
    while True:
        conn,addr = s.accept()
        gevent.spawn(talk,conn,addr)

def talk(conn,addr):
    try:
        while True:
            res = conn.recv(1024)
            print('client %s:%s msg:%s'\
                  %(addr[0],addr[1],res))
            conn.send(res.upper())
    except Exception as e:
        print(e)
    finally:
        conn.close()

if __name__ =='__main__':
    server('127.0.0.1',8080)