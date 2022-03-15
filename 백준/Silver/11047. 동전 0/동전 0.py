import sys
input = sys.stdin.readline


def solution(info: map) -> int:
    n, goal = info
    coins = [int(input()) for _ in range(n)]
    sumy = 0
    for i in range(n):
        if goal < coins[~i]:
            continue
        else:
            sumy += goal // (coin := coins[~i])
            goal %= coin
    
    return sumy


print(solution(map(int, input().split())))
