#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/4/21  11:18 AM
# @Author   : Marc
# @File     : sorted_merge_10_01

class SortedMerge:
    def merge(self, A: list[int], m: int, B: list[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        i, j, cur = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[cur] = A[i]
                cur = cur - 1
                i = i - 1
            else:
                A[cur] = B[j]
                j = j - 1
                cur = cur - 1
        if i < 0:
            for index in range(j):
                A[index] = B[index]
        return

