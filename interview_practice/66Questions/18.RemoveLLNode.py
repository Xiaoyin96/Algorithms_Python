#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin

'''
'''
给定单向链表的头指针和一个结点指针,定义一个函数在O(1)时间删除该结点
'''


class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def delete_node(head, node):
    if not (head and node):
        return False

    if head == node: # only one node
        head.val = None
        head.next = None
        node.val = None
        node.next = None


    if node.next: # node is not tail node
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
        next_node.val = None
        next_node.next = None
    else: # if tail node, have to traverse
        temp = head
        while temp.next != node:
            temp = temp.next
        temp.next = None
        node = None

    return head

def print_node(head):
    while head:
        print(head.val)
        head = head.next

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4

print(print_node(node1))
print(print_node(delete_node(node1,node4)))

