# -*- coding:utf-8 -*-
# import asyncio
# import time
#
#
# async def _sleep(x):
#     time.sleep(x)
#     return f'暂停了{x}秒'
#
#
# coroutine = _sleep(2)
#
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# loop.run_until_complete(task)
# print(1111)
#
# print('返回结果：{}'.format(task.result()))  # 同步回调

import time
import asyncio


async def _sleep(x):
    time.sleep(x)
    return '暂停了{}秒！'.format(x)


def callback(future):
    print('这里是回调函数，获取返回结果是：', future.result())


coroutine = _sleep(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)

# 添加回调函数
task.add_done_callback(callback)

loop.run_until_complete(task)
