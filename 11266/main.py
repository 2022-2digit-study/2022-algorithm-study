# (BOJ - 11266) 단절점: https://www.acmicpc.net/problem/11266
import sys

sys.setrecursionlimit(100000)
V, E = map(int, sys.stdin.readline().split())

# Target Graph
graph = [[] for _ in range(V + 1)]

# DFS Spanning Tree
dfs_orders = [0] * (V + 1)

# 방문 순서를 저장할 변수
dfs_order = 1

# 단절점 집합(중복 제거용)
answer = set()


# 그래프 초기화 함수
def init(graph, edge_num):
    for _ in range(edge_num):
        src, dst = map(int, sys.stdin.readline().split())
        graph[src].append(dst)
        graph[dst].append(src)


# DFS 함수
def dfs(node, is_root=False):
    global dfs_order
    dfs_orders[node] = dfs_order  # Spanning Tree 생성
    min_order = dfs_orders[node]  # 자손 노드 중 가장 빠른 순서가 담김
    dfs_order += 1
    deg = 0  # 방문하지 않은 노드의 차수 (루트 구분용)

    for adj_node in graph[node]:
        if dfs_orders[adj_node] > 0:  # 방문한 노드의 경우
            # 자식노드가 갈 수 있는 노드 중 최소 순서를 저장만 함
            min_order = min(dfs_orders[adj_node], min_order)
            continue

        # 방문하지 않은 노드의 경우
        deg += 1
        # 자손 노드가 갈 수 있는 가장 빠른 순서를 찾아 저장
        result = dfs(adj_node)

        # 루트 노드가 아니면서 자손 노드 중 node의 순서보다 더 빠른 순서를 가진 노드가 없는 경우
        if not is_root and dfs_orders[node] <= result:
            # 단절점 추가
            answer.add(node)
        # 최소 노드에는 가장 방문 순서가 빠른 노드의 순서를 저장
        min_order = min(min_order, result)

    # 루트이면서 방문하지 않은 루트의 차수가 2이상인 경우 단절점
    if is_root and deg > 1:
        answer.add(node)
    return min_order


# 그래프 초기화
init(graph, E)

# 단절점 찾기
for node in range(1, V + 1):
    if dfs_orders[node] == 0:
        dfs(node, True)

answer = list(answer)
answer.sort()

print(len(answer))
print(" ".join(map(str, answer)))
