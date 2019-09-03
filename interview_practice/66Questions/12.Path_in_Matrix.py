#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''

'''
给定一个字母构成的矩阵，判断是否有某一条路径，路径不能重复
回朔法： 如果这一步不可行，退回上一步。
'''



def find_path(matrix, string):
    rows = len(matrix)
    cols = len(matrix[0])

    visited = [[False] * cols for _ in range(rows)] # same size as matrix

    for i in range(rows):
        for j in range(cols):
            # 遍历寻找第一个字符
            if matrix[i][j] == string[0]:
                visited[i][j] = True
                found = find_next(matrix, string[1:],visited, (i,j))
                if found:
                    for r in visited:
                        print(r)
                    return True
                visited[i][j] = False
    return False


#%%
def find_next(matrix, string, visited, matrix_indices):
    if len(string) <= 0:
        return True
    # current position
    x, y = matrix_indices
    indices = []
    # 找到合法的上下左右坐标
    for shift in (-1, 1):
        if 0 <= x + shift < len(matrix) and not visited[x + shift][y]:
            indices.append((x + shift, y))

        if 0 <= y + shift < len(matrix[0]) and not visited[x][y + shift]:
            indices.append((x, y + shift))
    # 对比合法位置的string是否match,递归
    for x_next, y_next in indices:
        if matrix[x_next][y_next] == string[0]:
            visited[x_next][y_next] = True
            found = find_next(matrix, string[1:], visited, (x_next, y_next))
            if found:
                return True
            visited[x_next][y_next] = False
    return False

#%%
matrix = [
        ["a", "b", "t", "g"],
        ["c", "f", "c", "s"],
        ["j", "d", "e", "h"]
    ]
string = "bfce"
print(find_path(matrix=matrix, string=string))