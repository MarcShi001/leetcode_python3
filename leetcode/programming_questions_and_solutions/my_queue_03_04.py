#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/8 23:48
# @Author  : Marc
# @File    : my_queue_03_04.py

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__push_stack = []
        self.__pop__stack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.__push_stack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return -1
        if not self.__pop__stack:
            # pushstack --> popstack
            while self.__push_stack:
                self.__pop__stack.append(self.__push_stack.pop())
        return self.__pop__stack.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return -1
        if not self.__pop__stack:
            # pushstack --> popstack
            while self.__push_stack:
                self.__pop__stack.append(self.__push_stack.pop())
        return self.__pop__stack[-1]



    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.__pop__stack and not self.__push_stack:
            return True
        return False

def main():
    test_my_queue = MyQueue()
    test_my_queue.push(1)
    test_my_queue.push(2)
    print(test_my_queue.peek())
    print(test_my_queue.pop())
    print(test_my_queue.empty())

if __name__ == "__main__":
    main()



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()