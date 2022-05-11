import sys
from math import sqrt
input = sys.stdin.readline
print = sys.stdout.write


def sol(xs: int, ys: int, xe: int, ye: int) -> str:
    cnt = 0
    for _ in range(int(input())):
        cx, cy, r = map(int, input().split())
        cnt += (r > sqrt((cx-xs)**2 + (cy-ys)**2)) ^ (r > sqrt((cx-xe)**2 + (cy-ye)**2))
    return str(cnt) + '\n'

for _ in range(int(input())):
    print(sol(*map(int, input().split())))
