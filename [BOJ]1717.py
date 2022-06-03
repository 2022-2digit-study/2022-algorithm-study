# 백준 - https://www.acmicpc.net/problem/1717

import sys

limit_number = 10000
sys.setrecursionlimit(limit_number)


def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    p_a = find(a)
    p_b = find(b)

    if p_a != p_b:
        parents[p_b] = p_a


N, M = map(int, sys.stdin.readline().split())
parents = [i for i in range(N + 1)]

for _ in range(M):
    command, a, b = map(int, sys.stdin.readline().split())
    if command == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
