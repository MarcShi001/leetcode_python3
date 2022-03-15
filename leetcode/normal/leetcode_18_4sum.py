#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 11:02
# @Author  : Marc
# @File    : leetcode_18_4sum.py

class FourSum:
    def fourSum(self, nums: list, target: int) -> list:
        nums.sort()
        len_nums = len(nums)
        res = []
        if not nums or len_nums < 4:
            return res
        for i in range(len_nums-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(len_nums-3-i):
                if j > 0 and nums[i+j+1] == nums[i+j]:
                    continue
                left = i+j +2
                right = len_nums-1
                while left < right:
                    if target == nums[i] + nums[i+j+1] + nums[left] + nums[right]:
                        res.append([nums[i], nums[i+j+1], nums[left], nums[right]])
                        while left < right and nums[left+1] == nums[left]:
                            left += 1
                        while left < right and nums[right-1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif target > nums[i] + nums[i+j+1] + nums[left] + nums[right]:
                        left += 1
                    else:
                        right -= 1
        return res

def main():
    nums = [0, 0, 0, 0]
    test = FourSum()
    target = 0
    res = test.fourSum(nums, target)
    for i in range(len(res)):
        print(res[i])

if __name__ == "__main__":
    main()