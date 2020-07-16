#!/usr/bin/python3

__author__ = "yang.dd"

"""
    example 0534
    ^ 运算符 转为二进制 按补码计算 相同，为0，不同，为1
    0000 0010
    0000 0011
    ——————————
    0000 0001
"""

print(' 2 ^ 3  = %d' % (2 ^ 3))    # 0000 0010 ^ 0000 0011
print(' 2 ^ -3  = %d' % (2 ^ -3))  # 0000 0010 ^ 1111 1101
print(' -2 ^ 3  = %d' % (-2 ^ 3))  # 1111 1110 ^ 0000 0011



