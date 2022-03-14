#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 20:47
# @Author  : Marc
# @File    : leetcode_13_roman_to_integer.py

class RomanToInteger:
    def romanToInt(self, s: str) -> int:
        roman_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        len_str = len(s)
        answer = 0
        for index in range(len_str - 1):
            if roman_int_map[s[index]] < roman_int_map[s[index+1]]:
                answer -= roman_int_map[s[index]]
            else:
                answer += roman_int_map[s[index]]
        return answer + roman_int_map[s[-1]]