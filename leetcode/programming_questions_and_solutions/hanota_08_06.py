#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 16:32
# @Author  : Marc
# @File    : hanota_08_06.py


class Hanota:
    def hanota(self, A: list[int], B: list[int], C: list[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        self.recursion_move(len(A), A, B, C)


    def recursion_move(self, n : int, A: list, B: list, C: list) -> None:
        if n == 1:
            C.append(A.pop())
            return
        self.recursion_move(n-1, A, C, B)
        C.append(A.pop())
        self.recursion_move(n-1, B, A, C)
