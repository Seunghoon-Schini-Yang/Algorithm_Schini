# bitmask dp + dfs (recursive)
import sys
input = sys.stdin.readline


def dfs(node: int, mask: int) -> int:
    if memo[node][mask] < INF:
        return memo[node][mask]
    
    if mask == (1<<n)-1:
        memo[0][mask] = sub_INF if not weight[0][node] else weight[0][node]
        return memo[0][mask]
    
    for i in range(1, n):
        if not mask&(1<<i):
            if not weight[i][node]:
                weight[i][node] = sub_INF
            memo[node][mask] = min(memo[node][mask], dfs(i, mask|(1<<i)) + weight[i][node])
    return memo[node][mask]


if __name__ == '__main__':
    n = int(input())
    INF = pow(10, 9)
    sub_INF = pow(10, 8)
    weight = [list(map(int, input().split())) for _ in range(n)]


    memo = [[INF]*(1<<n) for _ in range(n)]
    print(dfs(0, 1))
