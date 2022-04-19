#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/4/19  10:53 PM
# @Author   : Marc
# @File     : color_fill_08_10

from collections import deque

class ColorFill:
    def floodFill(self, image: list, sr: int, sc: int, newColor: int) -> list:
        #return self.flood_fill_solution1(image, sr, sc, newColor)
        return self.flood_fill_solution2(image, sr, sc, newColor)


    def flood_fill_solution2(self, image: list, sr: int, sc: int, newColor:int) ->list:
        old_color = image[sr][sc]
        if old_color == newColor:
            return image
        q = deque([[sr, sc]])
        row, col = len(image), len(image[0])
        while q:
            x, y = q.popleft()
            image[x][y] = newColor
            for dx, dy in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and image[nx][ny] == old_color:
                    q.append([nx, ny])
        return image



    def flood_fill_solution1(self, image: list, sr: int, sc: int, newColor: int) -> list:
        old_color = image[sr][sc]
        if old_color == newColor:
            return image
        def dfs_fill_color(row: int, col: int, old_color: int, new_color: int):
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != old_color:
                return
            image[row][col] = new_color
            dfs_fill_color(row-1, col, old_color, new_color)
            dfs_fill_color(row+1, col, old_color, new_color)
            dfs_fill_color(row, col-1, old_color, new_color)
            dfs_fill_color(row, col+1, old_color, new_color)
        dfs_fill_color(sr, sc, old_color, newColor)
        return image

    def test(self):
        #image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        #sr = 1
        #sc = 1
        #newColor = 2

        image = [[0, 0, 0], [1, 0, 0]]
        sr = 1
        sc = 0
        newColor = 2
        res = self.floodFill(image, sr, sc, newColor)
        print(res)


if __name__ == "__main__":
        color_test = ColorFill()
        color_test.test()