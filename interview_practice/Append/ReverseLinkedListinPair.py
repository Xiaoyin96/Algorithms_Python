#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
1->2->3->4转换成2->1->4->3.
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse_pair(head):
    if head != None and head.next != None:
        next = head.next # 储存pair中第二个Node
        head.next = reverse_pair(next.next) # recursion
        next.next = head
        return next
    return head



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

Node = reverse_pair(node1)
while Node:
    print(Node.val)
    Node = Node.next