# 백준 - https://www.acmicpc.net/problem/1735

import sys


def euclidean_algorithm(num1, num2):
    min_num = min(num1, num2)
    max_num = max(num1, num2)
    while True:
        mok, na = divmod(max_num, min_num)
        if na == 0:
            break
        max_num, min_num = min_num, na
    return min_num


frac1 = list(map(int, sys.stdin.readline().split()))
frac2 = list(map(int, sys.stdin.readline().split()))
frac3 = (frac1[0] * frac2[1] + frac1[1] * frac2[0], frac1[1] * frac2[1])
gcd = max(euclidean_algorithm(frac3[0], frac3[1]), 1)
print(frac3[0] // gcd, frac3[1] // gcd)
