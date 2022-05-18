import sys
input = sys.stdin.readline
from functools import reduce


def sol(t: int) -> str:
    return '\n'.join(str(numofcases(int(input()))) for _ in range(t))


def numofcases(n: int) -> int:
    bucket = dict()
    for _ in range(n):
        key = input().split()[1]
        bucket[key] = bucket.get(key, 1) + 1
        
    ans = 1
    for val in bucket.values():
        ans *= val

    return ans - 1


print(sol(int(input())))
