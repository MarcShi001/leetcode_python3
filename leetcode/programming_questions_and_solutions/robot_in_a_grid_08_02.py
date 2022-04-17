#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/31 17:12
# @Author  : Marc
# @File    : robot_in_a_grid_08_02.py

class RobotinGrid:
    def __init__(self):
        self.__path = []
        self.__can_reach = False

    def pathWithObstacles(self, obstacleGrid: list[list[int]]) -> list[list[int]]:
        x, y = 0, 0
        self.search_path(obstacleGrid, x, y)
        return self.__path

    def search_path(self,  obstacleGrid: list[list[int]], x : int, y : int):
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        if self.__can_reach is False:
            return
        if x == row-1 and y == col -1:
            self.__can_reach = True
            self.__path.append([x, y])
            return
        self.__path.append(x, y)
        if obstacleGrid[x+1][y] == 0:
            self.search_path(obstacleGrid, x+1, y)
        if obstacleGrid[x][y+1] == 0:
            self.search_path(obstacleGrid, x, y+1)
        return