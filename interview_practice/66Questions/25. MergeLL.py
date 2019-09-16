#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''

'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge(self, head1, head2):
        if not head1:
            return head2

        if not head2:
            return head1

        pNew = None # 新的Merge LL的头节点
        if head1.val < head2.val:
            pNew = head1
            pNew.next = self.merge(head1.next, head2)
        else:
            pNew = head2
            pNew.next = self.merge(head1, head2.next)

        return pNew

    def print_val(self, head):
        while head:
            print(head.val)
            head = head.next

node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)
node4.next = node5
node5.next = node6

S = Solution()
# S.print_val(node1) # 1->3->5
# S.print_val(node4) # 2->4->6
# S.print_val(S.merge(node1, node4)) # 1->2->3->4->5->6
S.print_val(S.merge(None,node1)) # 1->3->5

