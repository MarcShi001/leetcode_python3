#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/04/18 11:15
# @Author   : Marc
# @File     : $Recursive_multply_08_05

class RecursiveMultiply:
    def multiply(self, A: int, B: int) -> int:
        if A == 0:
            return 0
        tmp = self.multiply(A>>1, B)
        if A % 2:
            return B + tmp + tmp
        else:
            return tmp + tmp
