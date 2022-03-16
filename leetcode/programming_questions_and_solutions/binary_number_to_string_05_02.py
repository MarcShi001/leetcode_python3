#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 16:39
# @Author  : Marc
# @File    : binary_number_to_string_05_02.py

class BinaryNumberToString:
    def printBin(self, num: float) -> str:
        base = 0.5
        ans = '0.'
        count = 30
        while num > 0. and count:
            if num >= base:
                ans += '1'
                num -= base
            else:
                ans += '0'
            base *= 0.5
            count -= 1
        if num > 0:
            return "ERROR"
        return ans

def main():
    test = BinaryNumberToString()
    num = 0.625
    ans = test.printBin(num)
    print(ans)


if __name__ == "__main__":
    main()