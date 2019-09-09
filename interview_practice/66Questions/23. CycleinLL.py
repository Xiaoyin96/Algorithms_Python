#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
如果一个链表中包含环，如何找出环的入口节点？
https://leetcode.com/problems/linked-list-cycle/description/
1）如何判断一个链表中是否包含环？1.两个指针一个fast、一个slow同时从一个链表的头部出发, fast一次走2步，slow一次走一步，如果该链表有环，两个指针必然在环内相遇，
2）如何得到环中节点的数目n？ 接着步骤1，如果两个指针相遇，必然在环内，所以可以从这个节点出发，一遍继续向前移动，一遍计数，当再次回到这个节点时，就可以得到环中节点数了
3）如何找到环的入口节点？ P1先在LL上走n步， 然后P1P2一起走，P2到达入口的时候P1正好走了一圈回到了入口，则P1P2在入口相遇;
OR 其中的一个指针重新指向链表头部，另一个不变（还在环内），这次两个指针一次走一步，相遇的地方就是入口节点
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    def cycle(self,head):
        if not head:
            return None

        pFast = head
        pSlow = head
        while pFast != None and pFast.next != None:
            pFast = pFast.next.next # 走两步
            pSlow = pSlow.next
            if pFast == pSlow: # 相遇
                break

        if pFast == None or pFast.next == None: # 如果是最后的节点，不是真的环
            return None

        pFast = head # 重置到头节点
        while pFast != pSlow:
            pFast = pFast.next
            pSlow = pSlow.next

        return pFast

    def Node(self,head):
        return head.val

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
node6.next = node3

s = solution()
print(s.Node(s.cycle(node1)))

