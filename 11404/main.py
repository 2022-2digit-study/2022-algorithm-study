# (BOJ - 11404) 플로이드: https://www.acmicpc.net/problem/11404
import sys

INF = 1000000000


def floyd_marshall(graph: list) -> None:
    n = len(graph)
    for mid in range(n):
        for src in range(n):
            for dst in range(n):
                if src != dst and graph[src][dst] >= (new_weight := graph[src][mid] + graph[mid][dst]):
                    graph[src][dst] = new_weight


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a - 1][b - 1] > c:
        graph[a - 1][b - 1] = c

floyd_marshall(graph)

for cities in graph:
    print(" ".join(map(str, map(lambda x: 0 if x == INF else x, cities))))
