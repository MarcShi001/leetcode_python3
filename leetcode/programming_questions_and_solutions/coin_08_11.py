#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2022/4/20  9:41 AM
# @Author   : Marc
# @File     : coin_08_11


class Coin:
    def waysToChange(self, n: int) -> int:
        coins = [1, 5, 10, 25]
        res = [0] * (n+1)
        res[0] = 1
        for coin in coins:
            for i in range(coin, n+1):
                res[i] = res[i] + res[i-coin]
        return res[n] % 1000000007