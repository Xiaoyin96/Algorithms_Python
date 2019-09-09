#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    def stack(self, head):
        if not head or not head.next:
            return head

        val = []
        temp = head
        while temp:
            val.append(temp.val)
            temp = temp.next

        reversed_val = val[::-1]

        new = head
        cnt = 0
        while new:
            new.val = reversed_val[cnt]
            new = new.next
            cnt += 1

        return head

    def pointer(self, head): # 定义3个指针，分别指向当前遍历到的节点pNode、它的前一个节点pPrev及后一个节点pNext。
        if not head or not head.next:
            return head

        last = None  # 指向上一个节点
        while head:
            # 先用tmp保存pHead的下一个节点的信息，
            # 保证单链表不会因为失去pHead节点的next而就此断裂
            tmp = head.next
            # 保存完next，就可以让pHead的next指向last了
            head.next = last
            # 让last，pHead依次向后移动一个节点，继续下一次的指针反转
            last = head # move last to head
            head = tmp # move head to head.next
        return last


    def print_ll(self, head):
        while head:
            print(head.val)
            head = head.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6


s = solution()
print(s.print_ll(s.pointer(node1)))
# print(s.print_ll(s.pointer(head2)))
