#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 18:55
# @Author  : Marc
# @File    : remove_duplicate_nodes_02_01.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class RemoveDuplicateNode:
    def remove_duplicate_node(self, head: ListNode) -> ListNode:
        pre_node, current_node = None, head
        visited_set = set()
        while current_node:
            if current_node.val in visited_set:
                pre_node.next = current_node.next
            else:
                pre_node = current_node
                visited_set.add(current_node.val)
            current_node = current_node.next
        return head