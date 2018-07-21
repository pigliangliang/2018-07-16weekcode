#author_by zhuxiaoliang
#2018-07-21 下午3:01
'''


import asyncio
@asyncio.coroutine
def countdown(number,n):
    while n>0:
        print('T-minus',n,'({})'.format(number))
        yield from asyncio.sleep(1)
        n -=1

loop = asyncio.get_event_loop()
tasks =[
    asyncio.ensure_future(countdown('A',2)),
    asyncio.ensure_future(countdown('B',3)),
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()


T-minus 2 (A)
T-minus 3 (B)
T-minus 1 (A)
T-minus 2 (B)
T-minus 1 (B)




python 3.4中引入了协程和事件循环，通过一个装饰器定义一个协程，使用get_event_loop来执行tasks中所有的协程任务。
python 3.5中引入新的语法：async&await，有了原生协程概念。



import  socket
from  concurrent import futures
from selectors import DefaultSelector,EVENT_WRITE,EVENT_READ
import asyncio
import time
now = lambda :time.time()
async def vgg(x):
    print('waiting:',x)
start = now()
coroutine = vgg(2)#创建协程对象
loop = asyncio.get_event_loop()#事件循环
task = loop.create_task(coroutine)#创建任务
#task = loop.ensure_future(coroutine)#同上
loop.run_until_complete(task)#将协程注册到事件循环并启动事件循环
print(task)
'''
#绑定回调函数
'''
在task执行完毕的时候可以获取执行的结果，回调的最后一个参数是future对象，通过该对象可以多去协程返回值
'''

import time
import asyncio


now = lambda :time.time()
async def do_some_work(x):
    print('waiting:',x)
    await asyncio.sleep(2)
    return 'Done after {}s'.format(x)
def callback(future):
    print('callback:',future.result())

start = now()
coroutine = do_some_work(3)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
loop.run_until_complete(task)
print("time:",now()-start)

'''
waiting: 3
callback: Done after 3s
time: 0.00036215782165527344
可以看到协程执行结束后会调用回调函数，并通过future获取协程的执行结果
'''

#async 和await语法
'''
使用async可以定义协程对象，使用await针对耗时的操作进行挂起，等价于yield关键字，让出对cpu的控制权。协程遇到await关键字时间循环将会挂起该协程，执行的协程
知道遇到其他的协程也挂起或者执行完毕，在执行下一个协程。
使用asyncio.sleep函数模拟IO操作。协程的目的是让这些IO异步化。
'''