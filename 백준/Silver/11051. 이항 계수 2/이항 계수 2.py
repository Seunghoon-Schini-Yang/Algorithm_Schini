def sol(n: int, k: int) -> int:
    k = min(n-k, k); ans = 1
    for s,b in enumerate(range(n, n-k, -1), start=1):
        ans = ans*b//s
    return ans%10007


print(sol(*map(int, input().split())))