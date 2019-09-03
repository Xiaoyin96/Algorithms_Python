#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''

class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, None)))))))))
# 1->2->3->4->5->6->7->8->9

#%% LL -> list
def reverse_linkedlist(head):
    val = []
    pointer = head

    while head:
        val.append(head.val)
        head = head.next

    reverse_val = val[::-1]

    index = 0
    head_new = pointer
    while pointer:
        pointer.val = reverse_val[index]
        index += 1
        pointer = pointer.next

    return head_new

link_new = reverse_linkedlist(link)
while link_new:
    print(link_new.val)
    link_new = link_new.next # 9,8,7,6,5,4,3,2,1

#%% 2 pointers
