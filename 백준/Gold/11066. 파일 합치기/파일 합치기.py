import sys
input = sys.stdin.readline
from itertools import accumulate

def solution(n: int) -> int:
    files = [0] + list(map(int, input().split()))
    acc = list(accumulate(files))
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for step in range(1, n):
        for e in range(step+1, n+1):
            s = e-step
            if e == s+1:
                dp[s][e] = acc[e] - acc[s-1]
            else:
                dp[s][e] = acc[e] - acc[s-1] + min(dp[s][k] + dp[k+1][e] for k in range(s, e))

    return dp[1][n]


print('\n'.join([str(solution(int(input()))) for _ in range(int(input()))]))