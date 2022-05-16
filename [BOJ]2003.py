# 백준 - https://www.acmicpc.net/problem/2003

import sys

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(N):
    temp_sum = 0
    for j in range(i, N):
        temp_sum += num_list[j]
        if temp_sum > M:
            break
        elif temp_sum == M:
            cnt += 1
            break
print(cnt)
