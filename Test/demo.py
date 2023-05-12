#! /usr/bin/env python
# -*-coding:utf-8-*-

"""
四则运算
"""


class Calculator(object):

    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4

    def sum(self):
        print(self.a + self.b)
        return self.a + self.b


if __name__ == '__main__':
    Ca = Calculator()
    Ca.sum()
