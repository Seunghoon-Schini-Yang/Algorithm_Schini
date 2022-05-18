import sys
input = sys.stdin.readline
from functools import reduce


def sol(t: int) -> str:
    return '\n'.join(str(numofcases(int(input()))) for _ in range(t))


def numofcases(n: int) -> int:
    if not n:
        return 0
    
    bucket = dict()
    for _ in range(n):
        key = input().split()[1]
        bucket[key] = bucket.get(key, 1) + 1

    return reduce((lambda x,y: x*y), bucket.values()) - 1


print(sol(int(input())))
