#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 12:16 AM
# @Author   : Marc
# @File     : permutation_08_07

class PermutationI:
    def permutation(self, S: str) -> list:
        if S == '':
            return []
        res = []
        path = ''
        def backtrack(S, path, res):
            if S == '':
                res.append(path)
                return

            for i in range(len(S)):
                cur = S[i]
                backtrack(S[:i] + S[i+1:], path + cur, res)

        backtrack(S, path, res)

        return res

    def test(self):
        S = 'qew'
        res = self.permutation(S)
        print(res)

if __name__ == "__main__":
    perm  = PermutationI()
    perm.test()