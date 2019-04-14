# -*- coding: utf-8 -*-
"""
    Created by Huang
    Date: 2019/4/14
    创建并开启子进程
"""
from multiprocessing import Process
import time, os

"""
第一种：直接定义
"""


def task(name):
    print(f'{name} is running')
    time.sleep(1)
    print(f'{name} is done')


"""
第二种：继承Process类
"""


class MyProcess(Process):
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        print(f'{os.getpid()} is running, parent_id is {os.getppid()} ')
        time.sleep(1)
        print(f'{os.getpid()} is done, parent_id is {os.getppid()}')


if __name__ == '__main__':
    # p = Process(target=task, args=('hello',))
    # p.start()

    # 创建4个进程
    processes = [MyProcess() for i in range(4)]

    for process in processes:
        process.start()
    print('主进程', os.getpid())

    p = Process(target=task, name='sub_process')
    p.start()
    p.terminate()  # 这里仅仅是给系统发要求让p死掉，但是是需要时间的，所以立即执行is_alive则进程还是活的
    time.sleep(3)
    print(p.is_alive())
