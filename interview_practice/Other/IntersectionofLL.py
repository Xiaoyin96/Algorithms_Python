#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''

'''
for example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.
https://leetcode.com/problems/intersection-of-two-linked-lists/
'''
#%% answer in leetcode
class Solution(object):
    def length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        a = self.length(headA)
        b = self.length(headB)
        if a < b:
            a, b = b, a
            headA, headB = headB, headA

        while a > b:
            a -= 1
            headA = headA.next

        while headA:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None

#%% method 1 LL-> list

def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
    if not headA or not headB:
        return None

    aList = []
    bList = [] # append多个linkedlist, [4->1->8->4->5, 1->8->4->5, 8->4->5, 4->5, 5->None]
    tempA = headA
    tempB = headB

    while tempA:
        aList.append(tempA)
        tempA = tempA.next

    while tempB:
        bList.append(tempB)
        tempB = tempB.next

    # 从尾部开始找相同
    while len(aList) > 1 and len(bList) > 1 and aList[-2] == bList[-2]: # -2index: (ListNode{val: 4, next: ListNode{val: 5, next: None}}, 4-->5 比较一个连接
        aList.pop()
        bList.pop()

    if aList[-1] == bList[-1]: #再比较最后一个元素是不是一样-->交点
        return bList[-1] # ListNode{val: 8, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}} 8->4->5
    else:
        return None

#%% method 2 2 pointer: 制定两个指针pA pB,分别用这两个指针遍历A+B,如果两个指针在某点相遇，则该点就是链表的交点
def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        tempA = headA
        tempB = headB
        while tempA!=tempB:
            tempA = tempA.next
            tempB = tempB.next
            if not tempA and not tempB:
                return None
            if not tempA:     #A链表后面接上B链表
                tempA = headB
            if not tempB:     #B链表后面接上A链表
                tempB = headA
        return tempA


#%% headA -> dict: time limit exceeds

class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        dic = {}
        while headA is not None:
            dic[headA] = 1  # 将LL作为Key
            headA = headA.next

        while headB is not None:
            if dic.has_key(headB): # if headB in dic.keys()
                return headB
            heaB = headB.next

        return None