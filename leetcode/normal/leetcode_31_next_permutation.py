#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 21:32
# @Author  : Marc
# @File    : leetcode_31_next_permutation.py


class NextPermutation:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        front, end = len(nums) - 2, len(nums) -1
        while front >= 0 and nums[front] >= nums[front+1]:
            front -= 1
        if front == -1:
            return nums.reverse()
        swap_index = end
        while swap_index > front and nums[front] >= nums[swap_index]:
            swap_index -= 1
        nums[front], nums[swap_index] = nums[swap_index], nums[front]

        for k in range((end - front) // 2):
            nums[front + 1 + k], nums[end - k] = nums[end - k], nums[front + 1 + k]
        return

def main():
    test = NextPermutation()
    nums = [1, 5, 1]
    test.nextPermutation(nums)
    print(",".join(str(x) for x in nums))

if __name__ == "__main__":
    main()