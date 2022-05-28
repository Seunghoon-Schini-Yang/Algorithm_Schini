import sys
input = sys.stdin.readline


def sol(n: int) -> list:
    arr = list(map(int, input().split()))
    table = {val: i for i, val in enumerate(sorted(set(arr)))}
    return [table[val] for val in arr]


print(*sol(int(input())))
