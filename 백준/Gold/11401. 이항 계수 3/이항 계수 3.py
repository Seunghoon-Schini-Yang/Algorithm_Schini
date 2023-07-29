def factorial(s, e, val, mod):
    for i in range(s, e):
        val = (val * i) % mod
    return val


class BiCoeffcient():
    def __init__(self, N, K):
        K = min(N, N-K)
        mod = 1_000_000_007

        fac_k = factorial(1, K+1, 1, mod)
        fac_nk = factorial(K+1, N-K+1, fac_k, mod)
        fac_n = factorial(N-K+1, N+1, fac_nk, mod)
        
        mul = (fac_k * fac_nk) % mod
        cur = 1
        for i in map(int, bin(1_000_000_005)[-1:1:-1]):
            if i:
                cur = (cur * mul) % mod
            mul = (mul * mul) % mod
        self.answer = (fac_n * cur) % mod


if __name__ == '__main__':
    bincoff = BiCoeffcient(*map(int, input().split()))
    print(bincoff.answer)
