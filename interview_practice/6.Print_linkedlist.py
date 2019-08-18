#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入一个链表，从尾到头打印链表每个节点的值。
'''


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
    def print(self, ListNode): #from tail to head
        if ListNode.val == None:
            return None
        stack = []
        head = ListNode
        while head:
            stack.append(head.val)
            head = head.next

        return stack[:-1]


#%%
node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

print