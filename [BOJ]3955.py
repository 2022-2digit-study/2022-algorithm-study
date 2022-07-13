# 백준 - https://www.acmicpc.net/problem/3955

import sys


def extended_euclidean(a, b):
    K = a
    x_1, y_1 = 1, 0
    x_2, y_2 = 0, 1
    while b != 0:
        mok, na = divmod(a, b)
        a, b = b, na
        x, y = x_1 - (x_2 * mok), y_1 - (y_2 * mok)
        x_1, y_1 = x_2, y_2
        x_2, y_2 = x, y
    if y_1 < 0:
        y_1 += K
    if a != 1 or y_1 > 10 ** 9:
        return "IMPOSSIBLE"
    return y_1


t = int(input())

for _ in range(t):
    K, C = list(map(int, sys.stdin.readline().split()))

    if C == 1:
        print("IMPOSSIBLE" if K + 1 > 10 ** 9 else K + 1)
        continue

    if K == 1:
        print(1)
        continue

    print(extended_euclidean(K, C))
