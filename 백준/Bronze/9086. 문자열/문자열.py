import sys
input = sys.stdin.readline


N = int(input())
for _ in range(N):
    word = input().rstrip()
    print(word[0] + word[-1])