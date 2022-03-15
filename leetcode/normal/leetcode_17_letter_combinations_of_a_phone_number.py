#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 9:34
# @Author  : Marc
# @File    : leetcode_17_letter_combinations_of_a_phone_number.py

class LetterCombinationsOfAPhoneNumber:
    def __init__(self):
        self.num_to_char_map = {'2': ['a', 'b', 'c'], \
                           '3': ['d', 'e', 'f'], \
                            '4': ['g', 'h', 'i'], \
                           '5': ['j', 'k', 'l'], \
                           '6': ['m', 'n', 'o'], \
                           '7': ['p', 'q', 'r', 's'], \
                           '8': ['t', 'u', 'v'], \
                           '9': ['w', 'x', 'y', 'z']}
        self.result = []
        self.len_digits = 0

    def letterCombinations(self, digits: str) :
        '''
        #递归实现
        size = len(digits)
        if size == 0:
            return self.result
        self.len_digits = size
        self.dfs_letter_combinations(digits, 0, "")
        return self.result
        '''
        #循环实现
        num_to_char_map = {'2':'abc' , '3':'def' , '4':'ghi' , '5':'jkl' , '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if not digits:
            return []
        res = ['']
        for digit_char in digits:
            len_res = len(res)
            for n in range(len_res):
                temp = res.pop(0)
                for ch in num_to_char_map[digit_char]:
                    res.append(''.join([temp, ch]))
        return res

    def dfs_letter_combinations(self, digits: str, index: int, curr: str):
        if index == self.len_digits:
            self.result.append(curr)
            return
        curr_chars = self.num_to_char_map[digits[index]]
        for ch in curr_chars:
            self.dfs_letter_combinations(digits, index+1, curr+ch)

def main():
    test = LetterCombinationsOfAPhoneNumber()
    digits = "23"
    res = test.letterCombinations(digits)
    for digits_to_str in res:
        print(digits_to_str)

if __name__ == "__main__":
    main()
