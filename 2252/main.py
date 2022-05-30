# (BOJ - 2252) 줄 세우기 - https://www.acmicpc.net/problem/2252
import sys

N, M = map(int, sys.stdin.readline().split())
adjacent_nodes = [list() for _ in range(N + 1)]
in_degree = [0] * (N + 1)
result = list()
queue = list()

# 초기화
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    adjacent_nodes[A].append(B)
    in_degree[B] += 1

# 초기 큐 형성: 진입차수 0
for student_i in range(1, N+1):
    if in_degree[student_i] == 0:
        queue.append(student_i)

# 노답인경우
for i in range(N):
    if not queue:
        print("답 없음")
        break
    # 유답인 경우
    front = queue[0]
    queue.pop(0)
    result.append(front)

    for j in range(len(adjacent_nodes[front])):
        y = adjacent_nodes[front][j]
        in_degree[y] -= 1
        if not in_degree[y]:
            queue.append(y)

# 결과 출력
if len(result) == N:
    for res in result:
        print(res)