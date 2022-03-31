#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/30 15:05
# @Author  : Marc
# @File    : convert_integer_05_06.py


class ConvertInteger:
    def convertInteger(self, A: int, B: int) -> int:
        '''
        a_bin, b_bin = A & 0xffffffff, B & 0xffffffff
        return bin(a_bin ^ b_bin).count('1')
        '''
        c = A & B
        res = 0
        for i in range(32):
            res += (c >> i) & 1
        return res
