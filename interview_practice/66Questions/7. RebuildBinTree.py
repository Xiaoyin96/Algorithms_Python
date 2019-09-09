#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
leetcode 105: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
'''

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rebuild(self, preorder, inorder):
        if not preorder and not inorder:
            return None
        if set(preorder) != set(inorder):
            return None

        root = Node(preorder[0])
        pos = inorder.index(preorder[0])
        root.left = self.rebuild(preorder[1:pos+1], inorder[:pos])
        root.right = self.rebuild(preorder[pos+1:], inorder[pos+1:])

        return root
