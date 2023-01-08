import sys
input = sys.stdin.readline


N, M = map(int, input().split())
x = [map(int, input().split()) for _ in range(N)]
y = [map(int, input().split()) for _ in range(N)]

for rx, ry in zip(x, y):
    for cx, cy in zip(rx, ry):
        print(cx+cy, end=' ')
    print()
