# (BOJ - 11438) LCA 2: https://www.acmicpc.net/problem/11438

import sys


def dfs(node: int, d: int):
    # 깊이 설정 (현재노드)
    depth[node] = d
    visited[node] = True
    # 자식 노드의 부모 설정
    for adj_node in graph[node]:
        if not visited[adj_node]:
            parent[adj_node][0] = node
            dfs(adj_node, d + 1)


def set_parent():
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, N + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]


def lca(node_1, node_2):
    # 노드의 깊이는 1번이 더 작게 설정
    if depth[node_1] > depth[node_2]:
        node_1, node_2 = node_2, node_1

    # 두 노드의 depth 맞추기
    for i in range(LOG - 1, -1, -1):
        if depth[node_2] - depth[node_1] >= 2 ** i:
            node_2 = parent[node_2][i]

    if node_1 == node_2:
        return node_1

    for i in range(LOG - 1, -1, -1):
        if parent[node_1][i] != parent[node_2][i]:
            node_1 = parent[node_1][i]
            node_2 = parent[node_2][i]

    return parent[node_1][0]


LOG = 21
N = int(sys.stdin.readline())
depth = [0] * (N + 1)
parent = [[0] * LOG for _ in range(N + 1)]
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

set_parent()

M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(lca(a, b))
