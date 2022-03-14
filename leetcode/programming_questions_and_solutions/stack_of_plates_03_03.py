#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/8 23:13
# @Author  : Marc
# @File    : stack_of_plates_03_03.py

class StackOfPlates:

    def __init__(self, cap: int):
        self.__stack = []
        self.__size = cap

    def push(self, val: int) -> None:
        if not self.__stack or len(self.__stack[-1]) == self.__size:
            if self.__size > 0:
                self.__stack.append([val])
        else:
            self.__stack[-1].append(val)

    def pop(self) -> int:
        if not self.__stack:
            return -1
        else:
            top = self.__stack[-1]
            val = top.pop()
            if not top:
                self.__stack.pop()
            return val


    def popAt(self, index: int) -> int:
        if not self.__stack or index > len(self.__stack):
            return -1
        current = self.__stack[index]
        val = current.pop()
        if not current:
            self.__stack.pop(index)
        return val



# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)