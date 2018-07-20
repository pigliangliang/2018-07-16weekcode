#author_by zhuxiaoliang
#2018-07-21 上午7:34

from  gevent import spawn,joinall,monkey;monkey.patch_all()
import time
def task(pid):
    print('Task %s starting'%pid)
    time.sleep(1)
    print('Task %s done' %pid)


def synchronous():
    for i in range(5):
        task(i)

def asynchorous():
    g_l = [spawn(task,i) for i in range(5)]
    joinall(g_l)


if __name__ =='__main__':
    print('synchronous:')
    synchronous()
    print('asynchronous:')
    asynchorous()

'''
输出：
synchronous:
Task 0 starting
Task 0 done
Task 1 starting
Task 1 done
Task 2 starting
Task 2 done
Task 3 starting
Task 3 done
Task 4 starting
Task 4 done
asynchronous:
Task 0 starting
Task 1 starting
Task 2 starting
Task 3 starting
Task 4 starting
Task 0 done
Task 1 done
Task 2 done
Task 3 done
Task 4 done
'''
#可以看出同步函数synchronous中是顺序执行的。异步函数async中是异步执行的，速度较快。