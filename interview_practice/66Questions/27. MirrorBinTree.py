#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
二叉树的镜像定义：源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9  11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7   5
'''
#%% recursion / queue
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirror(self, pRoot): # in-place
        if not pRoot:
            return None

        if not pRoot.left and not pRoot.right:
            return pRoot

        pTemp = pRoot.left
        pRoot.left = pRoot.right
        pRoot.right = pTemp

        if pRoot.left:
            self.mirror(pRoot.left)
        if pRoot.right:
            self.mirror(pRoot.right)

    def mirror_bfs(self, pRoot):
        ret = []
        queue = deque([pRoot])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.right)
                queue.append(node.left)
        return ret

    def preorder(self, pRoot):
        if pRoot is not None:
            print(pRoot.val)
            self.preorder(pRoot.left)
            self.preorder(pRoot.right)



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

S = Solution()
S.preorder(pNode1) # 8,6,5,7,10,9,11
S.mirror(pNode1)
print('--'*10, 'mirror')
S.preorder(pNode1) # 8,10,11,9,6,7,5



