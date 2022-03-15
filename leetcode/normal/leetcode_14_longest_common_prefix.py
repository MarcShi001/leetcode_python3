#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 23:10
# @Author  : Marc
# @File    : leetcode_14_longest_common_prefix.py


class LongestCommonPrefix:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        #题解： https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
        #解法1： 横向扫描，两两运算
        #解法2： 纵向扫描，按位比较
        #解法3： 分治算法
        len0, count = len(strs[0]), len(strs)

        for i in range(len0):
            tmp_char = strs[0][i]
            if any(i == len(strs[j]) or tmp_char != strs[j][i] for j in range(count)):
                return strs[0][0:i]
        return strs[0]