import sys
input = sys.stdin.readline


def sol(n: int) -> str:
    deck = set(input().split())
    input()
    return ' '.join('1' if x in deck else '0' for x in input().split())


print(sol(int(input())))
