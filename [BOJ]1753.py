# 백준 - https://www.acmicpc.net/problem/1753

import sys
import math
import heapq

INF = math.inf


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for vertex, weight in graph[now]:

            if (cost := dist + weight) < distance[vertex]:
                distance[vertex] = cost
                heapq.heappush(queue, (cost, vertex))


V, E = map(int, sys.stdin.readline().strip().split())
start = int(sys.stdin.readline().strip())

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, w))

dijkstra(start)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])