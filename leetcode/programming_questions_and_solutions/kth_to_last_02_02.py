#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 19:36
# @Author  : Marc
# @File    : kth_to_last_02_02.py
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class KthToLast0202:
    def kthToLast(self,head: ListNode, k: int) -> int:
        pre_node, tail_node = head, head
        for _ in range(k):
            tail_node = tail_node.next
        while tail_node:
            tail_node, pre_node = tail_node.next, pre_node.next
        return pre_node.val