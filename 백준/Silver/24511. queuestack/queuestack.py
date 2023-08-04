import sys
input = sys.stdin.readline


int(input())
x = [b for a, b in zip(map(int, input().split()), map(int, input().split())) if not a][::-1]
m = int(input())
x.extend(list(map(int, input().split())))
print(*x[:m])
