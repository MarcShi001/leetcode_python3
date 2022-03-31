#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/31 16:09
# @Author  : Marc
# @File    : three_steps_problem_08_01.py

class ThreeStepsProblem:
    def waysToStep(self, n : int) -> int:
        nums = [0] * (n + 4)
        nums[0] = 1
        nums[1] = 1
        nums[2] = 2
        nums[3] = 4
        nums[4] = 7
        nums[5] = 13
        for i in range(4, n+4):
            nums[i] = (nums[i-1] + nums[i-2] + nums[i-3]) % 1000000007
        return nums[n]