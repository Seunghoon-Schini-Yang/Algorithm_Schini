import sys
sys.setrecursionlimit(pow(10, 9))


def sol(n: int, k: int) -> int:
    def comb(n: int, k: int) -> int:
        if not k or n==k:
            return 1
        if memo[n][k]:
            return memo[n][k]
        
        memo[n][k] = (comb(n-1,k-1) + comb(n-1,k)) % 10007
        return memo[n][k]

    
    k = min(n-k, k)
    memo = [[0]*(k+1) for _ in range(n+1)]
    return comb(n,k)


print(sol(*map(int, input().split())))
