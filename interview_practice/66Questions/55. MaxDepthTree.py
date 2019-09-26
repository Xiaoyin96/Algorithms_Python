#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def MaxDepth(self, root):
        if not root:
            return 0

        left = self.MaxDepth(root.left)
        right = self.MaxDepth(root.right)
        return max(left, right) + 1

Node1 = TreeNode(2)
Node2 = TreeNode(3)
Node3 = TreeNode(4)
Node4 = TreeNode(5)
Node5 = TreeNode(6)
Node6 = TreeNode(7)
Node7 = TreeNode(8)

Node4.left = Node2
Node4.right = Node6
Node2.left = Node1
Node2.right = Node3
Node6.left = Node5
Node6.right = Node7

s = Solution()
print(s.MaxDepth(Node4)) # 3

#%%
'''平衡二叉树'''
