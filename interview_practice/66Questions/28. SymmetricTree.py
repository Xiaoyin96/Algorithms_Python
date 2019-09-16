#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的
先序遍历：根，左，右，反向先序遍历：根，右，左，如果两次遍历结果一样的话就是对称的
注意，我们必须把遍历二叉树时遇到的空指针考虑进来。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, pRoot):
        return self.core(pRoot, pRoot)

    def core(self, pRoot1, pRoot2):
        if not pRoot1 and not pRoot2: # both None
            return True

        if not pRoot1 or not pRoot2:
            return False

        if pRoot1.val != pRoot2.val:
            return False

        return self.core(pRoot1.left, pRoot2.right) and self.core(pRoot1.right, pRoot2.left)

pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(6)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(5)
pNode7 = TreeNode(4)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

s = Solution()
print(s.isSymmetric(pNode1))

