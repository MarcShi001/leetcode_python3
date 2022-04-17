#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 0:32
# @Author  : Marc
# @File    : power_set_08_04.py

class PowerSet:
    def subsets(self, nums: list) -> list:
        result = [[]]
        for num in nums:
            print("num = %d" % num)
            size = len(result)
            tmp = []
            for i in range(size):
                print("i = %d" % (i))
                print(result[i])
                tmp_list = result[i][:]
                tmp_list.append(num)
                tmp.append(tmp_list)
                tmp.append(result[i])
            result = tmp
        print(result)
        return result

    def test(self):
        nums = [1, 2, 3]
        result = self.subsets(nums)

if __name__ == "__main__":
    power_set = PowerSet()
    power_set.test()