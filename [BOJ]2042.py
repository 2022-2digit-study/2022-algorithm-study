# 백준 - https://www.acmicpc.net/problem/2042

import sys


def init_tree(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        tree[node] = init_tree(node * 2, start, (start + end) // 2) + init_tree(node * 2 + 1, (start + end) // 2 + 1,
                                                                                end)
        return tree[node]


def subSum(node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    return subSum(node * 2, start, (start + end) // 2, left, right) + subSum(node * 2 + 1, (start + end) // 2 + 1, end,
                                                                             left, right)


def update(node, start, end, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff

    if start != end:
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)
    return


N, M, K = map(int, sys.stdin.readline().split())

arr = [int(sys.stdin.readline()) for _ in range(N)]
tree = [0] * 3000000
init_tree(1, 0, N - 1)

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        diff = c - arr[b - 1]
        arr[b - 1] = c
        update(1, 0, N - 1, b - 1, diff)

    elif a == 2:
        print(subSum(1, 0, N - 1, b - 1, c - 1))
