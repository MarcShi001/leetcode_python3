#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/31 16:39
# @Author  : Marc
# @File    : draw_line_05_08.py


class DarwLine:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> list[int]:
        ans = [0] * length
        start = y * w // 32 + (x1 // 32)
        end = y * w // 32 + (x2 // 32)

        # 中间肯定都为0xffffffff，所以直接置为-1
        for i in range(start+1, end):
            ans[i] = -1
        # 开始和结束端点分别处理
        ans[start] = 0xffffffff >> (x1%32)
        temp_end = 0xffffffff << (31 - (x2 % 32)) & 0xffffffff
        ans[end] = temp_end & ans[start] if start == end else temp_end

        # 求补码
        for i in [start, end]:
            if ans[i] & 0x80000000 == 0x80000000:
                ans[i] = -((ans[i] ^ 0xffffffff) + 1)

        return ans