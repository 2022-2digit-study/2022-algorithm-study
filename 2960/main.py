# (BOJ - 2960) 예라토스테네스의 체: https://www.acmicpc.net/problem/2960
import sys

N, K = map(int, sys.stdin.readline().split())

nums = list(range(2, N + 1))


def get_remove_order(nums):
    count = 0
    while nums:
        for i in range(nums[0], N+1, nums[0]):
            if i in nums:
                nums.remove(i)
                count += 1
                if count == K:
                    return i


print(get_remove_order(nums))