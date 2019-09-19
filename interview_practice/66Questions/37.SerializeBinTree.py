#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
请实现两个函数，分别用来序列化和反序列化二叉树
二叉树的序列化就是采用前序遍历二叉树输出节点，再碰到左子节点或者右子节点为None的时候输出一个特殊字符”#”。
反序列化，就是针对输入的一个序列构建一棵二叉树
我们可以设置一个指针先指向序列的最开始，然后把指针指向位置的数字转化为二叉树的结点，后移一个数字，继续转化为左子树和右子树。
当遇到当前指向的字符为特殊字符”#”或者指针超出了序列的长度，则返回None，指针后移，继续遍历。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def serialize(self, root): # 前序遍历：根左右
        if not root:
            return '#'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, s):

        list = s.split(',')
        return self.core(list)

    def core(self, list):
        if len(list) <= 0:
            return None

        val = list.pop(0)
        root = None # '#'默认是None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.core(list)
            root.right = self.core(list)

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
sq = s.serialize(pNode1) # S: 8,6,5,#,#,7,#,#,10,9,#,#,11,#,#
tree = s.deserialize(sq)
print(s.serialize(tree)) # S: 8,6,5,#,#,7,#,#,10,9,#,#,11,#,#