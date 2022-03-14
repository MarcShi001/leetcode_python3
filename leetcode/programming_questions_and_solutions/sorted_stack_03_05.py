#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/11 17:33
# @Author  : Marc
# @File    : sorted_stack_03_05.py


class SortedStack:

    def __init__(self):
        self.__sort_stack = []
        self.__tmp_stack = []


    def push(self, val: int) -> None:
        if not self.__sort_stack:
            self.__sort_stack.append(val)
            return
        tmp_val = self.__sort_stack[-1]
        while tmp_val < val:
            self.__tmp_stack.append(tmp_val)
            self.__sort_stack.pop()
            if not self.__sort_stack:
                break
            tmp_val = self.__sort_stack[-1]
        self.__sort_stack.append(val)
        while self.__tmp_stack:
            tmp_val = self.__tmp_stack.pop()
            self.__sort_stack.append(tmp_val)



    def pop(self) -> None:
        if not self.__sort_stack:
            return
        val = self.__sort_stack.pop()
        return


    def peek(self) -> int:
        if not self.__sort_stack:
            return -1
        val = self.__sort_stack[-1]
        return val



    def isEmpty(self) -> bool:
        return not self.__sort_stack

def main():
    sorted_stack = SortedStack()
    sorted_stack.push(1)
    sorted_stack.push(2)
    val = sorted_stack.peek()
    print("val = %d" % (val))
    sorted_stack.pop()
    val = sorted_stack.peek()
    print("val = %d" % (val))

if __name__ == "__main__":
    main()


# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()