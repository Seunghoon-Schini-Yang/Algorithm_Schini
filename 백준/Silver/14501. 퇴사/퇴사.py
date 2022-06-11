# dp
import sys
input = sys.stdin.readline


def sol(n: int) -> int:
    memo = [0]*(n+1)
    cur_max = 0
    for i in range(n):
        t,p = map(int, input().split())
        if memo[i] > cur_max:
            cur_max = memo[i] 
        if i+t <= n and memo[i+t] < cur_max+p:
            memo[i+t] = cur_max+p
    return memo[n] if memo[n] > cur_max else cur_max


print(sol(int(input())))
