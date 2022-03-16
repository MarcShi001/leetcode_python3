#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 15:31
# @Author  : Marc
# @File    : successor_04_06.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Successor:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if root is None:
            return root
        pre_node = None
        stack = []
        while root or len(stack) != 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre_node:
                if pre_node.val == p.val:
                    return root
            pre_node = root
            root = root.right
        return None

def main():
    test = Successor()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    ans = test.inorderSuccessor(root, root.left)
    print(ans.val)


if __name__ == "__main__":
    main()