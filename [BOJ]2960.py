# 백준 - https://www.acmicpc.net/problem/2960

import sys


def eratos(integer_list, N, K):
    del_list = []
    for integer in integer_list:
        for num in range(integer, N + 1, integer):
            if num not in del_list:
                del_list.append(num)
        if len(del_list) >= K:
            break
    return del_list[K-1]


N, K = map(int, sys.stdin.readline().split())
integer_list = [i for i in range(2, N + 1)]

print(eratos(integer_list, N, K))
