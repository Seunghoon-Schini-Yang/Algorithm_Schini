import sys
input = sys.stdin.readline


memo = {'ChongChong'}
for _ in range(int(input())):
    a, b = input().rstrip().split()
    if a in memo or b in memo:
        memo.add(a)
        memo.add(b)
print(len(memo))