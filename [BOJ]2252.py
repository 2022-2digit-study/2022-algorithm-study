# 백준 - https://www.acmicpc.net/problem/2252

import sys

N, M = map(int, sys.stdin.readline().split())

answer = []
graph = [[] for _ in range(N + 1)]
inDegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    inDegree[b] += 1

queue = [node for node, degree in enumerate(inDegree) if node != 0 and degree == 0]

while queue:
    node = queue.pop(0)
    answer.append(str(node))

    for i in graph[node]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)

print(' '.join(answer))
