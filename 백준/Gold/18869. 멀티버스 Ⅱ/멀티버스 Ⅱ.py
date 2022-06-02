import sys
input = sys.stdin.readline


def sol(m: int, n: int) -> int:
    unis = [[] for _ in range(m)]
    for i in range(m):
        uni = list(map(int, input().split()))
        table = {size:i for i,size in enumerate(sorted(set(uni)))}
        unis[i] = [table[uni[i]] for i in range(n)]
    unis.sort()

    acc = 0; cnt = 1
    for i in range(m-1):
        if unis[i] == unis[i+1]:
            cnt += 1
        else:
            acc += cnt*(cnt-1)//2
            cnt = 1
    acc += cnt*(cnt-1)//2
    return acc


print(sol(*map(int, input().split())))
