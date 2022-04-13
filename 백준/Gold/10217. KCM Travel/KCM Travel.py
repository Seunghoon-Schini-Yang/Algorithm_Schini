# dp, brute force, O(n*m)
import sys
input = sys.stdin.readline
import math

def sol(n: int, m: int, k: int) -> str:
    INF = math.inf
    is_finite = math.isfinite

    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        u,v,c,d = map(int, input().split())
        graph[u].append((d,c,v))
    dp = [[INF]*(m+1) for _ in range(n+1)]
    dp[1][0] = 0
    
    for c in range(m+1):
        for v in range(1,n+1):
            if is_finite(dp[v][c]):
                for c_d,c_c,c_v in graph[v]:
                    if c+c_c <= m and dp[v][c]+c_d < dp[c_v][c+c_c]:
                        dp[c_v][c+c_c] = dp[v][c]+c_d
    
    ans = min(dp[n])
    return str(ans) if is_finite(ans) else 'Poor KCM'


print('\n'.join(sol(*map(int, input().split())) for _ in range(int(input()))))
