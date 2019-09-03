#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaoyin
'''
'''
类似12，加上位置数位之和 < threshold,
问机器人能到达多少格子？
回朔法
'''
import sys
sys.setrecursionlimit(15000)

def sum_digit(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

def check(matrix, threshold, visited, matrix_indices):
    x, y = matrix_indices
    if not (0 <= x < len(matrix)) or not (0 <= y < len(matrix[0])) or \
            (sum_digit(x) + sum_digit(y) > threshold) or \
            visited[x][y]:
        return False
    return True

def moving_count(matrix, threshold):
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not isinstance(matrix[0], list) or len(matrix[0]) == 0:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    for r in matrix:
        if len(r) != cols:
            return False

    visited = [[False] * cols for _ in range(rows)] # same size as matrix
    count = count_recursively(matrix, threshold, (0, 0), visited)
    return count

def count_recursively(matrix, threshold, matrix_indices, visited):
    count = 0
    x, y = matrix_indices
    if check(matrix, threshold, visited, matrix_indices):
        count = count + count_recursively(matrix, threshold, (x + 1, y), visited) + \
            count_recursively(matrix, threshold, (x - 1, y), visited) + \
            count_recursively(matrix, threshold, (x, y + 1), visited) + \
            count_recursively(matrix, threshold, (x, y - 1), visited)
    return count

matrix = [[1] * 5 for _ in range(5)]
threshold = 5
print(moving_count(matrix=matrix, threshold=threshold))