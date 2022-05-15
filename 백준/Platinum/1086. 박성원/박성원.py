import sys
input = sys.stdin.readline


def sol(n: int) -> str:
    def dfs(mask: int, n_len: int) -> None:
        if not n_len or visited[mask]:
            return

        visited[mask] = 1
        for i in range(n):
            if not mask&(1<<i):
                rem = modulo(arr[i].ljust(n_len, '0'))
                c_mask = mask|(1<<i)
                dfs(c_mask, n_len-len(arr[i]))
                for j in range(k):
                    if memo[c_mask][j]:
                        memo[mask][(rem+j)%k] += memo[c_mask][j]


    def modulo(n: str) -> int:
        n_len = len(n)
        while n_len >= 3:
            n = str(int(n[:3]) % k) + n[3:]
            n_len = len(n)
        n = int(n)

        if n >= k:
            n %= k
        return n
    

    arr = [input().rstrip() for _ in range(n)]
    tot_len = 0
    for num in arr:
        tot_len += len(num)
    k = int(input())
    memo = [[0] * k for _ in range(1<<n)]
    memo[(1<<n)-1][0] = 1
    visited = [0] * (1<<n)

    dfs(0, tot_len)
    numer = memo[0][0]
    denom = sum(memo[0])
    if not numer:
        return '0/1'
    else:
        gcd = get_gcd(numer, denom)
        return f'{numer//gcd}/{denom//gcd}'


def get_gcd(x: int, y: int) -> int:
    if not y % x:
        return x
    return get_gcd(y % x, x)


print(sol(int(input())))
