from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
for p1 in range(N):
    sum_candidate = 0
    for p2 in range(p1, N):
        sum_candidate += nums[p2]
        if sum_candidate == M:
            answer += 1

print(answer)
