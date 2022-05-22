# accumulate (itertools)
import sys
input = sys.stdin.readline
from itertools import accumulate


def sol(n: int, m: int) -> str:
    acc = [0] + list(accumulate(map(int, input().split())))
    return '\n'.join(map(str, [partial_sum(acc, *map(int, input().split())) for _ in range(m)]))


def partial_sum(acc: int, s: int, e: int) -> list:
    return acc[e] - acc[s-1]


print(sol(*map(int, input().split())))
