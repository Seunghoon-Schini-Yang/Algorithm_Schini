import sys
input = sys.stdin.readline


a = sorted([int(input()) for _ in range(5)])
print(sum(a) // 5)
print(a[2])
