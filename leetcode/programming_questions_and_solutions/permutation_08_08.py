#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 9:59 PM
# @Author   : Marc
# @File     : permutation_08_08

class Permutation_II:
    def permutation(self, S: str) -> list[str]:
        res = []
        path = ''
        list_str = list(S)
        list_str.sort()
        S = ''.join(list_str)
        def back_track(S, path: str, res: list):
            if S == '':
                res.append(path)
                return
            for i in range(len(S)):
                if i > 0:
                    if S[i] == S[i-1]:
                        continue
                current = S[i]
                back_track(S[:i] + S[i+1:], path+current, res)
        back_track(S, path, res)
        return res