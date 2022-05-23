# [BOJ - 2042] 구간 합 구하기 - https://www.acmicpc.net/problem/2042

import sys

N, M, K = map(int, sys.stdin.readline().split())
nodes = [int(sys.stdin.readline()) for _ in range(N)]
trees = [0] * (4 * N)


def init(start, end, ti):
    if start == end:
        trees[ti] = nodes[start - 1]
    else:
        mid = (start + end) // 2
        trees[ti] = init(start, mid, ti * 2) + init(mid + 1, end, ti * 2 + 1)
    return trees[ti]


def segment_sum(start, end, left, right, ti):
    if end < left or start > right:  # 구하려는 범위 밖에 노드 범위가 위치
        return 0
    if start >= left and right >= end:  # 구하려는 범위 안에 노드 범위가 위치
        return trees[ti]
    # 범위에 겹쳐있음
    mid = (start + end) // 2
    return segment_sum(start, mid, left, right, ti * 2) + segment_sum(mid + 1, end, left, right, ti * 2 + 1)


def update_node(start, end, node, ti, dif):
    if start <= node <= end:
        trees[ti] += dif
        if start != end:  # 리프노드
            mid = (start + end) // 2
            update_node(start, mid, node, ti * 2, dif)
            update_node(mid + 1, end, node, ti * 2 + 1, dif)


init(1, N, 1)
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:  # 수정
        update_node(1, N, b, 1, c - nodes[b-1])
    else:  # 구간 합
        print(segment_sum(1, N, b, c, 1))
