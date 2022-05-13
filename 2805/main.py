# (BOJ - 2805) 나무 자르기: https://www.acmicpc.net/problem/2805

N, M = map(int, input().split())
trees = list(map(int, input().split()))
answer = 0
left = 0
right = max(trees)


def sum_cut_trees(height):
    gathering_tree = 0
    for i in range(N):
        if (rest_tree := trees[i] - height) > 0:
            gathering_tree += rest_tree
    return gathering_tree


while left <= right:
    mid = (left + right) // 2
    if sum_cut_trees(mid) >= M:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)