#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 23:47
# @Author  : Marc
# @File    : leetcode_29_divide_two_integers.py

class DivideTwoIntegers:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2 ** 31, 2 ** 31 - 1

        sign = 1 if dividend * divisor >= 0 else -1
        cnt, dividend, divisor = 0, abs(dividend), abs(divisor)

        while dividend >= 0:
            if dividend <= divisor:  # 再减一次就结束
                cnt += 1
                dividend -= divisor
            else:  # 减不止一次，那么找到2的次幂对应的b重复次数
                bit_cnt = 0
                while (divisor << bit_cnt) <= dividend:
                    bit_cnt += 1
                cnt += 1 << (bit_cnt - 1)
                dividend -= divisor << (bit_cnt - 1)

        ans = sign * (cnt - 1)
        return ans if MIN_INT <= ans <= MAX_INT else MAX_INT
