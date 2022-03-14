#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 19:59
# @Author  : Marc
# @File    : delete_node_02_03.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class DeleteNode0203:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next