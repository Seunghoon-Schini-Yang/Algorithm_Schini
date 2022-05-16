from math import comb


def sol(n: int, k: int) -> int:
    return comb(n, k)


print(sol(*map(int, input().split())))
