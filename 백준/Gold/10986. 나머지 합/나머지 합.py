# prefix sum + comb (math)
import sys
input = sys.stdin.readline
from math import comb


def sol(n: int, m: int) -> int:
    occur = [0] * m
    occur[0] = 1

    acc = 0
    nums = map(int, input().split())
    for _ in range(n):
        acc = (acc+next(nums)) % m
        occur[acc] += 1
    
    return sum(comb(i, 2) for i in occur if i > 1)


print(sol(*map(int, input().split())))
