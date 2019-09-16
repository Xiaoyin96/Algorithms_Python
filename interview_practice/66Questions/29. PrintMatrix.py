#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
从外到里顺时针打印矩阵数字
'''

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

class solution:
    def print_matrix(self, matrix):
        cols = len(matrix[0])
        rows = len(matrix)

        if not matrix or cols <= 0 or rows <= 0:
            return None

        cnt = 0
        while cols > cnt*2 and rows > cnt*2:  # 可以打印的条件
            self.print_incircle(matrix, cols, rows, cnt)
            cnt += 1

    def print_incircle(self, matrix, cols, rows, cnt):
        endX = cols - 1 - cnt
        endY = rows - 1 - cnt

        # 从左到右打印一行
        for i in range(cnt, endX+1):
            print(matrix[cnt][i])

        # 从上到下打印一列
        if cnt < endY:
            for i in range(cnt + 1, endY + 1):
                print(matrix[i][endX])

            # 从右到左打印一行
        if cnt < endX and cnt < endY:
            for i in range(endX - 1, cnt - 1, -1):
                print(matrix[endY][i])

            # 从下到上打印一列
        if cnt < endX and cnt < endY - 1:
            for i in range(endY - 1, cnt, -1):
                print(matrix[i][cnt])

    def print2(self, matrix): #  python magic
        return matrix and [*matrix.pop(0)] + self.print2([*zip(*matrix)][::-1]) # 转置
    # and: matrix为空的时候不再pop
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], pop: [1,2,3,4]
    # matrix = [(8, 12, 16), (7, 11, 15), (6, 10, 14), (5, 9, 13)], pop: [8,12,16]
    # matrix = [(15, 14, 13), (11, 10, 9), (7, 6, 5)], pop: [15, 14, 13]
    # matrix = [(9, 5), (10, 6), (11, 7)], pop: [9,5]
    # matrix = [(6, 7), (10, 11)], pop: [6,7]
    # matrix = [(11,), (10,)], pop: [11]
    # matrix = [(10,)], pop: [10]


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
s = solution()
s.print_matrix(matrix)
print(s.print2(matrix))