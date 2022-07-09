import sys
input = sys.stdin.readline
from math import log2


def calc(n: int, x: int) -> int:
    for i in range(N+1):
        if n&(1<<i):
            x = table[i][x]
    return x


if __name__ == '__main__':
    N = int(log2(500_000))
    m = int(input())
    table = [[0]*(m+1) for _ in range(N+1)]
    table[0] = [0] + list(map(int, input().split()))

    for i in range(N):
        for v in range(1, m+1):
            table[i+1][v] = table[i][table[i][v]]

    print('\n'.join(map(str, [calc(*map(int, input().split())) for _ in range(int(input()))])))
