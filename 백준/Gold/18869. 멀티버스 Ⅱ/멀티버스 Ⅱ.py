import sys
input = sys.stdin.readline
from collections import defaultdict


def sol(m: int, n: int) -> int:
    unis = defaultdict(int)
    for i in range(m):
        uni = list(map(int, input().split()))
        table = {size:i for i,size in enumerate(sorted(set(uni)))}
        unis[tuple(table[uni[i]] for i in range(n))] += 1

    # skylake 님 코드 참고 (defaultdict)
    return sum(val*(val-1)//2 for val in unis.values())
       

print(sol(*map(int, input().split())))
