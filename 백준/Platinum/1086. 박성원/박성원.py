import sys
input = sys.stdin.readline


def sol(n: int) -> str:
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
    k = int(input())
    mod_arr = [(pow(10, len(elem), k), modulo(elem)) for elem in arr]
    memo = [[0] * k for _ in range(1<<n)]
    memo[0][0] = 1

    for mask in range(1<<n):
        for i in range(n):
            if mask&(1<<i):
                p_mask = mask & ~(1<<i)
                for j in range(k):
                    memo[mask][(j*mod_arr[i][0] + mod_arr[i][1]) % k] += memo[p_mask][j]

    numer = memo[(1<<n)-1][0]
    denom = sum(memo[(1<<n)-1])
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
