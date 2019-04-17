# -*- coding:utf-8 -*-
import asyncio


async def do_something(x):
    print('Waiting ', x)
    await asyncio.sleep(x)
    return f'Done after{x}'


# 协程对象
coroutine1 = do_something(1)
coroutine2 = do_something(2)
coroutine3 = do_something(4)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
