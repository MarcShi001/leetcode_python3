#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/21 16:49
# @Author  : Marc
# @File    : closed_number_05_04.py

class ClosedNumber:
    def findClosedNumbers(self, num: int) -> list:
        """
        较小数：找到 尽可能低位的 模式串'10' 翻转；若全为1则不存在更小数
        较大数：找到 尽可能低位的 模式串'01' 翻转，若全为1则加一位1，第二位1变0
        """
        b = str(bin(num))[2:]
        if not '0' in b:
            if int('0b10' + b[1:], 2) < int('08fffffff', 16):
                return [int('0b10'+b[1:], 2), -1]
            else:
                return[-1, -1]
        b = '0' + b
        smaller, bigger = None, None
        for i in range(len(b)-1, -1, -1):
            if b[i:i+2] == '10':
                tmp = b[i+2:]
                tmp = '1' * tmp.count('1') + '0' * tmp.count('0')
                smaller = b[:i] + '01' + tmp
                break
        for i in range(len(b)-1, -1, -1):
            if b[i:i+2] == '01':
                tmp = b[i+2:]
                tmp = '0' * tmp.count('0') + '1' * tmp.count('1')
                bigger = b[:i] + '10' + tmp
                break
        print("****************************")
        print(int(bigger,2))
        print(int('08fffffff', 16))
        if int(bigger, 2) < int('08fffffff', 16):
            return [int(bigger, 2), int(smaller, 2)]
        return [-1, int(smaller, 2)]


def main():
    num = 2147483647
    test = ClosedNumber()
    res = test.findClosedNumbers(num)
    print(res)

if __name__ == "__main__":
    main()