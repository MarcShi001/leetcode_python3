#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 23:24
# @Author  : Marc
# @File    : min_stack_03_02.py
import math


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = []
        self.__min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.__stack.append(x)
        self.__min_stack.append(min(x, self.__min_stack[-1]))

    def pop(self) -> None:
        self.__stack.pop()
        self.__min_stack.pop()


    def top(self) -> int:
        return self.__stack[-1]


    def getMin(self) -> int:
        return self.__min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()