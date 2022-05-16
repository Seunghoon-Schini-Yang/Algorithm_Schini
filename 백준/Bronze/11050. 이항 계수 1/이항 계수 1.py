from math import factorial


def sol(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n-k))


print(sol(*map(int, input().split())))
