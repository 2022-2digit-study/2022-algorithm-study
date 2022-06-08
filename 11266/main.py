# (BOJ - 11266) 단절점: https://www.acmicpc.net/problem/11266
import sys
sys.setrecursionlimit(100000)
V, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(V + 1)]
dfs_orders = [0] * (V + 1)
dfs_order = 1
answer = set()
for _ in range(E):
    src, dst = map(int, sys.stdin.readline().split())
    graph[src].append(dst)
    graph[dst].append(src)


def dfs(node, is_root=False):
    global dfs_order
    dfs_orders[node] = dfs_order
    min_order = dfs_orders[node]
    dfs_order += 1
    deg = 0
    for adj_node in graph[node]:
        if dfs_orders[adj_node] > 0:  # 방문한 노드의 경우
            # 자식노드가 갈 수 있는 노드 중 최소 순서를 찾음
            min_order = min(dfs_orders[adj_node], min_order)
            continue
        deg += 1
        # 방문하지 않은 노드의 경우
        result = dfs(adj_node)

        if not is_root and dfs_orders[node] <= result:
            answer.add(node)
        min_order = min(min_order, result)
    if is_root and deg > 1:
        answer.add(node)
    return min_order


for node in range(1, V + 1):
    if dfs_orders[node] == 0:
        dfs(node, True)

answer = list(answer)
answer.sort()

print(len(answer))
for num in answer:
    print(num, end=" ")
print()
