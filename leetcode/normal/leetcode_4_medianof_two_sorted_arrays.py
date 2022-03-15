#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 23:09
# @Author  : Marc
# @File    : leetcode_4_medianof_two_sorted_arrays.py

class MedianofTwoSortedArrays:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        #未完待续
        len1, len2 = len(nums1), len(nums2)
        middle = (len1 + len2) // 2
        left1, right1 = 0, len(nums1)
        left2, right2 = 0, len(nums2)
        middle2 = (left2 + right2) // 2
        middl1 = self.get_target(nums1, nums2[middle2])




    def get_target(self, nums: list, target: int) -> int:
        left, right = 0, len(nums) - 1
        middle = (left + right) // 2
        res = -1
        if nums[0] > target:
            return -1
        if nums[right] < target:
            return right+1
        if nums[right] == target:
            return right
        while nums[middle] != target and left < right:
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle
            else:
                left = middle+1
            middle = (left + right) // 2
        return middle
