#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/4/20  10:54 AM
# @Author   : Marc
# @File     : bracket_08_09

from collections import deque

class Bracket:
    def generateParenthesis(self, n: int) -> list:
        que = []
        res = []
        path = ''
        self.dfs_bracket(que, n, n, path, res)
        return res

    def dfs_bracket(self, que: list, left: int, right: int, path: str, res: list):
        if left == 0 and right == 0:
            res.append(path)
            return
        # 先放左括号
        if left > 0:
            path = path + '('
            left = left - 1
            que.append('(')
            self.dfs_bracket(que, left, right, path, res)
            que.pop()
            left = left + 1
            str_len = len(path)
            path = path[:str_len-1]

        #后放右括号
        if right > 0 and len(que) > 0 and que[-1] == '(':
            que.pop()
            path = path + ')'
            right = right - 1
            self.dfs_bracket(que, left, right, path, res)
            right = right + 1
            str_len = len(path)
            path = path[:str_len-1]
            que.append('(')
        return

    def test(self):
        n = 3
        res = self.generateParenthesis(n)
        print(res)


if __name__ == "__main__":
    backet_test = Bracket()
    backet_test.test()
