#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 21:27
# @Author  : Marc
# @File    : partition_list_02_04.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class PartitionList0204:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_head = ListNode(x-1)
        greater_head = ListNode(x)
        tmp_less = less_head
        tmp_great = greater_head

        current_node = head
        while current_node:
            if current_node.val < x:
                tmp_less.next = current_node
                tmp_less, current_node = tmp_less.next,  current_node.next
            else:
                tmp_great.next = current_node
                tmp_great, current_node = tmp_great.next, current_node.next
        tmp_less.next = greater_head.next
        tmp_great.next = None
        return less_head.next