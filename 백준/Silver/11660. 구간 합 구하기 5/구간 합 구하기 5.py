# prefix_sum + dp
import sys
input = sys.stdin.readline


def sol(n: int, m: int) -> str:
    table = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        line = map(int, input().split())
        for j in range(n):
            table[i+1][j+1] = next(line) + table[i+1][j] + table[i][j+1] - table[i][j]
    return '\n'.join(map(str, iter(partial_sum(table, *map(int, input().split())) for _ in range(m))))


def partial_sum(table: list, x1: int, y1: int, x2: int, y2: int) -> int:
    return table[x2][y2] - table[x2][y1-1] - table[x1-1][y2] + table[x1-1][y1-1]


print(sol(*map(int, input().split())))
