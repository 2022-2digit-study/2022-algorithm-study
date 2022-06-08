# 백준 - https://www.acmicpc.net/problem/11266

import sys

sys.setrecursionlimit(100000)


def DFS(curr_node, is_root):
    global node_cnt
    node_cnt += 1
    discover[curr_node] = node_cnt

    node_disc = discover[curr_node]
    child = 0

    for next_node in graph[curr_node]:
        if discover[next_node] == 0:
            child += 1

            min_disc = DFS(next_node, 0)

            if not is_root and min_disc >= discover[curr_node]:
                cut[curr_node] = 1

            node_disc = min(node_disc, min_disc)

        else:
            node_disc = min(node_disc, discover[next_node])

    if is_root and child > 1:
        cut[curr_node] = 1

    return node_disc


V, E = map(int, sys.stdin.readline().split())

node_cnt = 0
graph = [[] for _ in range(V + 1)]
discover = [0 for _ in range(V + 1)]
cut = [0 for _ in range(V + 1)]

for _ in range(E):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

for v in range(1, V + 1):
    if discover[v] == 0:
        DFS(v, 1)

print(sum(cut))

for v in range(1, V + 1):
    if cut[v] == 1:
        print(v, end=' ')
