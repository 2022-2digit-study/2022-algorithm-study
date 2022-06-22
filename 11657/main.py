# (BOJ - 11657) 타임머신: https://www.acmicpc.net/problem/11657
import sys

INF = 1000000000 # 무한대
V, E = map(int, sys.stdin.readline().split())
costs = [0] + [INF] * (V - 1)  # 시작 노드를 제외한 나머지 노드를 무한대로 초기화
edges = [] # 간선 정보가 보관될 리스트


class Edge:
    def __init__(self, src, dst, weight):
        self.src = src - 1  # 시작
        self.dst = dst - 1  # 도착
        self.weight = weight  # 가중치


for _ in range(E):
    src, dst, weight = map(int, sys.stdin.readline().split())
    edges.append(Edge(src, dst, weight))


def bellman_ford():
    for i in range(V):
        for j in range(E):
            if costs[edges[j].src] != INF and costs[edges[j].dst] > (new_weight := costs[edges[j].src] + edges[j].weight):
                costs[edges[j].dst] = new_weight
                if i == V - 1:
                    return True
    return False


if bellman_ford():
    print(-1)
else:
    for i in range(1, V):
        if (cost := costs[i]) != INF:
            print(cost)
        else:
            print(-1)
