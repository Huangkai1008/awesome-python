# -*- coding:utf-8 -*-
"""
基类
"""


class BaseClass:
    def talk(self):
        print("I am baseClass")


def say(self):
    print("hello")


# 构建类
User = type('User', (BaseClass,), dict(name='user', say=say))

user = User()
user.say()
