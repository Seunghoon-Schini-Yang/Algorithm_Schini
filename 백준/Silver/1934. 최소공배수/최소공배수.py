import sys
from math import lcm
input = sys.stdin.readline


def sol(n: int) -> None:
    return '\n'.join(str(lcm(*map(int, input().split()))) for _ in range(n))


print(sol(int(input())))
