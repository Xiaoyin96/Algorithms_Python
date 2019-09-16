#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入两棵二叉树A和B，判断B是不是A的子结构。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasSubTree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1HasTree2(pRoot1, pRoot2)
            if not result:
                result = self.hasSubTree(pRoot1.left, pRoot2)
            if not result:
                result = self.hasSubTree(pRoot1.right, pRoot2)

        return result

    def DoesTree1HasTree2(self, pRoot1, pRoot2):
        if not pRoot2: # recursion的break condition!! 顺序很重要，要先return True
            return True

        if not pRoot1:
            return False


        if pRoot1.val != pRoot2.val:
            return False

        return self.DoesTree1HasTree2(pRoot1.left, pRoot2.left) and self.DoesTree1HasTree2(pRoot1.right, pRoot2.right)

pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

pRoot8 = TreeNode(8)
pRoot9 = TreeNode(9)
pRoot10 = TreeNode(2)
pRoot8.left = pRoot9
pRoot8.right = pRoot10

S = Solution()
print(S.hasSubTree(pRoot1, pRoot8))
