#author_by zhuxiaoliang
#2018-07-19 下午9:47
import threading
#遇到iO阻塞时候回自动切换任务
import gevent

def eat(name):
    print('%s eat 1' %name)
    #print(threading.current_thread().getName())
    gevent.sleep(3)
    print('%s eat 2'%name)

def play(name):
    print('%s play 1' %name)
    #print('%s 线程-%s' %(name,threading.current_thread().getName()))
    gevent.sleep(2)
    print('%s play 2'%name)

g1 = gevent.spawn(eat,'pig')
g2 = gevent.spawn(play,'pig')

gevent.joinall([g1,g2])
print('main')
'''
输出：
pig eat 1
pig play 1
pig play 2
pig eat 2
main

'''