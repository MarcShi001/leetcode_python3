#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/26 16:10
# @Author  : Marc
# @File    : Leetcode_offer_9.py

class Leetcode_offer_9:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        if not self.stack1:
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
