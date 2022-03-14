#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 19:45
# @Author  : Marc
# @File    : set_zeroes_01_08.py

class SetZeroes0108:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        row_flag, col_flag = [False] * row, [False] * col
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_flag[i] = True
                    col_flag[j] = True
        for i in range(row):
            for j in range(col):
                if row_flag[i] or col_flag[j]:
                    matrix[i][j] = 0

    def setZeroes2(self, matrix: list[list[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        row_set = set()
        column_set = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    column_set.add(j)
        for i in row_set:
            for j in range(col):
                matrix[i][j] = 0
        for j in column_set:
            for i in range(row):
                matrix[i][j] = 0
        return

