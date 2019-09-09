#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入一个链表，输出该链表中倒数第k个结点。
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
让第一个指针先向前走k-1步，第二个指针保持不动；从第k步开始，第二个指针也开始从链表的头指针开始遍历。
由于两个指针的距离保持在k-1,当第一个指针到达链表的尾节点时，第二个指针刚好到达倒数第k个节点。
注意：1. k = 0
2. head = None
3. len(head) < k
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    def remove(self, head, k):
        if not head or k <= 0: # 1, 3
            return None

        pfast = pslow = head

        for i in range(k-1):
            if pfast.next:
                pfast = pfast.next
            else:
                return None # 2. Linkedlist length < k

        while pfast.next: # last one should not be None
            pfast = pfast.next
            pslow = pslow.next

        return pslow

    def print_ll(self,head):
       if head:
           return head.val

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(14)
node5 = ListNode(19)
node6 = ListNode(20)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

s = solution()
print(s.print_ll(s.remove(node1,3)))
