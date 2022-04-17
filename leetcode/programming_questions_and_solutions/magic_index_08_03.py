#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 23:55
# @Author  : Marc
# @File    : magic_index_08_03.py


class MagicIndex:
    def findMagicIndex(self, nums: list) -> int:
        i = 0
        while i < len(nums):
            if i == nums[i]:
                return i
            elif i < nums[i]:
                i = nums[i]
            else:
                i = i + 1
        return -1
        '''
        ans, left, right = -1, 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == middle:
                ans = middle
                break
            elif nums[middle] > middle:
                right = middle - 1
            else:
                
        return ans
        '''

    def test(self):
        nums = [0, 0 ,2]
        ans = self.findMagicIndex(nums)
        print("ans = ", ans)


if __name__ == "__main__":
    magic_index = MagicIndex()
    magic_index.test()