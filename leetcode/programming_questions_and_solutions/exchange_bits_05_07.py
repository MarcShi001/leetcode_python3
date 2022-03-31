#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/31 16:02
# @Author  : Marc
# @File    : exchange_bits_05_07.py

class ExchangeBits:
    def exchangeBits(self, num: int) -> int:
        return ((num & 0xaaaaaaaa) >> 1) + ((num & 0x55555555) << 1)