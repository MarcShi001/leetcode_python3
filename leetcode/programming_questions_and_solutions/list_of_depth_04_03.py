#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 12:26
# @Author  : Marc
# @File    : list_of_depth_04_03.py
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ListOfDepth:
    def listOfDepth(self, tree: TreeNode): # -> list[ListNode]:
        que1 = collections.deque()
        if not tree:
            return None
        que1.append(tree)
        alist = []
        while que1:
            n = len(que1)
            node = ListNode(0)
            head = node
            for _ in range(n):
                p = que1.popleft()
                node.next = ListNode(p.val)
                node = node.next
                if p.left:
                    que1.append(p.left)
                if p.right:
                    que1.append(p.right)
            alist.append(head.next)
        return alist
        # result = []
        # if not tree:
        #     return  result
        # queue =  [tree]
        # while len(queue) != 0:
        #     len_queue = len(queue)
        #     head = ListNode(-1)
        #     tmp = head
        #     for i in range(len_queue):
        #         tmp.next = ListNode(queue[i].val)
        #         tmp = tmp.next
        #         if queue[i].left is not None:
        #             queue.append(queue[i].left)
        #         if queue[i].right is not None:
        #             queue.append(queue[i].right)
        #     queue = queue[len_queue:]
        #     result.append(head.next)
        # return result

def main():
    # [1,2,3,4,5,null,7,8]
    list_of_depth = ListOfDepth()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    result = list_of_depth.listOfDepth(root)
    len_res = len(result)
    for i in range(len_res):
        head = result[i]
        while head:
            print(head.val)
            head = head.next



if __name__ == "__main__":
    main()