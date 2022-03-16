#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 16:10
# @Author  : Marc
# @File    : path_sum_04_12.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class PathSum:
    def __init__(self):
        self.__tmp_path = []
        self.__paths = 0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.preorder(root, 0, sum)
        if root.left is not None:
            self.pathSum(root.left, 0, sum)
        if root.right is not None:
            self.pathSum(root.right, 0, sum)
        return self.__paths

    def preorder(self, root: TreeNode, curr: int, sum: int):
        if root is None:
            return
        curr += root.val
        if curr == sum:
            self.__paths = self.__paths + 1
        self.preorder(root.left, curr, sum)
        self.preorder(root.right, curr, sum)
        curr -= root.val
        return

def main():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    root.right.right.right.right = TreeNode(5)
    test = PathSum()
    sum = 3
    ans = test.pathSum(root, sum)
    print(ans)


if __name__ == "__main__":
    main()
