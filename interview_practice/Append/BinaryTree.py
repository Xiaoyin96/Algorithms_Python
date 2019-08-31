#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
Binary tree

        1
      3   2
    7  6 5  4
   0

'''

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))

#%% 层次遍历 level-order traversal, from left to right, level by level, BFS
'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
'''

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
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
        next_node = []
        total_list.append(val_list)

    return total_list

print(levelOrder(tree)) # [[1], [3, 2], [7, 6, 5, 4], [0]]

#%% 深度遍历 DFS
def dfs(root):
    if root is not None:
        print(root.val)
        dfs(root.left)
        dfs(root.right)

print(dfs(tree))  # 1, 3, 7, 0, 6, 2, 5, 4

#%% 先序遍历: 根，左， 右
def preorder(root):
    if root is not None:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

print(preorder(tree)) # 1, 3, 7, 0, 6, 2, 5, 4, same as deep first traversal

#%% 中序遍历： 左， 根， 右
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

print(inorder(tree)) # 0, 7, 3, 6, 1, 5, 2, 4

#%% 后序遍历：左，右， 根
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

print(postorder(tree)) # 0, 7, 6, 3, 5, 4, 2, 1

#%% 最大深度
def maxdepth(root):
    if not root:
        return 0
    return max(maxdepth(root.left), maxdepth(root.right)) + 1

print(maxdepth(tree)) # depth = 4

#%% 求两棵树是否相同
def isSameTree(pTree, qTree):
    if pTree == None and qTree == None:
        return True
    elif pTree and qTree:
        return pTree.val == qTree.val and isSameTree(pTree.left, qTree.left) and isSameTree(pTree.right, qTree.right)
    else:
        return False

pTree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
qTree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5)))
print(isSameTree(pTree, qTree))

#%% 已知前序中序求后序
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rebuild(pre, center):
    if not pre:
        return
    root = Node(pre[0])
    pos = center.index(pre[0])
    root.left = rebuild(pre[1:pos+1],center[:pos])
    root.right = rebuild(pre[pos+1:], center[pos+1:])
    return root

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

pre = [1, 3, 7, 0, 6, 2, 5, 4]
center = [0, 7, 3, 6, 1, 5, 2, 4]
root = rebuild(pre, center)
print(postorder(root)) # 0, 7, 6, 3, 5, 4, 2, 1

#%% 反转二叉树
def reverse(root):
    if root is not None:
        root.left, root.right = root.right, root.left
        reverse(root.left)
        reverse(root.right)
    return root

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
root = reverse(tree)
print(preorder(root)) # 1, 2, 4, 5, 3, 6, 7, 0

