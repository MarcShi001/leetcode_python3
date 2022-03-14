#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 22:08
# @Author  : Marc
# @File    : get_intersection_node_02_07.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class GetIntersectionNode0207:
    def get_intersection_node(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        tmp_nodeA, tmp_nodeB = headA, headB
        lenA, lenB = 0, 0
        while tmp_nodeA is not None:
            lenA += 1
            tmp_nodeA = tmp_nodeA.next
        while tmp_nodeB is not None:
            lenB += 1
            tmp_nodeB = tmp_nodeB.next
        tmp_nodeA, tmp_nodeB = headA, headB
        while lenA > lenB:
            tmp_nodeA = tmp_nodeA.next
            lenA -= 1
        while lenB > lenA:
            tmp_nodeB = tmp_nodeB.next
            lenB -= 1
        while tmp_nodeA != tmp_nodeB:
            tmp_nodeA, tmp_nodeB = tmp_nodeA.next, tmp_nodeB.next
        return tmp_nodeA
        '''
        nodeA, nodeB = headA, headB
        while headA != headB:
            headA = headA.next if headA is not None else nodeB
            headB = headB.next if headB is not None else nodeA
        return headA