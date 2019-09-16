#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
叶节点：没有孩子
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def find_path(self, root, num):
        if not root:
            return None
        result = []


        def core(root, path, cur):
            cur += root.val
            path.append(root)

            # 判断是否到达叶节点
            flag = (root.left == None and root.right == None)

            if flag and cur == num:
                onepath = []
                for node in path:
                    onepath.append(node.val)
                result.append(onepath)

            if cur < num:
                if root.left:
                    core(root.left, path, cur)
                if root.right:
                    core(root.right, path, cur)
            path.pop() # pop is to delete this visited path

        core(root, [], 0)
        return result

    # def find_path2(self, root, num):
    #     if not root:
    #         return None
    #
    #     if root.right == None and root.left == None: # 叶节点
    #         if root.val == num:
    #             return [[root.val]]
    #         else:
    #             return []
    #
    #     a = self.find_path2(root.left, num - root.val) + self.find_path2(root.right, num - root.val) # 返回的是最后的一个叶节点
    #     return [[root.val] + i for i in a]



pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)
pNode6 = TreeNode(3)


pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode4.left = pNode6


S = Solution()
print(S.find_path(pNode1, 22))