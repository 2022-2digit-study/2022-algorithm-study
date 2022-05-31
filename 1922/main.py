# (BOJ-1922) 네트워크 연결: https://www.acmicpc.net/problem/1922

import sys


class Edge:
    def __init__(self, src, dst, cost):
        self.src = src
        self.dst = dst
        self.cost = cost

    def __lt__(self, edge):
        return self.cost < edge.cost

    def __lte__(self, edge):
        return self.cost <= edge.cost

    def __gt__(self, edge):
        return self.cost > edge.cost

    def __gte__(self, edge):
        return self.cost >= edge.cost

    def __eq__(self, edge):
        return self.cost == edge.cost


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

uf = UnionFind(N + 1)

edges = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append(Edge(a, b, c))
edges.sort()

answer = 0

for edge in edges:
    if uf.find(edge.src) != uf.find(edge.dst):
        uf.union(edge.src, edge.dst)
        answer += edge.cost

print(answer)
