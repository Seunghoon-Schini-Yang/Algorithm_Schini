import sys
input = sys.stdin.readline


def sol(n: int, k: int) -> int:
    temps = list(map(int, input().split()))
    cur = maxy = sum(temps[:k])
    for i in range(n-k):
        cur += temps[i+k]-temps[i]
        maxy = max(maxy, cur)
    return maxy


print(sol(*map(int, input().split())))
