#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
二叉搜索树：按照中序遍历：左根右-->顺序排列的节点
'''

class Solution:
    def VerifyBST(self,sequence):
        if not sequence or len(sequence) <= 0:
            return False

        root = sequence[-1] # 左右根，last one is root
        i = 0

        # 找出左小右大的分界点i,此时i属于右子树
        for node in sequence[:-1]:
            if node > root:
                break
            i += 1

        left = sequence[:i]
        right = sequence[i:-1]

        # 如果在右子树中有比根节点小的值，直接返回False
        for node in right:
            if node < root:
                return False

        # 判断左子树是否为二叉搜索树
        l = r = True
        if len(left) >= 1:
            l = self.VerifyBST(left)
        if len(right) >= 1:
            r = self.VerifyBST(right)

        return l and r

sequence = [7,4,6,5]
sequence1 = [5,7,6,9,11,10,8]
sequence2 = [1]
seq = []
s = Solution()
print(s.VerifyBST(sequence)) # False
print(s.VerifyBST(sequence1)) # True
print(s.VerifyBST(sequence2)) # True
print(s.VerifyBST(seq)) # False