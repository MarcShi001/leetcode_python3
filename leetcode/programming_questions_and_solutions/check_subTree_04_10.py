#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 15:41
# @Author  : Marc
# @File    : check_subTree_04_10.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CheckSubTree:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        '''
        if t2 is None:
            return True
        if t2 is not None and t1 is None:
            return False
        elif t2.val == t1.val:
            return self.checkSubTree(t1.left, t2.left) and self.checkSubTree(t1.right, t2.right)
        else:
            return self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)
        '''
        t1_str = self.serialize_tree(t1)
        t2_str = self.serialize_tree(t2)
        return t1_str.find(t2_str) != -1

    def serialize_tree(self, root: TreeNode):
        if root is None:
            return "#"
        left = self.serialize_tree(root.left)
        right = self.serialize_tree(root.right)

        return left + "," + str(root.val)  + "," + right
