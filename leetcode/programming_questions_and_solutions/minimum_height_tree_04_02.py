#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 12:09
# @Author  : Marc
# @File    : minimum_height_tree_04_02.py

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MinimumHeightTree:
    def sorted_array_to_BST(self, nums: list[int]) -> TreeNode:
        if not nums:
            return None
        len_nums = len(nums)
        root = self.dfs(nums, 0, len_nums-1)
        return root

    def dfs(self, nums: list[int], left: int, right: int) -> TreeNode:
        if left == right:
            return TreeNode(nums[left])
        middle = (left + right) // 2
        root = TreeNode(nums[middle])
        if middle != left:
            root.left = self.dfs(nums, left, middle-1)
        root.right = self.dfs(nums, middle+1, right)
        return root