#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
不分行从上到下打印二叉树, 同一层按从左到右的顺序 (level order travesal)
'''
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_print(self, root): # 不分行打印
        if not root:
            return None

        node_list = []
        val = []
        node_list.append(root)
        while node_list:
            node = node_list.pop(0) # left pop
            val.append(node.val)
            if node.left:
                node_list.append(node.left)
            if node.right:
                node_list.append(node.right)

        return val

    def level_row_print(self, root): # 分行打印
        if not root:
            return []
        cur_node = [root]
        next_node = []
        total_list = []
        while cur_node or next_node:
            val_list = []
            for node in cur_node:
                if node:
                    val_list.append(node.val)
                    if node.left:
                        next_node.append(node.left)
                    if node.right:
                        next_node.append(node.right)
            cur_node = next_node
            next_node = [] # 每次清空，保证分行输出
            total_list.append(val_list)

        return total_list

    def z_print(self, root): # Z字形按行打印
        if not root:
            return []
        res = []
        nodes = [root]
        leftToRight = True

        while nodes:
            curStack, nextStack = [], []
            for node in nodes:
                curStack.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            if not leftToRight:
                curStack.reverse()
            res.append(curStack)
            leftToRight = not leftToRight
            nodes = nextStack

        return res



tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
'''
        1
      3   2
    7  6 5  4
   0
   '''
s = Solution()
print(s.level_print(tree)) # [1, 3, 2, 7, 6, 5, 4, 0]
print(s.level_row_print(tree)) # [[1], [3, 2], [7, 6, 5, 4], [0]]
print(s.z_print(tree)) # [[1], [2, 3], [7, 6, 5, 4], [0]]
