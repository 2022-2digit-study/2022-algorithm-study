# (BOJ-1922) 네트워크 연결: https://www.acmicpc.net/problem/1922

import sys


class Edge:
    def __init__(self, src, dst, cost):
        self.src = src
        self.dst = dst
        self.cost = cost

    def __lt__(self, edge):
        return self.cost < edge.cost


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, elem, with_initialize: bool = False):
        if self.parent[elem] == elem:
            return elem
        elem_parent = self.find(self.parent[elem])
        if with_initialize:
            self.parent[elem] = elem_parent
        return elem_parent

    def union(self, elem1, elem2):
        elem1_parent = self.find(elem1, True)
        elem2_parent = self.find(elem2, True)
        if elem1_parent > elem2_parent:
            self.parent[elem1_parent] = elem2_parent
        elif elem1_parent < elem2_parent:
            self.parent[elem2_parent] = elem1_parent


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 1. 모든 노드를 트리로 만들기
uf = UnionFind(N + 1)

# 2. 정점을 연결하는 간선을 비용 기준으로 오름차순 정렬하기
edges = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append(Edge(a, b, c))
edges.sort()

answer = 0

# 3. 적은 비용을 가진 간선 순으로 간선을 연결하는 노드를 기준으로 트리를 합침
for edge in edges:
    if uf.find(edge.src) != uf.find(edge.dst):
        uf.union(edge.src, edge.dst)
        answer += edge.cost
    # 3-1: 사이클이 발생할 경우 해당 간선을 버린다.
    else:
        continue
print(answer)
