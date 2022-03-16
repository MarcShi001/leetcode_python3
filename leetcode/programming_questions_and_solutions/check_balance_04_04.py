#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 9:43
# @Author  : Marc
# @File    : check_balance_04_04.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CheckBalance:
    def isBalanced(self, root: TreeNode) -> bool:
        res = self.dfsBalanced(root)
        return res[0]


    def dfsBalanced(self, root: TreeNode) -> (bool, int):
        if not root:
            return (True, 0)
        left = self.dfsBalanced(root.left)
        right = self.dfsBalanced(root.right)
        if left[0] and right[0]:
            if abs(left[1] - right[1]) <= 1:
                return (True, max(left[1], right[1])+1)
        return (False, max(left[1], right[1])+1)

    def dfsBottomToUp(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.dfsBottomToUp(root.left)
        right = self.dfsBottomToUp(root.right)
        if left == -1 or right == -1 or abs(left -right) > 1:
            return -1
        return max(left, right) + 1

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    test = CheckBalance()
    ans = test.isBalanced(root)
    print(ans)

if __name__ == "__main__":
    main()
