#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
给定一颗二叉搜索树，请找出其中的第k小的结点。
中序遍历，再查找
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthNode(self, root, k): # 左根右
        if not root or k <= 0:
            return []

        res = []
        self.inorder(root, res) # res change in-place
        if len(res) >= k:
            return res[k-1]
        else:
            return None

    def inorder(self, root, res):
        if not root:
            return []

        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)


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
print(s.kthNode(Node4,3)) # 4
