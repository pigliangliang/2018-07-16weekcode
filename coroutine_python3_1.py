#author_by zhuxiaoliang
#2018-07-22 上午6:52

#asyncio实现异步编程
'''
import asyncio
import time
now = lambda :time.time()
async def do_some_work(x):
    print('waiting:',x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)
start = now()

coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3),

]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
for task in tasks:
    print('result:{}'.format(task.result()))
print('TIME: ', now() - start)

waiting: 1
waiting: 2
waiting: 4
result:Done after 1s
result:Done after 2s
result:Done after 4s
TIME:  4.004709005355835


'''
#协程的嵌套
#使用async 可以定义协程，协程用于耗时的io操作，可以封装更多的io操作。这样就实现协程的嵌套，即：
#一个协程await另外一个协程
import asyncio
import time
now = lambda :time.time()
async def do_some_work(x):
    print('waiting:',x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(3)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3),
    ]
    #dones,pendings = await asyncio.wait(tasks)
    #for task in dones:
    #   print('result:',task.result())

    results = await asyncio.gather(*tasks)

start = now()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print('time:',now()-start)
'''
waiting: 1
waiting: 2
waiting: 3
time: 3.002434730529785
'''

