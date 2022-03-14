#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 20:03
# @Author  : Marc
# @File    : add_two_numbers_02_05.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class AddTwoNumbers0205:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_node_1, current_node_2 = l1, l2
        pre_node = ListNode(0)
        pre_node.next = l1

        while current_node_1:
            if current_node_2:
                current_node_1.val = current_node_1.val + current_node_2.val
            else:
                break
            current_node_1, current_node_2 = current_node_1.next, current_node_2.next
            pre_node = pre_node.next
            if current_node_1 == None:
                pre_node.next = current_node_2
                break

        current_node_1 = l1
        while current_node_1:
            if current_node_1.val > 9:
                current_node_1.val -= 10
                if current_node_1.next == None:
                    current_node_1.next = ListNode(0)
                current_node_1.next.val += 1
            current_node_1 = current_node_1.next
        return l1