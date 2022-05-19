# 백준 - https://www.acmicpc.net/problem/2805

import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

high = max(trees)
low = 0
min_h = 0

while low <= high:
    mid = (low + high) // 2
    if sum([tree - mid for tree in trees if (tree - mid) > 0]) >= M:
        min_h = mid
        low += 1
    else:
        high -= 1

print(min_h)
