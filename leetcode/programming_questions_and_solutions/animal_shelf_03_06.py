#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/11 18:05
# @Author  : Marc
# @File    : animal_shelf_03_06.py
from collections import deque

class AnimalShelf:

    def __init__(self):
        self.__all_deque = deque()
        self.__cat_deque = deque()
        self.__dog_deque = deque()




    def enqueue(self, animal: list[int]) -> None:
        self.__all_deque.append(animal)

    def dequeueAny(self) -> list[int]:
        if self.dog_deque:
            return self.dog_deque.popleft()
        if self.cat_deque:
            return self.cat_deque.popleft()
        if self.all_deque:
            return self.all_deque.popleft()
        return [-1, -1]

    def dequeueDog(self) -> list[int]:
        if self.dog_deque:
            return self.dog_deque.popleft()
        while self.all_deque:
            if self.all_deque[0][1] == 1:
                return self.all_deque.popleft()
            self.cat_deque.append(self.all_deque.popleft())
        return [-1, -1]

    def dequeueCat(self) -> list[int]:
        if self.cat_deque:
            return self.cat_deque.popleft()
        while self.all_deque:
            if self.all_deque[0][1] == 0:
                return self.all_deque.popleft()
            self.dog_deque.append(self.all_deque.popleft())
        return [-1, -1]



# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()