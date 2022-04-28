# disjoint set + union_find + recursive
import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10,9))

def sol(n: int, m: int) -> str:
    p = [-1] * (n+1)
    for i in range(1,n):
        line = map(int, input().split())
        for _ in range(i):
            next(line)
        for j in range(i+1,n+1):
            if next(line):
                union(p, find(p,i), find(p,j))

    input()
    line = map(int, input().split())
    root = find(p,next(line))

    for i in line:
        root_2 = find(p,i)
        if root != root_2:
            return 'NO'

    return 'YES'


def find(p: list, n: int) -> int:
    if p[n] < 0:
        return n
    p[n] = find(p,p[n])
    return p[n]


def union(p: list, x: int, y: int) -> None:
    if x == y:
        return
    
    if p[x] > p[y]:
        p[x] = y
    else:
        p[y] = x
        if p[x] == p[y]:
            p[x] -= 1


print(sol(int(input()), int(input())))
