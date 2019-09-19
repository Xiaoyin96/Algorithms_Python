#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
二叉搜索树：中序遍历即为顺序排列
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convert(self, root):
        if not root:
            return None

        if not root.left and not root.right:
            return root

        # 处理左子树, 也按照接下来的连接来连接
        self.convert(root.left)
        left = root.left

        # 连接根与左子树最大结点
        if left:
            while left.right:
                left = left.right # 找到左树最大的子节点
            root.left, left.right = left, root # 左子树的最右孩子与根节点互相连接

        # 处理右子树
        self.convert(root.right)
        right = root.right

        # 连接
        if right:
            while right.left:
                right = right.left
            root.right, right.left = right, root

        while root.left:
            root = root.left # 找到最左边的节点，作为返回的Head Node

        return root



pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

s = Solution()
print(s.convert(pNode1).right.val) # 6
