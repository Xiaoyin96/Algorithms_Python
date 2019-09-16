#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''
class RandomListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

class Solution:
    def python_copy(self, pHead): #  method 1
        import copy
        return copy.deepcopy(pHead)

    def clone_resursion(self, pHead): # method 2
        if not pHead:
            return None

        newHead = RandomListNode(pHead.val)
        newHead.random = pHead.random # 有问题！！！还是指向Original的Linkedlist!!
        newHead.next = self.clone_resursion(pHead.next)
        return newHead

    def clone(self, pHead): # method 3
        self.clone_node(pHead)
        self.clone_random(pHead)
        return self.reconnect(pHead)

    def clone_node(self, pHead):
        # 复制原始链表的每个结点, 将复制的结点链接在其原始结点的后面 (in-place in pHead)
        pNode = pHead
        while pNode:
            pNew = RandomListNode(None)
            pNew.val = pNode.val
            pNew.next = pNode.next

            pNode.next = pNew
            pNode = pNew.next # move node to next original node

    def clone_random(self, pHead):
        # 将复制后的链表中的克隆结点的random指针链接到被克隆结点random指针的后一个结点 (in-place)
        # 现在的pHead: A->A'->B->B'->C->C'...
        pNode = pHead
        while pNode:
            pNew = pNode.next # 之前copy的Node
            if pNode.random:
                pNew.random = pNode.random.next
            pNode = pNew.next

    def reconnect(self,pHead):
        # 拆分链表,还原pHead,得到新的pNew
        pNode = pHead
        pNew = newHead = pNode.next
        pNode.next = pNew.next
        pNode = pNode.next
        while pNode:
            pNew.next = pNode.next
            pNew = pNew.next
            pNode.next = pNew.next
            pNode = pNode.next
        return newHead





node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3

S = Solution()
clonedNode = S.python_copy(node1)
clonedNode1 = S.clone_resursion(node1)
clonedNode2 = S.clone(node1)
print(clonedNode.next.val)
print(clonedNode1.next.val)
print(clonedNode2.next.val)
print(clonedNode.random.val)
print(clonedNode1.random.val)
print(clonedNode2.random.val)