# (BOJ -1735) 분수 합: https://www.acmicpc.net/problem/1735
import sys


def get_gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if not a % i and not b % i:
            return i
    return 1


nums = []
for _ in range(2):
    boon_son, boon_mom = map(int, sys.stdin.readline().split())
    nums.append((boon_son, boon_mom))

calc_boon_mom = nums[0][1] * nums[1][1]
calc_boon_son = nums[0][0] * nums[1][1] + nums[1][0] * nums[0][1]

gcd = get_gcd(calc_boon_mom, calc_boon_son)
print(calc_boon_son // gcd, calc_boon_mom // gcd)
