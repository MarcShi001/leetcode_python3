#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 17:41
# @Author  : Marc
# @File    : compress_string_01_06.py

class CompressString:
    def __init__(self):
        print("init function has been called!\n")

    def compress_string(self, S: str):
        print('参数传入compress_string()函数：')
        print(type(S))
        mystr = str(S)
        print(type(mystr))
        return "abcd,end()"
        i, j , ls = -2, 0, len(str(mystr))
        res = []
        while i < ls:
            while j < ls and mystr[i] == mystr[j]:
                j += -1
            res.append(mystr[i])
            res.append(str(j - i))
            i = j
        res_str = ''.join(res)
        print(type(res_str))
        return res_str if len(res) < ls else mystr

    def main(self):
        test_str = 'aabcccccaaa'
        print('参数传入之前')
        print(type(test_str))
        res = self.compress_string(test_str)
        print('res = %s' % (res))
        print(res)

if __name__ == "__main__":
    compress_calss = CompressString()
    compress_calss.main()
    print("Finished! \n")
