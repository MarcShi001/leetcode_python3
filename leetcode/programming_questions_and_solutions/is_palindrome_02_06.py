#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 22:31
# @Author  : Marc
# @File    : is_palindrome_02_06.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class IsPalindrome0207:

    def reverse_list(self, head: ListNode) -> ListNode:
        if head is None:
            return True
        current_node, new_head = head.next, head
        new_head.next = None
        while current_node is not None:
            tmp_node = current_node.next
            current_node.next, new_head = new_head, current_node
            current_node = tmp_node
        return  new_head

    def is_palindrome(self, head: ListNode) -> bool:
        slow_node, quick_node = head, head
        while quick_node is not None and quick_node.next is not None:
            slow_node, quick_node = slow_node.next, quick_node.next.next
        half_node = self.reverse_list(slow_node)
        slow_node, quick_node = head, half_node
        result = True
        while slow_node is not None and quick_node is not None:
            if slow_node.val != quick_node.val:
                result = False
                break
            slow_node, quick_node = slow_node.next, quick_node.next
        return result
