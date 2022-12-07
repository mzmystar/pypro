# -*- coding: UTF-8 -*-
# 将一个数拆分成N个数，且数字不重复，共有几种方法？
n, k = map(int, input().split())


def divide(n, m):
    if m <= 1 or n <= 1:
        return 1
    if n < m:
        return divide(n, n)
    return divide(n, m-1) + divide(n-m, m)


print(divide(n - k, k))
