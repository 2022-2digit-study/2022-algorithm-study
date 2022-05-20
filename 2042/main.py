# [BOJ - 2042] 구간 합 구하기 - https://www.acmicpc.net/problem/2042

import sys

N, M = map(int, sys.stdin.readline().split())
nodes = [int(input()) for _ in range(N)]
trees = [0] * (2 * N)


def init(start, end, ti):
    print(f"{start} {end} {ti}")
    if start == end:
        trees[ti] = nodes[start - 1]
    else:
        mid = (start + end) // 2
        trees[ti] = init(start, mid, ti * 2) + init(mid + 1, end, ti * 2 + 1)
    return trees[ti]


def segment_sum(start, end, left, right, ti):
    if start == left and end == right:
        return trees[ti]
    elif start <= left <= end and start <= right <= end:
        mid = (start + end) // 2
        return segment_sum(start, mid, left, right, ti * 2) + segment_sum(mid+1, end, left, right, ti * 2)
    #elif :

    else:
        return 0


init(1, N, 1)
print(trees)
