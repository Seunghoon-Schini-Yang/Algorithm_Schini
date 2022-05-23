# prefix sum
import sys
input = sys.stdin.readline
from math import comb


def sol(n: int, m: int) -> int:
    occur = [0] * m
    occur[0] = 1

    acc = [0] * (n+1)
    nums = map(int, input().split())
    for i in range(n):
        acc[i+1] = (acc[i]+next(nums)) % m
        occur[acc[i+1]] += 1
    
    return sum(comb(i, 2) for i in occur if i > 1)


print(sol(*map(int, input().split())))
