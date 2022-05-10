import sys, math
input = sys.stdin.readline


def sol(n: int, w: int, h: int) -> str:
    max_len = math.sqrt(w**2 + h**2)
    return '\n'.join('DA' if int(input()) <= max_len else 'NE' for _ in range(n))


print(sol(*map(int, input().split())))
