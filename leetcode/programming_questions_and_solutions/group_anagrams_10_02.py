#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/4/21  11:38 AM
# @Author   : Marc
# @File     : group_anagrams_10_02

class GroupAnagrams:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        self.group_angrams_solution1(strs)


    def group_angrams_solution1(self,strs: list[str]) -> list[list[str]]:
        pr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        tmp_dict = {}
        for tmp_str in strs:
            key = 1
            for ch in tmp_str:
                key = key * pr[ord(ch) - 97]
            if key in tmp_dict:
                tmp_dict[key].append(tmp_str)
            else:
                tmp_dict[key] = [tmp_str]
        return list(tmp_dict.values())

    def group_angrams_solution2(self,strs: list[str]) -> list[list[str]]:
        res_dict = {}
        for tmp_str in strs:
            sorted_str = sorted(tmp_str)
            tuple_sorted_str = tuple(sorted_str)
            if tuple_sorted_str in res_dict:
                res_dict[tuple_sorted_str].append(tmp_str)
            else:
                res_dict[tuple_sorted_str] = [tmp_str]
        return list(res_dict.values())

