#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 23:27
# @Author  : Marc
# @File    : leetcode_15_3sum.py

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        len_nums = len(nums)
        res = []
        if not nums or len_nums < 3:
            return res
        nums.sort()
        for i in range(len_nums):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len_nums - 1
            while left < right:
                if (nums[i] + nums[left] + nums[right]) == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while right > left and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif (nums[i] + nums[left] + nums[right]) > 0:
                    right -= 1
                else:
                    left += 1
        return res

