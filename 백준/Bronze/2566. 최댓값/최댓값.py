import sys
input = sys.stdin.readline


maxy = -1
for row in range(1, 10):
    for col, val in enumerate(map(int, input().split()), start=1):
        if val > maxy:
            x = row; y = col
            maxy = val

print(maxy)
print(x, y)
