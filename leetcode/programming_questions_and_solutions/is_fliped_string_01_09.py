#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 21:48
# @Author  : Marc
# @File    : is_fliped_string_01_09.py

class IsFlipedString:
    def is_fliped_string(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        return s1 in (s2 + s2)