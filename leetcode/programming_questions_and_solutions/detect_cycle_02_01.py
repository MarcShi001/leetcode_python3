#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 22:53
# @Author  : Marc
# @File    : detect_cycle_02_01.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class DetectCycle0201:
    def detect_cycle(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        if head.next == head:
            return head
        slow_node, quick_node = head, head
        while quick_node is not None:
            slow_node, quick_node = slow_node.next, quick_node.next
            if quick_node is None:
                return None
            else:
                quick_node = quick_node.next
            if quick_node == slow_node:
                break
        if quick_node is None:
            return None
        tmp_node = head
        while tmp_node != slow_node:
            tmp_node, slow_node = tmp_node.next, slow_node.next
        return tmp_node

def main():
    # [3,2,0,-4], pos = 1
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next

    detect_cycle_test = DetectCycle0201()
    node = detect_cycle_test.detect_cycle(head)
    print(node.val)
if __name__ == '__main__':
    main()

