#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/21 16:39
# @Author  : Marc
# @File    : reverse_bits_05_03.py

class ReverseBits:
    def reverseBits(self, num: int) -> int:
        """
        :type num: int
        :rtype: int
        """
        current_one, insert_one, ans = 0, 0, 0
        for i in range(32):
            if num & (1<<i):
                current_one += 1
                insert_one += 1
            else:
                insert_one = current_one + 1
                current_one = 0
            ans = max(ans, insert_one)
        return ans