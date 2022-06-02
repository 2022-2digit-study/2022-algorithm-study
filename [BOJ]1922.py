# 백준 - https://www.acmicpc.net/problem/1922

import sys
import heapq


def Prim():
    answer = 0
    queue = []
    heapq.heappush(queue, (0, 1))

    while queue:
        cost, now = heapq.heappop(queue)
        if visited[now] == False:
            visited[now] = True
            answer += cost
            for next_cost, next_node in graph[now]:
                heapq.heappush(queue, (next_cost, next_node))
    return answer


N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

print(Prim())
