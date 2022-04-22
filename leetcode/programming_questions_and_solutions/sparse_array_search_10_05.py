#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/4/21  1:09 PM
# @Author   : Marc
# @File     : sparse_array_search_10_05


class SparseArraySearch:
    def findString(self, words: list[str], s: str) -> int:
        left, right, middle = 0, len(words) - 1, 0
        while left <= right:
            middle = (left + right) // 2
            tmp = middle
            while words[middle] == "":
                middle = middle - 1
            if words[middle] == s:
                return middle
            elif words[middle] < s:
                left = tmp + 1
            else:
                right = middle-1
        return -1



