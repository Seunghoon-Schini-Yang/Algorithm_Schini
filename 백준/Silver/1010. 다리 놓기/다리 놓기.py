import sys
input = sys.stdin.readline
from math import comb


def sol(n: int) -> str:
    return '\n'.join(str(get_comb(*map(int, input().split()))) for _ in range(n))


def get_comb(k: int, n: int) -> int:
    return comb(n, k)


print(sol(int(input())))
