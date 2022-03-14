#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 19:11
# @Author  : Marc
# @File    : rotate_01_07.py


class Rotate_01_07:

    def rotate(self, matrix: list[list[int]]) -> None:
        i, j = 0, 0
        n = len(matrix)
        # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
        matrix_new = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                matrix_new[j][n-i-1] = matrix[i][j]
        matrix[:] = matrix_new


    def rotate_2(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range (n//2):
            for j in range(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
