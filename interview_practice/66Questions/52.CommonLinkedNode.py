#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入两个链表，找出它们的第一个公共节点。
首先遍历两个链表得到它们的长度，如果m>n，则m链表先走m-n步，然后两个链表再同时走，直到找到第一个相同的节点（即为它们的第一个公共节点）。（推荐，时间复杂度O(m+n),且不需要额外辅助空间）
'''

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def commonNode(self, headA, headB):
        pHead1 = headA
        pHead2 = headB # copy head is important

        if not pHead1 or not pHead2:
            return None

        length1 = 0
        while pHead1:
            pHead1 = pHead1.next # 已经遍历完了head, head -> None
            length1 += 1

        length2 = 0
        while pHead2:
            pHead2 = pHead2.next
            length2 += 1

        if length1 > length2:
            pLong = headA
            pShort = headB
        else:
            pLong = headB
            pShort = headA

        for i in range(abs(length1 - length2)): #先走几步
            pLong = pLong.next

        while pLong and pShort and pLong != pShort:
            pLong = pLong.next
            pShort = pShort.next

        pHead = pLong

        return pHead

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(4)
Node4 = Node(5)
Node5 = Node(6)

Node6 = Node(7)
Node7 = Node(8)



Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node6.next = Node7
Node7.next = Node3

s = Solution()
print(s.commonNode(Node1,Node6).val) # intersection at 4