#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 14:34
# @Author  : Marc
# @File    : legal_binary_search_tree_04_05.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LegalBinarySearchTree:
    def __init__(self):
        self.__pre_node = None

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        ans = self.inorder(root)
        return ans[0]

    def inorder_prenode(self, root: TreeNode):
        if not root:
            return True
        if not self.inorder_prenode(root.left):
            return False
        #访问当前节点
        if self.__pre_node is not None and self.__pre_node.val >= root.val:
            return False
        self.__pre_node = root
        if not self.inorder_prenode(root.right):
            return False
        return True

    def inorder(self, root: TreeNode) -> (bool, TreeNode, TreeNode):
        if not root:
            return (True, root, root)
        left = self.inorder(root.left)
        right = self.inorder(root.right)
        if left[0] and right[0]:
            if left[2] is None and right[1] is None:
                return (True, root, root)
            elif left[2] is None and root.val < right[1].val:
                return (True, root, right[2])
            elif right[1] is None and root.val > left[2].val:
                return (True, left[1], root)
            else:
                if root.val > left[2].val and root.val < right[1].val:
                    return (True, left[1], right[2])
        return (False, None, None)

    def inorder_loop(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        pre_node = None
        while root or len(stack) != 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre_node:
                if pre_node.val >= root.val:
                    return False
            pre_node = root
            root = root.right
        return True

def main():
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    test = LegalBinarySearchTree()
    ans = test.isValidBST(root)
    print(ans)

if __name__ == "__main__":
    main()
