#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
inorder traversal: pNode->left->right
'''

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def Next(self, pNode):
        if not pNode:
            return None

        # 如果该节点有右子树，那么下一个节点就是它右子树中的最左节点
        if pNode.right != None: #
            pNode = pNode.right
            while pNode.left != None: # search for the leftest one
                pNode = pNode.left
            return pNode

        # 如果一个节点没有右子树，，并且它还是它父节点的右子节点
        elif pNode.next != None and pNode.next.right == pNode: # next pointer to parent node
            while pNode.next != None and pNode.next.left != pNode # 父节点不是None,并且一直不是父节点的左孩子
                pNode = pNode.next # 往父节点找，直到找到结点是父节点的左孩子
            return pNode.next





