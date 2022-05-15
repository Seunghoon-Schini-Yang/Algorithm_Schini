import sys
input = sys.stdin.readline


def sol(n: int) -> str:
    def dfs(mask: int, n_len: int) -> dict:
        if not n_len:
            return {0: 1}
        if memo[mask]:
            return memo[mask]

        for i in range(n):
            if not mask&(1<<i):
                rem = modulo(arr[i].ljust(n_len, '0'))
                for k,v in dfs(mask|(1<<i), n_len-len(arr[i])).items():
                    memo[mask][(rem+k)%dvr] = v + memo[mask].get((rem+k)%dvr, 0)
        return memo[mask]


    def modulo(n: str) -> int:
        n_len = len(n)
        while n_len >= 3:
            n = str(int(n[:3]) % dvr) + n[3:]
            n_len = len(n)
        n = int(n)

        if n >= dvr:
            n %= dvr
        return n
    

    arr = [input().rstrip() for _ in range(n)]
    tot_len = 0
    for num in arr:
        tot_len += len(num)
    dvr = int(input())
    memo = [{} for _ in range(1<<n)]

    result = dfs(0, tot_len)
    numer = result.get(0, 0)
    denom = sum(result.values())
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
