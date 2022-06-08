# 백준 - https://www.acmicpc.net/problem/11438

import sys

sys.setrecursionlimit(100000)


def dfs(x, depth):
    visited[x] = True
    depth_list[x] = depth
    for y in tree[x]:
        if visited[y]:
            continue
        parent[y][0] = x
        dfs(y, depth + 1)


def set_parent():
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, N + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]


def lca(a, b):
    if depth_list[a] > depth_list[b]:
        a, b = b, a

    for i in range(LOG - 1, -1, -1):
        if depth_list[b] - depth_list[a] >= (1 << i):
            b = parent[b][i]

    if a == b:
        return a

    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]


N = int(sys.stdin.readline())

LOG = 21
tree = [[] for _ in range(N + 1)]
parent = [[0] * LOG for _ in range(N + 1)]
depth_list = [0] * (N + 1)
visited = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

set_parent()

M = int(sys.stdin.readline())

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(lca(a, b))