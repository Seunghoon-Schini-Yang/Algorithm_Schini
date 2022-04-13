import sys
input = sys.stdin.readline

def sol(n: int) -> int:
    values = sorted(map(int, input().split()))
    goal = int(input())
    i, j = 0, len(values)-1
    cnt = 0
    while i < j:
        sumx = values[i] + values[j]
        if sumx > goal:
            j -= 1
        elif sumx < goal:
            i += 1
        else:
            i += 1
            j -= 1
            cnt += 1
    return cnt


print(sol(int(input())))
