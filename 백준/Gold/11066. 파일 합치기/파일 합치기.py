import sys
input = sys.stdin.readline
from itertools import accumulate

def solution(n: int) -> int:
    files = [0] + list(map(int, input().split()))
    acc = list(accumulate(files))
    dp = [[0] * (n+1) for _ in range(n+1)]
    knuth = [[0] * (n+1) for _ in range(n+1)]
    
    for step in range(1, n):
        for e in range(step+1, n+1):
            s = e-step
            if e == s+1:
                dp[s][e] = acc[e] - acc[s-1]
                knuth[s][e] = s
            else:
                miny = sys.maxsize
                for k in range(knuth[s][e-1], knuth[s+1][e] + 1):
                    if dp[s][k] + dp[k+1][e] < miny:
                        miny = dp[s][k] + dp[k+1][e]
                        min_k = k
                knuth[s][e] = min_k
                dp[s][e] = acc[e] - acc[s-1] + miny


    return dp[1][n]


print('\n'.join([str(solution(int(input()))) for _ in range(int(input()))]))
