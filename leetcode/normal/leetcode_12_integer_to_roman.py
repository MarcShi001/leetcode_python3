#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 20:38
# @Author  : Marc
# @File    : leetcode_12_integer_to_roman.py

class IntegerToRoman:
    def intToRoman(self, num: int) -> str:
        hashmap = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for key in hashmap:
            if num // key != 0:
                count = num // key
                res += hashmap[key]*count
                num = num % key
        return res
