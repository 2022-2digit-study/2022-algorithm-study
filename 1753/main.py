# (BOJ-1753) 최단거리: https://www.acmicpc.net/problem/1753
import heapq
import sys

INF = 100000000
V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
tree_set = [INF] * (V + 1)


class Edge:
    def __init__(self, dst: int, weight: int):
        self.dst = dst
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


for _ in range(E):
    src, dst, weight = map(int, sys.stdin.readline().split())
    graph[src].append(Edge(dst, weight))


def dijkstra(src: int):
    tree_set[src] = 0
    fringe_set = []
    # 초기 노드
    heapq.heappush(fringe_set, Edge(start, 0))

    # fringe_set이 빌 때까지 반복
    while fringe_set:
        min_edge = heapq.heappop(fringe_set)

        for edge in graph[min_edge.dst]:
            # 새로운 가중치가 기존의 가중치보다 작은지 확인
            if (new_min_weight := edge.weight + min_edge.weight) < tree_set[edge.dst]:
                # tree_set에 답 넣기
                tree_set[edge.dst] = new_min_weight
                # 추가된 노드의 갱신된 노드를 fringe_set에 넣기
                heapq.heappush(fringe_set, Edge(edge.dst, new_min_weight))


dijkstra(start)

for weight in tree_set[1:]:
    if weight == INF:
        print("INF")
    else:
        print(weight)
