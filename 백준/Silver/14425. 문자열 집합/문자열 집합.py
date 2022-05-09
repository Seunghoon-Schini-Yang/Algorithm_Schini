import sys
input = sys.stdin.readline


def sol(n: int, m: int) -> int:
    deck = {input() for _ in range(n)}
    return sum(1 if input() in deck else 0 for _ in range(m))


print(sol(*map(int, input().split())))
