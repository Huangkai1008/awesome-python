# -*- coding:utf-8 -*-
import asyncio


async def hello(name):
    print('Hello, ', name)


# 定义协程对象
coroutine = hello('Python')

loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)

loop.run_until_complete(task)
